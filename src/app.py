from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.deps import deps
from src.routers.auth import auth_router
from src.routers.chat import chat_router

app = FastAPI(title='webSockChat')
app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_methods=['*'])

app.include_router(chat_router, prefix='/api', dependencies=deps)
app.include_router(auth_router, prefix='/api', dependencies=deps)
