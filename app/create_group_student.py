from entities import IFakerStudentData, IFakerGroupData, IGroupCreator, IStudentCreator, Student, Group
from random import choice, uniform

from faker import Faker


class FakeStudentData(IFakerStudentData):
    def __init__(self, faker: Faker):
        self.faker = faker
        self.gender = choice(['М', 'Ж'])

    def get_fullname(self) -> str:
        if self.gender == 'М':
            return self.faker.name_male()
        return self.faker.name_female()

    def get_age(self) -> int:
        return self.faker.random_int(18, 26)

    def get_gender(self) -> str:
        return self.gender

    def get_height(self) -> int:
        return self.faker.random_int(150, 210)

    def get_weight(self) -> int:
        return self.faker.random_int(50, 120)

    def get_average_score(self) -> float:
        return round(uniform(3, 5), 2)


class FakeGroupDada(IFakerGroupData):
    def __init__(self, faker: Faker):
        self.faker = faker

    def get_name(self) -> str:
        return self.faker.company()


class StudentCreator(IStudentCreator):
    def create_student(self) -> Student:
        name = self.faker_student_data.get_fullname()
        age = self.faker_student_data.get_age()
        gender = self.faker_student_data.get_gender()
        height = self.faker_student_data.get_height()
        weight = self.faker_student_data.get_weight()
        average_score = self.faker_student_data.get_average_score()

        return Student(name, age, gender, weight, height, average_score)


class GroupCreator(IGroupCreator):
    def create_group(self) -> Group:
        name = self.faker_group_data.get_name()

        return Group(name, self.students)
