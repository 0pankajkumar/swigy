import os


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'SECRET_KEY'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgresql://pankaj:1234@localhost:5432/pankaj'