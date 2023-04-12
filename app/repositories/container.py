from faker import Faker
from pydantic import BaseModel

from domain.create_group_student import FakeGroupData, FakeStudentData, GroupCreator, StudentCreator
from domain.create_subject_time_table import TimeTableCreator
from domain.entities import Group
from domain.group_builder import GroupsBuilder
from domain.interfaces import IReportBuilder
from repositories.reports.types import REPORT_TYPES


class AppContainer(BaseModel):
    gc: int
    sc: int
    rtype: str

    def create_report_builder(self) -> IReportBuilder:
        fake_student_data = FakeStudentData(faker=Faker("ru_RU"))
        fake_group_data = FakeGroupData(faker=Faker("ru_RU"))

        group_creator = GroupCreator(faker=fake_group_data)
        student_creator = StudentCreator(faker=fake_student_data)
        timetable_creator = TimeTableCreator()

        builder = GroupsBuilder(
            group_creator=group_creator,
            student_creator=student_creator,
            groups_count=self.gc,
            students_count=self.sc,
            timetable_creator=timetable_creator,
        )
        groups: list[Group] = builder.run()

        report: IReportBuilder = REPORT_TYPES[self.rtype](groups)

        return report
