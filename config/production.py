from config.default import *
import psycopg2 


SQLALCHEMY_DATABASE_URI = 'postgresql://wxmedoqx:hihfM0QF3AtbKXRC8cOy_Nc5yVxrL_1j@arjuna.db.elephantsql.com/wxmedoqx'
host = 'arjuna.db.elephantsql.com'
user = 'wxmedoqx'
password = 'hihfM0QF3AtbKXRC8cOy_Nc5yVxrL_1j'
database = 'wxmedoqx'

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'K\x9e\x0c\x96\x9f\xd6\x92T\x91l\xb5X\x0f\xa3\x0e\xc7'