from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.data.models.base_class import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(unique=True)
    age: Mapped[int]
    gender: Mapped[str] = mapped_column(String(1))
    weight: Mapped[int]
    height: Mapped[int]
    average_score: Mapped[float]
    group: Mapped[int] = mapped_column(Integer, ForeignKey("groups.id"))

    def __repr__(self):
        return (
            f"Студент {self.full_name}: возраст {self.age}, пол {self.gender}, вес {self.weight}, "
            f"рост {self.height}, средний балл{self.average_score}."
        )
