from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
from models import Base

# Constantes para recomendaçao de investment profile
renda_minima_para_perfil_conservador = 2000
dinheiro_ocioso_minimo_para_perfil_conservador = 500
renda_minima_para_perfil_misto = 5000
dinheiro_ocioso_minimo_para_perfil_misto = 1500

def initialize_engine(database_url, echo=False):
    """Initializes the engine."""
    return create_engine(database_url, echo=echo)

def create_session(engine):
    """Creates the session factory."""
    return sessionmaker(bind=engine)

def create_tables(engine):
    """Creates the database tables."""
    Base.metadata.create_all(engine)

def print_all_entries(session, model_class):
    entries = session.query(model_class).all()
    for entry in entries:
        print(entry)

def add_entries_if_not_exists(session, model_class, entries):
    """
    Adds entries to the database if an identical entry does not already exist. nao funciona por enquanto
    
    :param session: SQLAlchemy session object
    :param model_class: SQLAlchemy model class
    :param entries: List of entries to be added, each entry being an instance of model_class
    """
    for entry in entries:
        # Get the column names and values of the entry
        entry_attrs = {attr.key: getattr(entry, attr.key) for attr in inspect(entry).mapper.column_attrs if not attr.columns[0].primary_key}
        
        # Build the filter criteria dynamically
        filter_criteria = [getattr(model_class, attr) == value for attr, value in entry_attrs.items()]
        
        # Check if an identical entry already exists
        existing_entry = session.query(model_class).filter(*filter_criteria).first()
        
        if existing_entry:
            print(f"Existing entry found: {entry}")
        else:
            # No existing entry found, adding entry to the session
            session.add(entry)
            print(f"Adding new entry: {entry}")

    session.commit()


def delete_entries_if_exists(session, model_class, entries):
    """
    Deletes entries from the database if an identical entry exists.
    
    :param session: SQLAlchemy session object
    :param model_class: SQLAlchemy model class
    :param entries: List of entries to be deleted, each entry being an instance of model_class
    """
    for entry in entries:
        # Get the column names and values of the entry
        entry_attrs = {attr.key: getattr(entry, attr.key) for attr in inspect(entry).mapper.column_attrs}
        
        # Build the filter criteria dynamically
        filter_criteria = [getattr(model_class, attr) == value for attr, value in entry_attrs.items()]
        
        # Check if an identical entry exists
        existing_entry = session.query(model_class).filter(*filter_criteria).first()
        
        if existing_entry:
            session.delete(existing_entry)
    
    session.commit()
