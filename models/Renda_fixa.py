from sqlalchemy import Column, String, DateTime
from .Base_investment import BaseInvestment

class RendaFixa(BaseInvestment):
    __tablename__ = 'renda_fixa'

    id: Column[str] = Column(String, primary_key=True)
    expiration_date: Column[DateTime] = Column(DateTime)
    currency: Column[str] = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'renda_fixa'
    }
