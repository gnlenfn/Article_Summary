import psycopg2 


SQLALCHEMY_DATABASE_URI = '##'
host = '##'
user = '##'
password = '##'
database = '##'

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'dev'