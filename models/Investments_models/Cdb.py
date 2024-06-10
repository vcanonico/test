from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .Base_investment import BaseInvestment

class CDB(BaseInvestment):
    __tablename__ = 'cdb'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    expiration_date: Mapped[DateTime] = mapped_column(DateTime)  # Expiration date of the investment
    currency: Mapped[str] = mapped_column(String)
    investment_id: Mapped[int] = mapped_column(Integer, ForeignKey('investments.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'cdb'
    }

    def __repr__(self):
        return (f"<CDB(id={self.id}, profit_rate={self.profit_rate}, profit_rate_measure={self.profit_rate_measure}, "
            f"profit_type={self.profit_type}, min_investment={self.min_investment}, min_movement={self.min_movement}, "
            f"liquidity_days={self.liquidity_days}, estimated_risk={self.estimated_risk}, type={self.type}, "
            f"expiration_date={self.expiration_date}, currency={self.currency})>, uid={self.uid}>")
