import json

from app.config import GROUPS_COUNT, STUDENTS_IN_GROUP_COUNT
from app.domain.report_creator import IReportGetter


class JsonReport(IReportGetter):
    @staticmethod
    def __add_num_if_key_in_dict(key: str, user_dict: dict, prefix: str, count: int) -> str:
        desired_key = f"{prefix} {key}"

        if desired_key in user_dict:
            for i in range(1, count):
                desired_key_with_num = f"{desired_key}{i}"
                if desired_key_with_num in user_dict:
                    continue
                return desired_key_with_num
        else:
            return desired_key

    def get_report(self) -> None:
        report = {}
        for group in self.groups:
            group_name = self.__add_num_if_key_in_dict(
                key=group.name, user_dict=report, prefix="Группа", count=GROUPS_COUNT
            )

            report[group_name] = {}
            for student in group.students:
                student_data = list(vars(student).values())[1:]

                student_name = self.__add_num_if_key_in_dict(
                    key=student.full_name, user_dict=report[group_name], prefix="Студент", count=STUDENTS_IN_GROUP_COUNT
                )

                report[group_name][student_name] = dict(
                    zip(
                        [
                            "Возраст",
                            "Пол",
                            "Вес",
                            "Рост",
                            "Средний балл",
                        ],
                        student_data,
                    )
                )
        with open(f"{self.report_path}.json", "w", encoding="utf8") as file:
            json.dump(report, file, indent=4, ensure_ascii=False)
