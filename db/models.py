from peewee import PrimaryKeyField, CharField, TextField, Model
from .databse import db

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = "id"

class User(BaseModel):
    name = CharField()
    avatar = TextField()

    class Meta:
        db_table = "users"

class Anime(BaseModel):
    title = TextField()
    description = TextField()

    class Meta:
        db_table = "anime"
