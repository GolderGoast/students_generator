from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Student:
    full_name: str
    age: int
    gender: str
    weight: int
    height: int
    average_score: float


@dataclass
class Group:
    name: str
    students: list[Student]


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
    def run(self, students: list[Student]) -> Group:
        pass
