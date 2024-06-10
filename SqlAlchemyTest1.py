from database.database_utils import (
    initialize_engine,
    create_session,
    create_tables,
    add_users,
    update_user_age,
    delete_users,
    query_users_ordered_by_age_split_by_18_years,
    query_users_by_income_and_idle_money,
    recommend_investment_profile
)
from models.user import User

engine = initialize_engine('sqlite:///cousinsForTest.db', echo=True)
Session = create_session(engine)
create_tables(engine)

new_users = [
    User(name='Vinicius', age=22, income=4500.0, avg_idle_money=500.0),
    User(name='Carlos', age=20, income=200.0, avg_idle_money=50.0),
    User(name='Vitor', age=24, income=5000.0, avg_idle_money=2000.0),
    User(name='Heitor', age=11, income=0.0, avg_idle_money=0.0),
    User(name='Caio', age=16, income=0.0, avg_idle_money=0.0),
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

    
    min_income = 2000.0
    min_avg_idle_money = 500.0
    wealthy_users = query_users_by_income_and_idle_money(session, min_income, min_avg_idle_money)

    print(f"\nUsuarios com renda acima de {min_income} e pelo menos {min_avg_idle_money} de dinheiro ocioso médio:")
    for user in wealthy_users:
        investment_profile = recommend_investment_profile(user)
        print(f"User: {user.name}, Age: {user.age}, Income: {user.income}, Avg Idle Money: {user.avg_idle_money}")
        print(f"perfil recomendado: {investment_profile}")
        print("-" * 50)

users_to_delete = [
    User(name='Vinicius', age=22, income=4500.0, avg_idle_money=500.0),
    User(name='Carlos', age=20, income=200.0, avg_idle_money=50.0),
    User(name='Vitor', age=24, income=5000.0, avg_idle_money=2000.0),
    User(name='Heitor', age=11, income=0.0, avg_idle_money=0.0),
    User(name='Caio', age=16, income=0.0, avg_idle_money=0.0),
]
# Deleta usuarios escolhidos
with Session() as session:
    usernames_to_delete = [user.name for user in users_to_delete]
    delete_users(session, usernames_to_delete)
    session.commit()
