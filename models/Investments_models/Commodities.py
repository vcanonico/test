from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .Base_investment import BaseInvestment

class Commodities(BaseInvestment):
    __tablename__ = 'commodities'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(String)
    expiration_date: Mapped[DateTime] = mapped_column(DateTime)
    investment_id: Mapped[int] = mapped_column(Integer, ForeignKey('investments.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'commodities'
    }
