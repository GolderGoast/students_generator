from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from data.models.base_class import Base


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    day: Mapped[str]
    time: Mapped[str]
    timetable: Mapped[int] = mapped_column(ForeignKey("timetables.id"))

    def __repr__(self):
        return f"Предмет {self.name}, день {self.day}, время{self.time}"
