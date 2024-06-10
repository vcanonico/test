# main.py
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.Base import Base
from models.User_models.user import User
from models.Investments_models.Stocks import Stocks
from models.Investments_models.Cdb import CDB
from datetime import datetime
from database.User_database_utils import *

# Constants
DATABASE_URL = 'sqlite:///users.db'

def main():
    # Initialize the database engine
    engine = initialize_engine(DATABASE_URL, echo=True)
    
    # Create the database tables
    create_tables(engine)
    
    # Create a session
    Session = create_session(engine)
    with Session() as session:

        # Add some users
        users = [
            User(name='Alice', age=30, income=70000.0, avg_idle_money=15000.0),
            User(name='Bob', age=17, income=500.0, avg_idle_money=100.0),
            User(name='Charlie', age=45, income=120000.0, avg_idle_money=50000.0)
        ]
        add_users(session, users)
        
        # Query and print all users
        print("All users:")
        print_all_entries(session, User)
        
        # Query and print underage users
        underage_users = query_underage_users(session)
        print("Underage users:")
        for user in underage_users:
            print(user)
        
        # Query and print adult users
        adult_users = query_adult_users(session)
        print("Adult users:")
        for user in adult_users:
            print(user)
        
        # Update a user's age
        update_user_age(session, 'Bob', 18)
        
        # Update a user's income
        update_user_income(session, 'Alice', 75000.0)
        
        # Update a user's idle money
        update_user_idle_money(session, 'Charlie', 60000.0)
        
        # Query and print all users again to see the updates
        print("All users after updates:")
        print_all_entries(session, User)
        
        # Recommend investment profiles for all users
        print("Investment profile recommendations:")
        all_users = session.query(User).all()
        for user in all_users:
            recommendation = recommend_investment_profile(user)
            print(f"{user.name}: {recommendation}")
        
        # Delete a user
        delete_users(session, ['Alice'])
        
        # Query and print all users again to see the deletion
        print("All users after deletion:")
        print_all_entries(session, User)
        
        # Close the session
        session.close()

if __name__ == "__main__":
    main()
