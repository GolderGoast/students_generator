from create_group_student import StudentCreator, FakeStudentData

from faker import Faker

faker = Faker()

s_creator = StudentCreator(FakeStudentData(faker))

print(vars(s_creator.create_student()))
