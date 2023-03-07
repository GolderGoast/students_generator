import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

GROUPS_COUNT = int(os.getenv("GROUPS_COUNT"))
STUDENTS_IN_GROUP_COUNT = int(os.getenv("STUDENTS_IN_GROUP_COUNT"))
TYPE_REPORT = os.getenv("TYPE_REPORT")
