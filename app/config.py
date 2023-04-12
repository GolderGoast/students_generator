from typing import Any

from pydantic import BaseSettings, PostgresDsn, validator


class AppSettings(BaseSettings):
    groups_count: int = 10
    students_in_group_count: int = 30
    type_report: str = "db"


class DBSettings(BaseSettings):
    postgres_scheme: str = "postgresql"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db: str = "reports"
    postgres_host: str = "localhost"
    postgres_port: str = "5432"
    dsn: str | None

    @validator("dsn", pre=True)
    def dsn_build(cls, value: str | None, values: dict[str, Any]):
        if isinstance(value, str):
            return value

        return PostgresDsn.build(
            scheme=values["postgres_scheme"],
            host=values["postgres_host"],
            port=values["postgres_port"],
            user=values["postgres_user"],
            password=values["postgres_password"],
            path=f"/{values['postgres_db']}",
        )


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    db: DBSettings = DBSettings()


settings = Settings()
