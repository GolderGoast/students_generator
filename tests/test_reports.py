from dataclasses import dataclass

from openpyxl import load_workbook

from app.report_creator import XLSXReport


@dataclass()
class MockStudent:
    full_name: str = 'John'
    age: int = 20
    gender: str = 'M'
    weight: int = 90
    height: int = 180
    average_score: float = 3.5


@dataclass()
class MockGroup:
    students: list[MockStudent]
    name: str = 'MyGroup'


mock_groups = [
               MockGroup([MockStudent(), MockStudent(), MockStudent()]),
               MockGroup([MockStudent(), MockStudent(), MockStudent()])
]


def test_xlsx_report(tmpdir):
    file_path = tmpdir.join('report')

    getter = XLSXReport(mock_groups, file_path)
    getter.get_report()

    wb = load_workbook(f'{file_path}.xlsx')
    assert wb.sheetnames == ['Группа MyGroup', 'Группа MyGroup1']
    assert len(list(wb.active)) == 4

    for sheet in wb.worksheets:
        for row in list(sheet)[1:]:
            assert [cell.value for cell in row] == ['John', 20, 'M', 90, 180, 3.5]
