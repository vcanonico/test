from database.database_utils import initialize_engine, create_session, create_tables
from models import Investment, SubInvestment

# Initialize the database
engine = initialize_engine('sqlite:///investments.db', echo=True)
create_tables(engine)
Session = create_session(engine)

# Add initial investments and sub-investments
with Session() as session:
    # Check if investments are already added
    if not session.query(Investment).first():
        # Add main investments
        investment_names = ["tesouro", "cdb", "renda_fixa", "ações", "commodities", "derivativos"]
        investments = [Investment(name=name) for name in investment_names]
        session.add_all(investments)
        session.commit()

        # Query investments to get their IDs
        acoes = session.query(Investment).filter_by(name="ações").first()

        # Add sub-investments for "ações"
        sub_investments = [
            SubInvestment(name="blue chips", investment_id=acoes.id),
            SubInvestment(name="normal", investment_id=acoes.id),
        ]
        session.add_all(sub_investments)
        session.commit()
