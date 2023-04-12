from flask import Flask, jsonify, request

from config import settings
from repositories.container import AppContainer

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/report")
def main() -> jsonify:
    gc = request.args.get("gc", default=settings.app.groups_count, type=int)
    sc = request.args.get("sc", default=settings.app.students_in_group_count, type=int)
    rtype = request.args.get("rtype", default=settings.app.type_report, type=str)

    container: AppContainer = AppContainer(gc=gc, sc=sc, rtype=rtype)
    report = container.create_report_builder()
    report.get_report()

    return jsonify({"message": "Отчет готов"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
