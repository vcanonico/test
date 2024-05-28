from database.database_utils import (
    initialize_engine,
    create_session,
    create_tables,
    add_users,
    update_user_age,
    delete_users,
    query_users_ordered_by_age_split_by_18_years
)
from models.user import User

engine = initialize_engine('sqlite:///cousinsForTest.db', echo=True)
Session = create_session(engine)
create_tables(engine)

new_users = [
    User(name='Vinicius', age=22),
    User(name='Carlos', age=20),
    User(name='Vitor', age=24),
    User(name='Heitor', age=11),
    User(name='Caio', age=16),
]

# Adiciona usuarios
with Session() as session:
    add_users(session, new_users)
    session.commit()

# filtra usuarios pela idade, separando entre maiores e menores de 18 anos.
with Session() as session:
    underage_users, adult_users = query_users_ordered_by_age_split_by_18_years(session)

    print("Usuarios com menos de 18 anos (ordenados por idade):")
    for user in underage_users:
        print(f"User: {user.name}, Age: {user.age}")

    print("\nUsuarios com pelo menos 18 anos (ordenados por idade):")
    for user in adult_users:
        print(f"User: {user.name}, Age: {user.age}")


users_to_delete = [
    User(name='Vinicius', age=22),
    User(name='Carlos', age=20),
    User(name='Vitor', age=24),
    User(name='Heitor', age=11),
    User(name='Caio', age=16),
]
# Deleta usuarios escolhidos
with Session() as session:
    usernames_to_delete = [user.name for user in users_to_delete]
    delete_users(session, usernames_to_delete)
    session.commit()
