from pydantic import BaseSettings


class Settings(BaseSettings):
    groups_count: int
    students_in_group_count: int
    type_report: str

    class Config:
        env_file = ".env"


settings = Settings()

GROUPS_COUNT = settings.groups_count
STUDENTS_IN_GROUP_COUNT = settings.students_in_group_count
TYPE_REPORT = settings.type_report
