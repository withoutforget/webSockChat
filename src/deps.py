from typing import Annotated

from fastapi import Depends
from redis import Redis, ConnectionPool

from Repository import RedisUsers, RedisMessages
from Services import MessageService, AuthService

redis = ConnectionPool()
users, messages = RedisUsers(Redis(connection_pool=redis)), RedisMessages(Redis(connection_pool=redis))
auth_service, message_service = AuthService(users), MessageService(messages)

async def get_authservice() -> AuthService: return auth_service
async def get_messageservice() -> MessageService: return message_service
deps = [
    Depends(get_authservice),
    Depends(get_messageservice)
]
AuthDep = Annotated[AuthService, Depends(get_authservice)]
MessageDep = Annotated[MessageService, Depends(get_messageservice)]