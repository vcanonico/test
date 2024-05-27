from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User  

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
