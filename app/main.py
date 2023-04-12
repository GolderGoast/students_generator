import typer

from config import settings
from repositories.container import AppContainer

app = typer.Typer()


@app.command()
def main(
    gc: int = settings.app.groups_count,
    sc: int = settings.app.students_in_group_count,
    rtype: str = settings.app.type_report,
) -> None:
    container: AppContainer = AppContainer(gc=gc, sc=sc, rtype=rtype)
    report = container.create_report_builder()
    report.get_report()


if __name__ == "__main__":
    app()
