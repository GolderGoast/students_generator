from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.data.models.base_class import Base


class DBSubject(Base):
    __tablename__ = "subject"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    day: Mapped[str]
    time: Mapped[str]
    timetable: Mapped[int] = mapped_column(ForeignKey("timetable.id"))

    def __repr__(self):
        return f"Предмет {self.name}, день {self.day}, время{self.time}"
