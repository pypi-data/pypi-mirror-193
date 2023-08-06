from functools import wraps
from flask import request, make_response, jsonify
from json import JSONDecodeError
import json
import uuid
import logging
import redis
import copy
import deepdiff
import time


def jwt_redis_auth(
    redis_instance: redis, channel_name: str, pub_message: dict, response_template: dict
):
    def funct_decorator(org_function):
        @wraps(org_function)
        def authorize(*args, **kwargs):
            """
            Authorization method that runs before all request to check if upcoming request
            is authorized in the system.
            """
            publish_message = copy.deepcopy(pub_message)
            response_message = copy.deepcopy(response_template)

            logging.info("Authorization")
            token = request.headers.get("Authorization")
            if token:
                token = token.replace("Bearer ", "")
            else:
                logging.error("Bearer Token was not found.")
                return _make_response("Token is missing", 401)

            request_id = str(uuid.uuid4())

            try:
                logging.info("Connecting to Redis Server")
                redis_client = redis_instance.client()
                pubsub = redis_client.pubsub()
                pubsub.subscribe(channel_name + ".reply")

                publish_message = _transform_dict(publish_message, token, request_id)
                response_message = _transform_dict(response_message, "", request_id)

                logging.info("Publishing message to Redis server for token validation.")
                redis_client.publish(
                    channel_name,
                    json.dumps(publish_message),
                )

                try:
                    timeout = 5.0
                    live_timeout = time.time() + 5
                    logging.info("Waiting for Redis response.")
                    pubsub.get_message()
                    while True:
                        if time.time() > live_timeout:
                            raise TimeoutError
                        message = pubsub.get_message(timeout=timeout)
                        if message:
                            redis_response = {}
                            for key, value in message.items():
                                redis_response[key] = _transform_redis_response(value)
                            diff = deepdiff.DeepDiff(response_message, redis_response)
                            if diff == {}:
                                logging.info("Redis response - Token is valid")
                                break
                            values = diff.get("values_changed", {})
                            for change in values.values():
                                if change["old_value"] == request_id:
                                    continue
                            logging.info("Redis response - Token is invalid")
                            return _make_response("Unauthorized", 401)
                        else:
                            raise TimeoutError
                except TimeoutError:
                    logging.error(
                        "Haven't received any answer from Redis for 5 seconds."
                    )
                    return _make_response("Gateway Timeout", 504)
                pubsub.unsubscribe(channel_name + ".reply")
            except redis.exceptions.ConnectionError:
                logging.error("Redis refused to connect.")
                return _make_response("Bad Gateway", 502)

            return org_function(*args, **kwargs)

        return authorize

    return funct_decorator


def _transform_dict(data, new_token: str = "", new_id: str = "") -> dict:
    """
    Function to insert into given dictionary `Token` and `ID` fields.
    returns and
    :param data: Dictionary where to apply transformation
    :type data: dict
    :param new_token: Token string to place in dictionary
    :type new_token: str
    :param new_id: ID string to place in dictionary
    :type new_id: str
    :return: Transformed dictionary
    :rtype: dict
    """
    working_dict = copy.deepcopy(data)
    for key, value in working_dict.items():
        if working_dict[key] == "TOKEN":
            working_dict[key] = new_token
        elif working_dict[key] == "ID":
            working_dict[key] = new_id
        elif isinstance(value, dict):
            working_dict[key] = _transform_dict(value, new_token, new_id)
    return working_dict


def _transform_redis_response(data):
    """
    Function to transform response from Redis message broker to Python Dictionary
    :param data: Redis response values
    :type data: all
    :return: Returns transformed redis value
    :rtype: all
    """
    try:
        if isinstance(data, dict):
            loaded_d = data
        else:
            loaded_d = json.loads(data)
        for key, value in loaded_d.items():
            loaded_d[key] = _transform_redis_response(value)
    except (JSONDecodeError, TypeError):
        if isinstance(data, bytes):
            return data.decode("utf-8")
        return data
    return loaded_d


def _make_response(message: str, status_code: int):
    """
    Function to make a Flask response and return it back.
    This response will contain JSON body with 2 parameters - `message`
    (response message, answer) and `status_code` (integer value of HTTP response code).
    :param message: Message on the response
    :type message: str
    :param status_code:
    :type status_code:
    :return: Flask Response
    :rtype: Response
    """
    return (
        make_response(
            jsonify(
                {
                    "message": message,
                    "statusCode": status_code,
                }
            )
        ),
        status_code,
    )
