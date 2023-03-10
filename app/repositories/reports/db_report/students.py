from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.repositories.reports.db_report.base_class import Base


class DBStudent(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]
    gender: Mapped[str] = mapped_column(String(1))
    weight: Mapped[int]
    height: Mapped[int]
    average_score: Mapped[float]
    group: Mapped[int] = mapped_column(Integer, ForeignKey("group.id"))

    def __repr__(self):
        return (
            f"Студент {self.full_name}: возраст {self.age}, пол {self.gender}, вес {self.weight}, "
            f"рост {self.height}, средний балл{self.average_score}."
        )
