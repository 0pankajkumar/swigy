import os


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'hjxzavyu1tee98829sh21h8h1uh1h1wh1'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = 'postgresql://pankaj:1234@localhost:5432/pankaj'