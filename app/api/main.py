from faker import Faker
from flask import Flask, jsonify, request

from config import GROUPS_COUNT, STUDENTS_IN_GROUP_COUNT, TYPE_REPORT
from domain.create_group_student import FakeGroupData, FakeStudentData, Group, GroupCreator, StudentCreator
from domain.create_subject_time_table import TimeTableCreator
from domain.group_builder import GroupsBuilder
from domain.interfaces import IReportGetter
from repositories.reports.types import REPORT_TYPES

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/report")
def main(gc: int = GROUPS_COUNT, sc: int = STUDENTS_IN_GROUP_COUNT, rtype: str = TYPE_REPORT) -> jsonify:
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

    report: IReportGetter = REPORT_TYPES[rtype](groups)
    report.get_report()

    return jsonify({"message": "Отчет готов"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
