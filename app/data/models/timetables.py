from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.models.base_class import Base


class TimeTable(Base):
    __tablename__ = "timetables"

    id: Mapped[int] = mapped_column(primary_key=True)
    subject = relationship("Subject")
    group: Mapped[int] = mapped_column(Integer, ForeignKey("groups.id"))

    def __repr__(self):
        return f"Расписание номер {self.id}"
