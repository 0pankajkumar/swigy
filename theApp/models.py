from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from theApp import db


# appy = Flask(__name__)
# appy.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pankaj:1234@localhost:5432/pankaj"
# appy.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(appy)
# from sqlalchemy import create_engine, Column, String
# engine = create_engine('postgresql://postgres@localhost:Octa4core@@localhost:5432/pankaj')


class Bunch(db.Model):
	__tablename__ = 'shortkeys'
	idx = db.Column(db.Integer, primary_key=True)
	shortlink = db.Column(db.String(15), unique=True, nullable=False)
	longlink = db.Column(db.String(250), nullable=False)

	def __init__(self, shortlink, longlink):
		self.shortlink = shortlink
		self.longlink = longlink

	def __repr__(self):
		return f"Bunch({self.shortlink}, {self.longlink})"

