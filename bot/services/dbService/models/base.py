from peewee import PostgresqlDatabase, Model, SqliteDatabase

from bot.config import DATABASE_USER, DATABASE_HOST, DATABASE_NAME, DATABASE_PORT, DATABASE_PASSWORD

"""
db = PostgresqlDatabase(
    database=DATABASE_NAME,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT
)
"""

db = SqliteDatabase("../bot_data.db")


class BaseModel(Model):
    class Meta:
        database = db
