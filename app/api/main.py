from faker import Faker
from flask import Flask, jsonify, request

from config import settings
from domain.create_group_student import FakeGroupData, FakeStudentData, Group, GroupCreator, StudentCreator
from domain.create_subject_time_table import TimeTableCreator
from domain.group_builder import GroupsBuilder
from domain.interfaces import IReportBuilder
from repositories.reports.types import REPORT_TYPES

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/report")
def main(
    gc: int = settings.app.groups_count,
    sc: int = settings.app.students_in_group_count,
    rtype: str = settings.app.type_report,
) -> jsonify:
    fake_student_data = FakeStudentData(faker=Faker("ru_RU"))
    fake_group_data = FakeGroupData(faker=Faker("ru_RU"))

    group_creator = GroupCreator(faker=fake_group_data)
    student_creator = StudentCreator(faker=fake_student_data)
    timetable_creator = TimeTableCreator()

    gc = request.args.get("gc", default=gc, type=int)
    sc = request.args.get("sc", default=sc, type=int)
    rtype = request.args.get("rtype", default=rtype, type=str)

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

    return jsonify({"message": "Отчет готов"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
