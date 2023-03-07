from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    MALE = 0
    FEMALE = 1


@dataclass
class Student:
    full_name: str
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


class IAdministrator(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def add_group(self):
        pass

    @abstractmethod
    def del_group(self):
        pass

    @abstractmethod
    def rename_group(self):
        pass

    @abstractmethod
    def add_student(self):
        pass

    @abstractmethod
    def del_student(self):
        pass

    @abstractmethod
    def rename_student(self):
        pass

    @abstractmethod
    def add_timetable(self):
        pass

    @abstractmethod
    def del_timetable(self):
        pass

    @abstractmethod
    def change_timetable(self):
        pass


class IFakeStudentDataCreator(ABC):
    @abstractmethod
    def get_fullname(self) -> str:
        pass

    @abstractmethod
    def get_age(self) -> int:
        pass

    @abstractmethod
    def get_gender(self) -> str:
        pass

    @abstractmethod
    def get_weight(self) -> int:
        pass

    @abstractmethod
    def get_height(self) -> int:
        pass

    @abstractmethod
    def get_average_score(self) -> float:
        pass


class IFakeGroupDataCreator(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


class IStudentCreator(ABC):
    def __init__(self, faker: IFakeStudentDataCreator):
        self.faker = faker

    @abstractmethod
    def run(self) -> Student:
        pass


class IGroupCreator(ABC):
    def __init__(self, faker: IFakeGroupDataCreator):
        self.faker = faker

    @abstractmethod
    def run(self, students: list[Student], timetable: TimeTable) -> Group:
        pass


class ISubjectDataCreator(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_day(self):
        pass

    @abstractmethod
    def get_time(self):
        pass


class ISubjectCreator(ABC):
    def __init__(self, subj_data: ISubjectDataCreator):
        self.subj_data = subj_data

    @abstractmethod
    def run(self) -> Subject:
        pass


class ITimeTableCreator(ABC):
    def __init__(self):
        self.subjects: list[Subject] = []

    @abstractmethod
    def run(self, week: tuple[str, ...], times: tuple[str, ...], names: tuple[str, ...]) -> TimeTable:
        pass
