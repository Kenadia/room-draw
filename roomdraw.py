import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
dp = SQLAlchemy(app)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hall = db.Column(db.String(60), unique=False)
    room_number = db.Column(db.String(10), unique=False)
    draw_number = db.Column(db.Integer, unique=False)
    year = db.Column(db.Integer, unique=False)

    def __init__(self, hall, room_number, draw_number, year):
        self.hall = hall
        self.room_number = room_number
        self.draw_number = draw_number
        self.year

    def __repr__(self):
        return '<Room: %r hall>' % (self.hall)


@app.route('/')
def hello():
    return 'Hello World!'
