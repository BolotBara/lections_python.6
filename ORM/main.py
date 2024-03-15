# ORM (Object-Relational Mapping)- технология програмирования, благодоря которой разработчики могут использовать язык програмирования для взаимодествия с реляционной базой данных(PostgresSQL, MySQL и тд). Вместо того чтобы писать сырые запросы (операторы SQL), вы будете писать код на языке прог. Это очень сильно ускоряет разработку приложений и бд, особенно на начальных этапах. 

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    database = 'orm_db',
    user = 'bolot',
    password = '1',
    host = 'localhost', # 127.0.0.1
    port = 5432
)

# a = db.connect()
# print(a)

























