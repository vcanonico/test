from sqlalchemy import Column, String, DateTime
from .Base_investment import BaseInvestment

class Commodities(BaseInvestment):
    __tablename__ = 'commodities'

    id: Column[str] = Column(String, primary_key=True)
    category: Column[str] = Column(String)
    expiration_date: Column[DateTime] = Column(DateTime)

    __mapper_args__ = {
        'polymorphic_identity': 'commodities'
    }
