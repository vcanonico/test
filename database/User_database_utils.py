from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from models import User
from Base_database_utils import *


def query_users_ordered_by_age_split_by_18_years(session):
    """Filters users by age, returning lists of users under and over 18, respectively."""
    stmt = select(User).order_by(User.age)
    users = session.execute(stmt).scalars().all()

    underage_users = [user for user in users if user.age < 18]
    adult_users = [user for user in users if user.age >= 18]

    return underage_users, adult_users

def recommend_investment_profile(user):
    """
    Recommends an investment profile based on the user's financial data.
    """
    if user.income < renda_minima_para_perfil_conservador or user.avg_idle_money < dinheiro_ocioso_minimo_para_perfil_conservador:
        return "Não há perfil de investimentos recomendado"
    elif user.income < renda_minima_para_perfil_misto or user.avg_idle_money < dinheiro_ocioso_minimo_para_perfil_misto:
        return "Recomendado perfil conservador com foco em tesouro e cdb"
    else:
        return "Recomendado carteira mista, contando com tesouro e cdbs, além de renda fixa e ações blue chips"

def query_users_by_income_and_idle_money(session, min_income, min_avg_idle_money):
    """Filters users by minimum income and average idle money."""
    return session.query(User).filter(
        User.income > min_income,
        User.avg_idle_money >= min_avg_idle_money
    ).all()

def add_users(session, users):
    """Adds users to the database."""
    for user in users:
        existing_user = session.query(User).filter(User.name == user.name).first()
        if not existing_user:
            session.add(user)
    session.commit()

def delete_users(session, usernames):
    """Deletes users from the database."""
    for username in usernames:
        user_to_delete = session.query(User).filter(User.name == username).first()
        if user_to_delete:
            session.delete(user_to_delete)
            print(f"Deleted user '{username}' from the database.")
        else:
            print(f"User '{username}' not found in the database.")
    session.commit()

def update_user_age(session, username, new_age):
    """Updates a user's age."""
    user = session.query(User).filter(User.name == username).first()
    if user:
        user.age = new_age
        session.commit()

def update_user_income(session, username, new_income):
    """Updates a user's income."""
    user = session.query(User).filter(User.name == username).first()
    if user:
        user.income = new_income
        session.commit()

def update_user_idle_money(session, username, new_idle_money):
    """Updates a user's average idle money."""
    user = session.query(User).filter(User.name == username).first()
    if user:
        user.avg_idle_money = new_idle_money
        session.commit()

def query_underage_users(session):
    """Filters users under 18 years old."""
    return session.query(User).filter(User.age < 18).all()

def query_adult_users(session):
    """Filters users 18 years and older."""
    return session.query(User).filter(User.age >= 18).all()
