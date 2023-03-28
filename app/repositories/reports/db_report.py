from passlib.hash import pbkdf2_sha256
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DSN_DB
from app.data.models.groups import Group
from app.data.models.students import Student
from app.data.models.subjects import Subject
from app.data.models.timetables import TimeTable
from app.domain.entities import Group as GroupEntity
from app.domain.report_creator import IReportGetter


class DataBaseReport(IReportGetter):
    def __init__(self, groups: list[GroupEntity], report_path: str = "report", engine: str = DSN_DB):
        super().__init__(groups=groups, report_path=report_path)
        self.engine = create_engine(engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def get_report(self):
        for group in self.groups:
            group_for_db = Group(name=group.name)
            self.session.add(group_for_db)
            self.session.commit()

            for student in group.students:
                student_for_db = Student(
                    full_name=student.full_name,
                    email=student.email,
                    password=pbkdf2_sha256.hash(student.password),
                    age=student.age,
                    gender=student.gender,
                    weight=student.weight,
                    height=student.height,
                    average_score=student.average_score,
                    group=group_for_db.id,
                )
                self.session.add(student_for_db)

            timetable_for_db = TimeTable(group=group_for_db.id)
            self.session.add(timetable_for_db)
            self.session.commit()

            for subject in group.timetable.subjects:
                subj_for_db = Subject(
                    name=subject.name, day=subject.day_of_week, time=subject.time, timetable=timetable_for_db.id
                )
                self.session.add(subj_for_db)
            self.session.commit()
