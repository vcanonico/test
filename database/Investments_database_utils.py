from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from models.Investments_models.Base_investment import BaseInvestment
from database.Base_database_utils import *

def create_tables(engine):
    """Creates the database tables."""
    BaseInvestment.metadata.create_all(engine)
