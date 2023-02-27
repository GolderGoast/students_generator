import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint, choice, uniform

import typer
from faker import Faker
from openpyxl import Workbook

from config import (
    GROUPS_COUNT,
    STUDENTS_IN_GROUP_COUNT,
    TYPE_REPORT,
)


class UniversityGetterGroup(ABC):
    @abstractmethod
    def get_group(self):
        pass


class University(UniversityGetterGroup):
    def __init__(self):
        self.groups = []

    def create_groups(self, groups_count: int) -> None:
        for _ in range(groups_count):
            self.groups.append(Group())

    def get_group(self):
        for group in self.groups:
            yield group


class GroupGetterStudent(ABC):
    @abstractmethod
    def get_student(self):
        pass


class Group(GroupGetterStudent):
    def __init__(self):
        self.students = []

    def create_students(self, students_count: int) -> None:
        for _ in range(students_count):
            fake = Faker("ru_RU")
            gender = choice(
                (
                    "М",
                    "Ж",
                )
            )
            if gender == "М":
                fio = fake.name_male()
            else:
                fio = fake.name_female()
            age = randint(18, 25)
            weight = randint(60, 120)
            height = randint(150, 200)
            average_score = round(uniform(3, 5), 2)

            student = Student(
                fio=fio,
                age=age,
                gender=gender,
                weight=weight,
                height=height,
                average_score=average_score,
            )
            self.students.append(student)

    def get_student(self):
        for student in self.students:
            yield student


@dataclass()
class Student:
    fio: str
    age: int
    gender: str
    weight: int
    height: int
    average_score: float


class UniversityReportGetter(ABC):
    def __init__(self, group_getter):
        self.group_getter = group_getter

    @abstractmethod
    def get_report(self):
        pass


class XLSXReportGetter(UniversityReportGetter):
    def __init__(self, group_getter):
        super().__init__(group_getter=group_getter)

    def get_report(self) -> None:
        wb = Workbook()
        ws = wb.active
        wb.remove(ws)
        for num, group in enumerate(self.group_getter.get_group()):
            ws = wb.create_sheet(f"Группа_{num + 1}")
            ws.append(
                [
                    "ФИО",
                    "Возраст",
                    "Пол",
                    "Вес",
                    "Рост",
                    "Средний балл",
                ]
            )
            for student in group.get_student():
                ws.append(list(vars(student).values()))

        wb.save("report.xlsx")


class JsonReportGetter(UniversityReportGetter):
    def __init__(self, group_getter):
        super().__init__(group_getter=group_getter)

    def get_report(self) -> None:
        university = {}
        for g_num, group in enumerate(self.group_getter.get_group()):
            university[f"Group_{g_num + 1}"] = {}
            for s_num, student in enumerate(group.get_student()):
                student_data = list(vars(student).values())
                university[f"Group_{g_num + 1}"][f"Student_{s_num + 1}"] = dict(
                    zip(
                        [
                            "ФИО",
                            "Возраст",
                            "Пол",
                            "Вес",
                            "Рост",
                            "Средний балл",
                        ],
                        student_data,
                    )
                )
        with open("report.json", "w", encoding="utf8") as file:
            json.dump(university, file, indent=4)


app = typer.Typer()


@app.command()
def main(
    gc: int = GROUPS_COUNT,
    sc: int = STUDENTS_IN_GROUP_COUNT,
    rtype: str = TYPE_REPORT,
):
    university = University()
    university.create_groups(gc)
    for group in university.groups:
        group.create_students(sc)

    if rtype == "excel":
        report = XLSXReportGetter(group_getter=university)
        report.get_report()
    elif rtype == "json":
        report = JsonReportGetter(group_getter=university)
        report.get_report()
    else:
        print("Указан неверный формат отчета!")


if __name__ == "__main__":
    app()
