from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Base import Base
from models.Investments_models.Stocks import Stocks
from models.Investments_models.Cdb import CDB
from datetime import datetime
from database.Investments_database_utils import *

# Initializa a engine
DATABASE_URL = "sqlite:///Investments.db"  
engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

example_stocks = [
    Stocks(
        profit_rate=5.0,
        profit_rate_measure="yearly",
        profit_type='Fixed',
        min_investment=1000.0,
        min_movement=100.0,
        liquidity_days=30,
        estimated_risk='Low',
        stock_types='Blue_chip',
        fund_name='Blue Chip Fund',
        stock_market='NYSE',
        uid='Blue Chip Fund'
    ),
    Stocks(
        profit_rate=7.0,
        profit_rate_measure="yearly",
        profit_type='Variable',
        min_investment=2000.0,
        min_movement=200.0,
        liquidity_days=60,
        estimated_risk='Medium',
        stock_types='Normal',
        fund_name='Growth Fund',
        stock_market='NASDAQ',
        uid='Growth Fund'
    ),
    Stocks(
        profit_rate=10.0,
        profit_rate_measure="yearly",
        profit_type='Variable',
        min_investment=5000.0,
        min_movement=500.0,
        liquidity_days=90,
        estimated_risk='High',
        stock_types='Start_up,Unicorn',
        fund_name='Tech Innovations Fund',
        stock_market='NYSE',
        uid='Tech Innovations Fund'
    )
]


# Example CDB records
example_cdbs = [
    CDB(
        profit_rate=14.5,
        profit_rate_measure="yearly",
        profit_type='Fixed',
        min_investment=5000.0,
        min_movement=500.0,
        liquidity_days=180,
        estimated_risk='Low',
        expiration_date=datetime(2025, 1, 1),
        currency='BRL',
        uid='CDB_001'
    ),
    CDB(
        profit_rate=6.0,
        profit_rate_measure="yearly",
        profit_type='Variable',
        min_investment=10000.0,
        min_movement=1000.0,
        liquidity_days=360,
        estimated_risk='Medium',
        expiration_date=datetime(2026, 6, 1),
        currency='USD',
        uid='CDB_002'
    ),
    CDB(
        profit_rate=8.0,
        profit_rate_measure="yearly",
        profit_type='Variable',
        min_investment=15000.0,
        min_movement=1500.0,
        liquidity_days=720,
        estimated_risk='High',
        expiration_date=datetime(2027, 12, 1),
        currency='EUR',
        uid='CDB_003'
    )
]

add_entries_if_not_exists(session, Stocks, example_stocks, 'uid')
add_entries_if_not_exists(session, CDB, example_cdbs, 'uid')

# Print all stocks
print("\nAll Stocks:")
print_all_entries(session, Stocks)

# Print all CDBs
print("\nAll CDBs:")
print_all_entries(session, CDB)

# Close the session
session.close()