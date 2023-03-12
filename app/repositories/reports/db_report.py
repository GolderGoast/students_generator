import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.data.models.base_class import Base
from app.data.models.groups import DBGroup
from app.data.models.students import DBStudent
from app.data.models.subjects import DBSubject
from app.data.models.timetables import DBTimeTable
from app.domain.entities import Group
from app.domain.report_creator import IReportGetter


class DataBaseReport(IReportGetter):
    def __init__(self, groups: list[Group], report_path: str = "report"):
        super().__init__(groups=groups, report_path=report_path)
        self.engine = create_engine(f"sqlite:///{self.report_path}.db")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def _create_db(self):
        Base.metadata.create_all(self.engine)

    def _clear_db(self):
        Base.metadata.drop_all(self.engine)

    def get_report(self):
        if os.path.exists(f"{self.report_path}.db"):
            self._clear_db()
            self._create_db()
        else:
            self._create_db()

        for group in self.groups:
            group_for_db = DBGroup(name=group.name)
            self.session.add(group_for_db)
            self.session.commit()

            for student in group.students:
                student_for_db = DBStudent(
                    full_name=student.full_name,
                    age=student.age,
                    gender=student.gender,
                    weight=student.weight,
                    height=student.height,
                    average_score=student.average_score,
                    group=group_for_db.id,
                )
                self.session.add(student_for_db)

            timetable_for_db = DBTimeTable(group=group_for_db.id)
            self.session.add(timetable_for_db)
            self.session.commit()

            for subject in group.timetable.subjects:
                subj_for_db = DBSubject(
                    name=subject.name, day=subject.day_of_week, time=subject.time, timetable=timetable_for_db.id
                )
                self.session.add(subj_for_db)
            self.session.commit()
