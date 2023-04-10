from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    MALE = 0
    FEMALE = 1


@dataclass
class Admin:
    email: str
    password: str


@dataclass
class Student:
    full_name: str
    email: str
    password: str
    age: int
    gender: str
    weight: int
    height: int
    average_score: float


@dataclass
class Subject:
    name: str
    day_of_week: str
    time: str


@dataclass
class TimeTable:
    subjects: list[Subject]
    week: tuple[str, ...]
    times: tuple[str, ...]


@dataclass
class Group:
    name: str
    students: list[Student]
    timetable: TimeTable
