from src.config import get_config, Config
from src.main.web import setup_fastapi

config:Config = get_config()

app = setup_fastapi(config.api)

__all__ = ['app', 'config']