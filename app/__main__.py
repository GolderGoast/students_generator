from faker import Faker

from app.config import GROUPS_COUNT, STUDENTS_IN_GROUP_COUNT
from app.get_report import TypeReport
from create_group_student import StudentCreator, FakeStudentData, GroupCreator, FakeGroupDada

faker = Faker('ru_RU')

groups = []
for _ in range(GROUPS_COUNT):
    students = []
    for _ in range(STUDENTS_IN_GROUP_COUNT):
        students_creator = StudentCreator(FakeStudentData(faker))
        students.append(students_creator.create_student())

    group_creator = GroupCreator(FakeGroupDada(faker), students)
    groups.append(group_creator.create_group())


report_typer = TypeReport()
