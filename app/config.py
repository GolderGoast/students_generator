from pydantic import BaseSettings


class Settings(BaseSettings):
    groups_count: int
    students_in_group_count: int
    type_report: str
    user_db: str
    password_db: str
    name_db: str
    host_db: str

    class Config:
        env_file = ".env"


settings = Settings()

GROUPS_COUNT = settings.groups_count
STUDENTS_IN_GROUP_COUNT = settings.students_in_group_count
TYPE_REPORT = settings.type_report

USER_DB = settings.user_db
PASSWORD_DB = settings.password_db
NAME_DB = settings.name_db
HOST_DB = settings.host_db
