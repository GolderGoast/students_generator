from random import choice, uniform

from faker import Faker

from domain.entities import (
    Gender,
    Group,
    IFakeGroupDataCreator,
    IFakeStudentDataCreator,
    IGroupCreator,
    IStudentCreator,
    Student,
    TimeTable,
)


class FakeStudentData(IFakeStudentDataCreator):
    def __init__(self, faker: Faker):
        self.faker = faker
        self.gender = Gender.MALE

    def get_fullname(self) -> str:
        self.gender = choice(list(Gender))

        if self.gender == Gender.MALE:
            return self.faker.name_male()
        return self.faker.name_female()

    def get_email(self) -> str:
        return self.faker.free_email()

    def get_password(self) -> str:
        return self.faker.password(length=12)

    def get_age(self) -> int:
        return self.faker.random_int(18, 25)

    def get_gender(self) -> str:
        if self.gender == Gender.MALE:
            return "М"
        return "Ж"

    def get_height(self) -> int:
        return self.faker.random_int(150, 210)

    def get_weight(self) -> int:
        return self.faker.random_int(50, 120)

    def get_average_score(self) -> float:
        return round(uniform(3, 5), 2)


class FakeGroupData(IFakeGroupDataCreator):
    def __init__(self, faker: Faker):
        self.faker = faker

    def get_name(self) -> str:
        return self.faker.company()


class StudentCreator(IStudentCreator):
    def run(self) -> Student:
        name = self.faker.get_fullname()
        email = self.faker.get_email()
        password = self.faker.get_password()
        age = self.faker.get_age()
        gender = self.faker.get_gender()
        height = self.faker.get_height()
        weight = self.faker.get_weight()
        average_score = self.faker.get_average_score()

        return Student(name, email, password, age, gender, weight, height, average_score)


class GroupCreator(IGroupCreator):
    def run(self, students: list[Student], timetable: TimeTable) -> Group:
        name = self.faker.get_name()

        return Group(name, students=students, timetable=timetable)
