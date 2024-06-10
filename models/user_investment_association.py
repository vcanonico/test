from sqlalchemy import Table, Column, ForeignKey
from models.Base import Base

user_investment_association = Table(
    'user_investment_association',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('investment_id', ForeignKey('investments.id'), primary_key=True)
)
