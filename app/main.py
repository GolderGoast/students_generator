import typer
from faker import Faker
from flask import Flask, jsonify, request

from config import GROUPS_COUNT, STUDENTS_IN_GROUP_COUNT, TYPE_REPORT
from domain.create_group_student import FakeGroupData, FakeStudentData, Group, GroupCreator, StudentCreator
from domain.create_subject_time_table import TimeTableCreator
from domain.group_builder import GroupsBuilder
from domain.report_creator import IReportGetter
from repositories.reports.db_report import DataBaseReport
from repositories.reports.json_report import JsonReport
from repositories.reports.pdf_report import PDFReport
from repositories.reports.xlsx_report import XLSXReport

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

REPORT_TYPES = {"xlsx": XLSXReport, "json": JsonReport, "pdf": PDFReport, "db": DataBaseReport}

typer_app = typer.Typer()


@app.route("/report")
@typer_app.command()
def main(gc: int = GROUPS_COUNT, sc: int = STUDENTS_IN_GROUP_COUNT, rtype: str = TYPE_REPORT) -> jsonify:
    fake_student_data = FakeStudentData(faker=Faker("ru_RU"))
    fake_group_data = FakeGroupData(faker=Faker("ru_RU"))

    group_creator = GroupCreator(faker=fake_group_data)
    student_creator = StudentCreator(faker=fake_student_data)
    timetable_creator = TimeTableCreator()

    gc = int(request.args.get("gc")) if request.args.get("gc") else gc
    sc = int(request.args.get("sc")) if request.args.get("sc") else sc
    rtype = request.args.get("rtype") if request.args.get("rtype") else rtype

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
