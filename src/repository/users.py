from abc import ABC, abstractmethod

from redis import Redis

from src.models.user import User


class Users(ABC):
    @abstractmethod
    def get_user(self, username: str) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def set_user(self, user: User) -> None:
        raise NotImplementedError


class RedisUsers(Users):
    __redis: Redis

    def __init__(self, redis: Redis):
        self.__redis = redis

    def get_user(self, username: str) -> User | None:
        user = self.__redis.get(f'u{username}')
        if user is None: return None
        return User.model_validate_json(user)

    def set_user(self, user: User) -> None:
        self.__redis.set(f'u{user.username}', user.model_dump_json())
