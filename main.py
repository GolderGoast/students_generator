import argparse
import json
from random import randint, choice, uniform

from faker import Faker
from openpyxl import Workbook

from config import GROUPS_COUNT, STUDENTS_IN_GROUP_COUNT, TYPE_REPORT


class University:
    def __init__(self):
        self.groups = []

    def create_groups(self, groups_count):
        for _ in range(groups_count):
            self.groups.append(Group())


class Group:
    def __init__(self):
        self.students = []

    def create_students(self, students_count):
        for _ in range(students_count):
            fake = Faker('ru_RU')
            gender = choice(('М', 'Ж',))
            if gender == 'М':
                fio = fake.name_male()
            else:
                fio = fake.name_female()
            age = randint(18, 25)
            weight = randint(60, 120)
            height = randint(150, 200)
            average_score = round(uniform(3, 5), 2)

            student = Student(fio=fio, age=age, gender=gender, weight=weight, height=height,
                              average_score=average_score)
            self.students.append(student)


class Student:
    def __init__(self, fio, age, gender, weight, height, average_score):
        self.fio = fio
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.average_score = average_score


class UniversityReportGetter:
    def __init__(self, university):
        self.university = university

    def get_report(self, report_type):
        if report_type == 'excel':
            self._get_xlsx_report()
        elif report_type == 'json':
            self.get_json_report()
        else:
            print('Указан неверный формат отчета!')

    def _get_xlsx_report(self):
        wb = Workbook()
        ws = wb.active
        wb.remove(ws)
        for num, group in enumerate(self.university.groups):
            ws = wb.create_sheet(f'Группа_{num + 1}')
            ws.append(['ФИО', 'Возраст', 'Пол', 'Вес', 'Рост', 'Средний балл'])
            for student in group.students:
                ws.append(list(vars(student).values()))

        wb.save('report.xlsx')

    def get_json_report(self):
        university = {}
        for g_num, group in enumerate(self.university.groups):
            university[f'Group_{g_num + 1}'] = {}
            for s_num, student in enumerate(group.students):
                student_data = list(vars(student).values())
                university[f'Group_{g_num + 1}'][f'Student_{s_num + 1}'] = dict(
                    zip(['ФИО', 'Возраст', 'Пол', 'Вес', 'Рост', 'Средний балл'], student_data))
        with open('report.json', 'w', encoding='utf8') as file:
            json.dump(university, file, indent=4)


def command_string_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-gc', default=GROUPS_COUNT)
    parser.add_argument('-sc', default=STUDENTS_IN_GROUP_COUNT)
    parser.add_argument('-type', default=TYPE_REPORT)
    args = vars(parser.parse_args())

    return args


def main():
    command_string_args = command_string_parser()

    university = University()
    university.create_groups(command_string_args['gc'])
    for group in university.groups:
        group.create_students(command_string_args['sc'])

    report_getter = UniversityReportGetter(university)
    report_getter.get_report(command_string_args['type'])


if __name__ == '__main__':
    main()
