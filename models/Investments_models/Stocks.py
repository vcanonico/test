# models/stocks.py
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .Base_investment import BaseInvestment

class Stocks(BaseInvestment):
    __tablename__ = 'stocks'
    __mapper_args__ = {
        'polymorphic_identity': 'stocks'
    }

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    stock_types: Mapped[str] = mapped_column(String)  # Types of stocks: "Blue_chip", "Normal", "Start_up", "Unicorn" etc.
    fund_name: Mapped[str] = mapped_column(String)
    stock_market: Mapped[str] = mapped_column(String)
    investment_id: Mapped[int] = mapped_column(Integer, ForeignKey('investments.id'))

    def __repr__(self):
        return (f"<Stocks(id={self.id}, profit_rate={self.profit_rate}, profit_rate_measure={self.profit_rate_measure}, "
                f"profit_type={self.profit_type}, min_investment={self.min_investment}, min_movement={self.min_movement}, "
                f"liquidity_days={self.liquidity_days}, estimated_risk={self.estimated_risk}, type={self.type}, "
                f"stock_types={self.stock_types}, fund_name={self.fund_name}, stock_market={self.stock_market})>")
