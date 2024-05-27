from database.database_utils import initialize_engine, create_session, create_tables, add_users, query_underage_users, query_adult_users,update_user_age,delete_users
from models.user import User

engine = initialize_engine('sqlite:///cousinsForTest.db', echo=True)
Session = create_session(engine)
create_tables(engine)

new_users = [
    User(name='Vinicius', age=22),
    User(name='Carlos', age=20),
    User(name='Vitor', age=24),
    User(name='Heitor', age=11),
    User(name='Caio', age=16)
]

# popula a lista com usuarios exemplo caso nao ja existam
with Session() as session:
    add_users(session, new_users)

# filtra usuarios pela idade
with Session() as session:
    underage_users = query_underage_users(session)
    print("Usuarios com menos de 18 anos:")
    for user in underage_users:
        print(f"User: {user.name}, Age: {user.age}")

    adult_users = query_adult_users(session)
    print("\nUsuarios com pelo menos de 18 anos:")
    for user in adult_users:
        print(f"User: {user.name}, Age: {user.age}")

# deleta os usuarios da lista
usernames_to_delete = [user.name for user in new_users]
with Session() as session:
    delete_users(session, usernames_to_delete)