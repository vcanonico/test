from sqlalchemy import Column, String, Float, DateTime
from .Base_investment import BaseInvestment

class Tesouro(BaseInvestment):
    __tablename__ = 'tesouro'

    id: Column[str] = Column(String, primary_key=True)
    expiration_date: Column[DateTime] = Column(DateTime)
    
    __mapper_args__ = {
        'polymorphic_identity': 'tesouro'
    }
