from dynaconf import Dynaconf
from os import getenv
from dataclasses import dataclass, field
from adaptix import Retort

@dataclass(slots=True)
class ApiConfig:
    host: str
    port: int

    project_name: str = 'websockChat'
    allow_origins: list[str] = field(default_factory=list)
    allow_methods: list[str] = field(default_factory=list)
    allow_headers: list[str] = field(default_factory=list)
    allow_credentials: bool = True

@dataclass(slots=True)
class Config:
    api:ApiConfig

def get_config() -> Config:
    dynaconf = Dynaconf(
        settings_files = ['./src/config.toml'],
        load_dotenv = True
    )

    retort = Retort()

    cfg:Config = retort.load(dynaconf,Config)

    return cfg

config:Config = get_config()