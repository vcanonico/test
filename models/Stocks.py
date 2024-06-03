from sqlalchemy import Column, String, ARRAY
from .Base_investment import BaseInvestment

class Stocks(BaseInvestment):
    __tablename__ = 'stocks'

    id: Column[str] = Column(String, primary_key=True)
    stock_types: Column[ARRAY[str]] = Column(ARRAY(String))  # Types of stocks, "Blue_chip"/"Normal"/"Start_up"/"Unicorn"
    fund_name: Column[str] = Column(String)
    stock_market: Column[str] = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'stocks'
    }
