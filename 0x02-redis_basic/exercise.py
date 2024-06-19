#!/usr/bin/env python3
"""
A module for managing data storage with Redis.
"""
from functools import wraps
from typing import Callable, Union, Any
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of calls to the cache methods.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Increment call count in Redis and call the actual method.
        """
        key = f"count:{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for each method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Store input and output history in Redis.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


def replay(method: Callable) -> None:
    """
    Function to display the history of calls of a particular method.
    """
    self = method.__self__
    method_name = method.__qualname__
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"
    count = self._redis.get(f"count:{method_name}")

    print(f"{method_name} was called {count.decode('utf-8')} times:")

    inputs = self._redis.lrange(inputs_key, 0, -1)
    outputs = self._redis.lrange(outputs_key, 0, -1)

    for input_, output in zip(inputs, outputs):
        print(f"{method_name}(*{input_.decode('utf-8')}) -> {output.decode('utf-8')}")


class Cache:
    """
    Cache class for storing and retrieving data from Redis.
    """

    def __init__(self) -> None:
        """
        Initialize the Redis connection and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a unique key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        Retrieve and optionally transform data from Redis by key.
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Retrieve a string value from Redis.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieve an integer value from Redis.
        """
        return self.get(key, lambda x: int(x))
