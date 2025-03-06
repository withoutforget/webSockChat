from fastapi import APIRouter, FastAPI

from src.presentation.fastapi.routes.auth.api import router as auth_router

def setup_routes(app:FastAPI):
    router = APIRouter()

    router.include_router(auth_router, prefix = '/auth')

    app.include_router(router, prefix='/api')
