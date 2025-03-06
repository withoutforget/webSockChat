from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import ApiConfig

from src.presentation.fastapi.setup import setup_routes

def setup_fastapi(config: ApiConfig) -> FastAPI:
    app = FastAPI(
        title = config.project_name
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins = config.allow_origins,
        allow_methods = config.allow_methods,
        allow_headers = config.allow_headers,
        allow_credentials = config.allow_credentials,
    )

    setup_routes(app)

    return app
