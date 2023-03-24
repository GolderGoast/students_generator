from typing import Any

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    groups_count: int = 10
    students_in_group_count: int = 30
    type_report: str = "db"
    scheme_db: str = "postgresql"
    user_db: str = "postgres"
    password_db: str = "postgres"
    name_db: str = "reports"
    host_db: str = "localhost"
    port_db: str = "5432"
    dsn: str | None

    @validator("dsn", pre=True)
    def dsn_build(cls, value: str | None, values: dict[str, Any]):
        if isinstance(value, str):
            return value

        return PostgresDsn.build(
            scheme=values["scheme_db"],
            host=values["host_db"],
            port=values["port_db"],
            user=values["user_db"],
            password=values["password_db"],
            path=f"/{values['name_db']}",
        )

    class Config:
        env_file = ".env"


settings = Settings()

GROUPS_COUNT = settings.groups_count
STUDENTS_IN_GROUP_COUNT = settings.students_in_group_count
TYPE_REPORT = settings.type_report

DSN_DB = settings.dsn
