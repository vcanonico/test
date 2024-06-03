from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float
from .base import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    income: Mapped[float] = mapped_column(Float)
    avg_idle_money: Mapped[float] = mapped_column(Float)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age}, income={self.income}, avg_idle_money={self.avg_idle_money})>"
