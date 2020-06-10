from theApp import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from shortner.shortner import shortner_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:Octa4core@@localhost:5432/pankaj'
db = SQLAlchemy(app)



app.register_blueprint(shortner_bp, url_prefix='/short')

'''
