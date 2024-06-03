from sqlalchemy import Column, String, Float, DateTime
from .Base_investment import BaseInvestment

class Derivativos(BaseInvestment):
    __tablename__ = 'derivatives'

    id: Column[str] = Column(String, primary_key=True)
    underlying_asset: Column[str] = Column(String)
    expiration_date: Column[DateTime] = Column(DateTime)

    __mapper_args__ = {
        'polymorphic_identity': 'derivatives'
    }
