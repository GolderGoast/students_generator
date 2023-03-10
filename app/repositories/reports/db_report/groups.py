from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.repositories.reports.db_report.base_class import Base


class DBGroup(Base):
    __tablename__ = "group"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    student = relationship("DBStudent")
    timetable = relationship("DBTimeTable", uselist=False)

    def __repr__(self):
        return f"Группа {self.name}."
