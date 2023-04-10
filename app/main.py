import typer
from faker import Faker

from config import GROUPS_COUNT, STUDENTS_IN_GROUP_COUNT, TYPE_REPORT
from domain.create_group_student import FakeGroupData, FakeStudentData, Group, GroupCreator, StudentCreator
from domain.create_subject_time_table import TimeTableCreator
from domain.group_builder import GroupsBuilder
from domain.interfaces import IReportBuilder
from repositories.reports.types import REPORT_TYPES

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

    report: IReportBuilder = REPORT_TYPES[rtype](groups)
    report.get_report()


if __name__ == "__main__":
    app()
