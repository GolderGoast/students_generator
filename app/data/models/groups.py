from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.models.base_class import Base


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    student = relationship("Student")
    timetable = relationship("TimeTable", uselist=False)

    def __repr__(self):
        return f"Группа {self.name}."
