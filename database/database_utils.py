from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models.user import User  

def query_users_ordered_by_age_split_by_18_years(session):
    """filtra usuarios pela idade, retornando listas com os menores e maiores de 18, respectivamente."""
    stmt = select(User).order_by(User.age)
    users = session.execute(stmt).scalars().all()

    underage_users = [user for user in users if user.age < 18]
    adult_users = [user for user in users if user.age >= 18]

    return underage_users, adult_users

def query_users_by_income_and_idle_money(session, min_income, min_avg_idle_money):
    """filtra usuarios com as quantidades minimas passadas"""
    return session.query(User).filter(
        User.income > min_income,
        User.avg_idle_money >= min_avg_idle_money
    ).all()

def initialize_engine(database_url, echo=False):
    """initializa a engine"""
    return create_engine(database_url, echo=echo)

def create_session(engine):
    """Cria a session factory."""
    return sessionmaker(bind=engine)

def create_tables(engine):
    """cria a tabela do banco de dados."""
    User.metadata.create_all(engine)

def add_users(session, users):
    """Adiciona usuarios ao banco de dados."""
    for user in users:
        existing_user = session.query(User).filter(User.name == user.name).first()
        if not existing_user:
            session.add(user)
    session.commit()

def delete_users(session, usernames):
    """Deleta usuarios do banco de dados."""
    for username in usernames:
        user_to_delete = session.query(User).filter(User.name == username).first()
        if user_to_delete:
            session.delete(user_to_delete)
            print(f"Deletado usuario '{username}' do banco de dados.")
        else:
            print(f"usuario '{username}' não encontrado no banco de dados.")
    session.commit()

def update_user_age(session, username, new_age):
    """atualiza a idade de um usuario"""
    user = session.query(User).filter(User.name == username).first()
    if user:
        user.age = new_age
        session.commit()

def query_underage_users(session):
    """filtra usuarios com menos de 18 anos"""
    return session.query(User).filter(User.age < 18).all()

def query_adult_users(session):
    """filtra usuarios com pelo menos 18 anos"""
    return session.query(User).filter(User.age >= 18).all()
