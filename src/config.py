class ApiConfig:
    host: str
    port: int

    project_name: str
    allow_origins: list[str]
    allow_methods: list[str]
    allow_headers: list[str]
    allow_credentials: bool = True

def get_api() -> ApiConfig:
    api = ApiConfig()

    api.project_name = 'webSockChat'

    api.allow_origins = ['*']
    api.allow_methods = ['*']
    api.allow_headers = ['*']

    return api

class Config:
    api:ApiConfig

def get_config() -> Config:
    cfg = Config()

    cfg.api = get_api()

    return cfg

config:Config = get_config()