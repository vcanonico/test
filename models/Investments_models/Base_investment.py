# models/base_investment.py
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from ..Base import Base

class BaseInvestment(Base):
    __tablename__ = 'investments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    profit_rate: Mapped[float] = mapped_column(Float, nullable=False)
    profit_rate_measure: Mapped[String] = mapped_column(String, nullable=False)
    profit_type: Mapped[str] = mapped_column(String(50), nullable=False)
    min_investment: Mapped[float] = mapped_column(Float, nullable=False)
    min_movement: Mapped[float] = mapped_column(Float, nullable=False)
    liquidity_days: Mapped[int] = mapped_column(Integer, nullable=False)
    estimated_risk: Mapped[str] = mapped_column(String(50), nullable=False)
    uid: Mapped[str] = mapped_column(String(50), nullable=False)


    # Discriminator column to differentiate between investment types
    type: Mapped[str] = mapped_column(String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'base_investment',
        'polymorphic_on': type
    }
