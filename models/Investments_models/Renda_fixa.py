from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .Base_investment import BaseInvestment

class RendaFixa(BaseInvestment):
    __tablename__ = 'renda_fixa'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    expiration_date: Mapped[DateTime] = mapped_column(DateTime)
    currency: Mapped[str] = mapped_column(String)
    investment_id: Mapped[int] = mapped_column(Integer, ForeignKey('investments.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'renda_fixa'
    }
