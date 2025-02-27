from abc import ABC, abstractmethod

from redis import Redis

from Models import MessageList, Message


class Messages(ABC):
    @abstractmethod
    def get_all(self) -> MessageList:
        raise NotImplementedError

    @abstractmethod
    def add(self,message: Message) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_after(self, timestamp: int) -> MessageList:
        raise NotImplementedError

class RedisMessages(Messages):
    __redis: Redis

    def __init__(self, redis:Redis):
        self.__redis = redis

        if self.__redis.get('msgs') is None:
            self.__redis.set('msgs', MessageList(messages=[]).model_dump_json())

    def get_all(self) -> MessageList:
        res = self.__redis.get('msgs')
        return MessageList.model_validate_json(res)

    def add(self, msg: Message) -> None:
        res = self.get_all()
        res.messages.append(msg)
        self.__redis.set('msgs', res.model_dump_json())

    def get_after(self, timestamp: int) -> MessageList:
        return MessageList(messages=[i for i in self.get_all().messages if i.timestamp > timestamp])
