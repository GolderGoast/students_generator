import typer
from app.config import GROUPS_COUNT, STUDENTS_IN_GROUP_COUNT, TYPE_REPORT
from faker import Faker

from app.domain.create_group_student import FakeGroupData, FakeStudentData, Group, GroupCreator, StudentCreator
from app.domain.create_subject_time_table import TimeTableCreator
from app.domain.group_builder import GroupsBuilder
from app.domain.report_creator import IReportGetter
from app.repositories.reports.db_report.db_report import DataBaseReport
from app.repositories.reports.json_report import JsonReport
from app.repositories.reports.pdf_report import PDFReport
from app.repositories.reports.xlsx_report import XLSXReport

REPORT_TYPES = {"xlsx": XLSXReport, "json": JsonReport, "pdf": PDFReport, "db": DataBaseReport}

app = typer.Typer()


@app.command()
def main(gc: int = GROUPS_COUNT, sc: int = STUDENTS_IN_GROUP_COUNT, rtype: str = TYPE_REPORT) -> None:
    fake_student_data = FakeStudentData(faker=Faker("ru_RU"))
    fake_group_data = FakeGroupData(faker=Faker("ru_RU"))

    group_creator = GroupCreator(faker=fake_group_data)
    student_creator = StudentCreator(faker=fake_student_data)
    timetable_creator = TimeTableCreator()

    builder = GroupsBuilder(
        group_creator=group_creator,
        student_creator=student_creator,
        groups_count=gc,
        students_count=sc,
        timetable_creator=timetable_creator,
    )
    groups: list[Group] = builder.run()

    report: IReportGetter = REPORT_TYPES[rtype](groups)
    report.get_report()


if __name__ == "__main__":
    app()
