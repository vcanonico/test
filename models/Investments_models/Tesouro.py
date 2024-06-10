from sqlalchemy import DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .Base_investment import BaseInvestment

class Tesouro(BaseInvestment):
    __tablename__ = 'tesouro'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    expiration_date: Mapped[DateTime] = mapped_column(DateTime)
    investment_id: Mapped[int] = mapped_column(Integer, ForeignKey('investments.id'))


    __mapper_args__ = {
        'polymorphic_identity': 'tesouro'
    }
