from typing import Annotated

from fastapi import Depends
from redis import Redis, ConnectionPool

from src.repository.messages import RedisMessages
from src.repository.users import RedisUsers
from src.services.auth import AuthService
from src.services.message import MessageService

redis = ConnectionPool()
users, messages = RedisUsers(Redis(connection_pool=redis)), RedisMessages(Redis(connection_pool=redis))
auth_service, message_service = AuthService(users), MessageService(messages)


async def get_authservice() -> AuthService: return auth_service


async def get_msgservice() -> MessageService: return message_service


deps = [
    Depends(get_authservice),
    Depends(get_msgservice)
]
AuthDep = Annotated[AuthService, Depends(get_authservice)]
MessageDep = Annotated[MessageService, Depends(get_msgservice)]
