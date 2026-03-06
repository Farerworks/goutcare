import os
from dataclasses import dataclass, field

from dotenv import load_dotenv


load_dotenv()


def _env(key: str, default: str = "") -> str:
    return os.getenv(key, default)


@dataclass
class Settings:
    DB_HOST: str = field(default_factory=lambda: _env("DB_HOST", "db"))
    DB_PORT: str = field(default_factory=lambda: _env("DB_PORT", "5432"))
    DB_USER: str = field(default_factory=lambda: _env("DB_USER", "postgres"))
    DB_PASS: str = field(default_factory=lambda: _env("DB_PASS", "postgres"))
    DB_NAME: str = field(default_factory=lambda: _env("DB_NAME", "postgres"))
    SECRET_KEY: str = field(default_factory=lambda: _env("SECRET_KEY", ""))
    DATABASE_URL: str = field(init=False)

    def __post_init__(self) -> None:
        default_url = (
            f"postgresql://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
        self.DATABASE_URL = _env("DATABASE_URL", default_url)


settings = Settings()
