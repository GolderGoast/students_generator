from faker import Faker
from flasgger import Swagger
from flask import Flask, jsonify, request

import config
from domain.create_group_student import FakeGroupData, FakeStudentData, Group, GroupCreator, StudentCreator
from domain.create_subject_time_table import TimeTableCreator
from domain.group_builder import GroupsBuilder
from domain.interfaces import IReportGetter
from repositories.reports.types import REPORT_TYPES

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

swagger = Swagger(app)


@app.get("/report/")
def create_report():
    """Создание отчета"""

    fake_student_data = FakeStudentData(faker=Faker("ru_RU"))
    fake_group_data = FakeGroupData(faker=Faker("ru_RU"))

    group_creator = GroupCreator(faker=fake_group_data)
    student_creator = StudentCreator(faker=fake_student_data)
    timetable_creator = TimeTableCreator()

    gc = request.args.get("gc", type=int, default=config.GROUPS_COUNT)
    sc = request.args.get("sc", type=int, default=config.STUDENTS_IN_GROUP_COUNT)
    rtype = request.args.get("rtype", type="str", default=config.TYPE_REPORT)

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
