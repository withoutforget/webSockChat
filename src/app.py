from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from redis import Redis

from Repository import Users, Messages, RedisUsers, RedisMessages
from Routers import chat_router, auth_router
from Services import AuthService, MessageService

app = FastAPI(title = 'webSockChat')
app.add_middleware(CORSMiddleware,
                   allow_origins = ['*'],
                   allow_methods = ['*'])

from deps import deps

app.include_router(chat_router, prefix = '/api', dependencies=deps)
app.include_router(auth_router, prefix = '/api', dependencies=deps)
