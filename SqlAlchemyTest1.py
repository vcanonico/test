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


engine = create_engine('sqlite:///cousinsForTest.db', echo=True)

Base = declarative_base()

# Define modelo da tabela
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

new_users = [
    User(name='Vinicius', age=22),
    User(name='Carlos', age=20),
    User(name='Vitor', age=24),
    User(name='Heitor', age=11),
    User(name='Caio', age=16)
]

# atribui dados exemplo a tabela caso nao já existam.
with Session() as session:
    for new_user in new_users:
        existing_user = session.query(User).filter(User.name == new_user.name).first()
        if not existing_user:
            session.add(new_user)

    session.commit()

# filtra usuarios com base na idade 
with Session() as session:
    underage_users = session.query(User).filter(User.age < 18).all()
    print("Users younger than 18 years:")
    for user in underage_users:
        print(f"User: {user.name}, Age: {user.age}")

    adult_users = session.query(User).filter(User.age >= 18).all()
    print("\nUsers with at least 18 years:")
    for user in adult_users:
        print(f"User: {user.name}, Age: {user.age}")
