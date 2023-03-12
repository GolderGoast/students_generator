from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.data.models.base_class import Base


class DBTimeTable(Base):
    __tablename__ = "timetable"

    id: Mapped[int] = mapped_column(primary_key=True)
    subject = relationship("DBSubject")
    group: Mapped[int] = mapped_column(Integer, ForeignKey("group.id"))

    def __repr__(self):
        return f"Расписание номер {self.id}"
