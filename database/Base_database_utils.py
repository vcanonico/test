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

def add_entries_if_not_exists(session, model_class, entries, uid_column):
    """
    Adds entries to the database if an identical entry does not already exist based on a unique identifier column.
    
    :param session: SQLAlchemy session object
    :param model_class: SQLAlchemy model class
    :param entries: List of entries to be added, each entry being an instance of model_class
    :param uid_column: The unique identifier column to check for existing entries
    """
    for entry in entries:
        # Get the unique identifier value of the entry
        uid_value = getattr(entry, uid_column)
        
        # Check if an entry with the same unique identifier already exists
        existing_entry = session.query(model_class).filter_by(**{uid_column: uid_value}).first()
        
        if existing_entry:
            print(f"Existing entry found: {entry}")
        else:
            # No existing entry found, adding entry to the session
            session.add(entry)
            print(f"Adding new entry: {entry}")

    session.commit()


def delete_entries_if_exists(session, model_class, entries, uid_column):
    """
    Deletes entries from the database if an identical entry exists.
    
    :param session: SQLAlchemy session object
    :param model_class: SQLAlchemy model class
    :param entries: List of entries to be deleted, each entry being an instance of model_class
    :param uid_column: Name of the column to be used as the unique identifier
    """
    for entry in entries:
        # Get the column value of the unique identifier
        uid_value = getattr(entry, uid_column)
        
        # Check if an identical entry exists based on the unique identifier
        existing_entry = session.query(model_class).filter(getattr(model_class, uid_column) == uid_value).first()
        
        if existing_entry:
            session.delete(existing_entry)
    
    session.commit()