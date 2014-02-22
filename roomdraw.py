import os
from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')


app = Flask(__name__, template_folder=tmpl_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
db = SQLAlchemy(app)


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
        self.year = year

    def __repr__(self):
        return '<Room: %r hall>' % (self.hall)


def getData(dorm, year):
    results = Room.query.filter_by(hall=dorm[:4].upper(), year=year).all()
    data = [{
        draw_number: room.draw_number,
        room_number: room.room_number
    } for room in results]
    return data


@app.route('/<dorm>')
def hello(dorm):
    data = getData(dorm, 2003)
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.debug = True
    app.run()
