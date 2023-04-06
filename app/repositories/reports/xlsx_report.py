from openpyxl.workbook import Workbook

from domain.interfaces import IReportGetter


class XLSXReport(IReportGetter):
    def get_report(self) -> None:
        wb = Workbook()
        ws = wb.active
        wb.remove(ws)
        for group in self.groups:
            ws = wb.create_sheet(f"Группа {group.name}")
            ws.append(
                [
                    "ФИО",
                    "Электронная почта",
                    "Возраст",
                    "Пол",
                    "Вес",
                    "Рост",
                    "Средний балл",
                ]
            )
            for student in group.students:
                ws.append(list(vars(student).values()))

        wb.save(f"{self.report_path}.xlsx")
