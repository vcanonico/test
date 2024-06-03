from sqlalchemy import Column, String, DateTime
from .Base_investment import BaseInvestment

class CDB(BaseInvestment):
    __tablename__ = 'cdb'

    id: Column[str] = Column(String, primary_key=True)
    expiration_date: Column[DateTime] = Column(DateTime)  # Expiration date of the investment
    currency: Column[str] = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'cdb'
    }
