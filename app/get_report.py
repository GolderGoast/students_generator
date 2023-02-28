import json
from abc import ABC, abstractmethod

from openpyxl.workbook import Workbook

from entities import Group
from config import TYPE_REPORT


class ITypeReport(ABC):
    @abstractmethod
    def get_type(self):
        pass


class IReportGetter(ABC):
    def __init__(self, groups: list[Group], report_typer: ITypeReport, report_path: str = 'report'):
        self.groups = groups
        self.report_type = report_typer.get_type()
        self.report_path = report_path

    @abstractmethod
    def get_report(self):
        pass


class TypeReport(ITypeReport):
    def __init__(self, report_type: str = TYPE_REPORT):
        self.report_type = report_type

    def get_type(self) -> str:
        return self.report_type


class XLSXReportGetter(IReportGetter):
    def get_report(self) -> None:
        wb = Workbook()
        ws = wb.active
        wb.remove(ws)
        for group in self.groups:
            ws = wb.create_sheet(f"Группа_{group.name}")
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
            for student in group.students:
                ws.append(list(vars(student).values()))

        wb.save(f'{self.report_path}.{self.report_type}')


class JsonReportGetter(IReportGetter):
    def get_report(self) -> None:
        university = {}
        for group in self.groups:
            university[f"Group_{group.name}"] = {}
            for student in group.students:
                student_data = list(vars(student).values())[1:]
                university[f"Group_{group.name}"][f"Student_{student.full_name}"] = dict(
                    zip(
                        [
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
