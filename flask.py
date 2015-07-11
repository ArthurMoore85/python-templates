from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy # Remove if not using

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # Example SQLAlchemy

db = SQLAlchemy(app) # Example SQLAlchemy connection
from models import * # If using SQLAlchemy


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
