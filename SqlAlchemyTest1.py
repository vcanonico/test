"""
    Initializes a new instance of the Repository class.

    Args:
        logger: The logger object for logging.
        session: The session object for database operations.
        helper: The helper object for utility functions.
"""

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create an engine
engine = create_engine('sqlite:///cousinsForTest.db', echo=True)  # Echo will show SQL queries

# Define a base class
Base = declarative_base()

# Define your model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create tables
Base.metadata.create_all(engine)

# Create a session
session = sessionmaker(bind=engine)
'''
# Define the name of the user you want to delete
user_name_to_delete = 'Heitor'  # Replace with the name of the user you want to delete
with Session() as session:
    # Query the user by name
    user_to_delete = session.query(User).filter(User.name == user_name_to_delete).first()

    # Check if the user exists
    if user_to_delete:
        # Delete the user
        session.delete(user_to_delete)
        session.commit()
        print(f"User '{user_name_to_delete}' deleted successfully.")
    else:
        print(f"User '{user_name_to_delete}' not found.")
'''
# Create a list of new users
new_users = [
    User(name='Vinicius', age=22),
    User(name='Carlos', age=20),
    User(name='Vitor', age=24),
    User(name='Heitor', age=11),
    User(name='Caio', age=16)
]

# Populate the table with example rows within a with statement
with session() as session:
    # Add all new users in a single statement
    session.add_all(new_users)

    # Commit the transaction to save changes
    session.commit()

# Query users younger than 18 years
with session() as session:
    underage_users = session.query(User).filter(User.age < 18).all()
    print("Users younger than 18 years:")
    for user in underage_users:
        print(f"User: {user.name}, Age: {user.age}")

# Query users with at least 18 years
with session() as session:
    adult_users = session.query(User).filter(User.age >= 18).all()
    print("\nUsers with at least 18 years:")
    for user in adult_users:
        print(f"User: {user.name}, Age: {user.age}")
