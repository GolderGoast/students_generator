from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass()
class Student:
    full_name: str
    age: int
    gender: str
    weight: int
    height: int
    average_score: float


@dataclass()
class Group:
    name: str
    students: list[Student]


class IFakerStudentData(ABC):
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


class IFakerGroupData(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


class IStudentCreator(ABC):
    def __init__(self, faker_student_data: IFakerStudentData):
        self.faker_student_data = faker_student_data

    @abstractmethod
    def create_student(self) -> Student:
        pass


class IGroupCreator(ABC):
    def __init__(self, faker_group_data: IFakerGroupData, students: list[Student]):
        self.faker_group_data = faker_group_data
        self.students = students

    @abstractmethod
    def create_group(self) -> Group:
        pass
