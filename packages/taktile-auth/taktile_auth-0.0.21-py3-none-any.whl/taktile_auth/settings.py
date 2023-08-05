import pathlib

import pkg_resources
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str = "local"
    RESOURCE_PATH: pathlib.Path = pathlib.Path(
        pkg_resources.resource_filename(
            "taktile_auth", "assets/resources.yaml"
        )
    )
    ROLE_PATH: pathlib.Path = pathlib.Path(
        pkg_resources.resource_filename("taktile_auth", "assets/roles.yaml")
    )

    CACHE_SPEEDUP_TIME_MINUTES: int = 60
    CACHE_FALLBACK_TIME_MINUTES: int = 60 * 72


settings = Settings()
