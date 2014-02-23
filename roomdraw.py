import os
from collections import defaultdict
from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///roomdraw.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hall = db.Column(db.String(60), unique=False)
    room_number = db.Column(db.String(10), unique=False)
    draw_number = db.Column(db.Integer, unique=False)
    draw_order = db.Column(db.Integer, unique=False)
    year = db.Column(db.Integer, unique=False)

    def __init__(self, hall, room_number, draw_number, draw_order, year):
        self.hall = hall
        self.room_number = room_number
        self.draw_number = draw_number
        self.draw_order = draw_order
        self.year = year

    def __repr__(self):
        return '<Room: %r hall>' % (self.hall)


def doseBins(yolo):
    maxi = [max(x) for x in yolo]
    bignum = max(maxi)
    binsize = 10
    lsize = (bignum / binsize) + 1
    newlo = []
    for hall in yolo:
        dd = defaultdict(int)
        for r in hall:
            dd[r / binsize] += 1
        newlo.append([dd[x] for x in range(lsize)])
    return newlo


def getData(dorms):
    results = [map(lambda r: r.draw_order, Room.query.filter_by(hall=dorm[:4].upper()).all())
               for dorm in dorms]
    data = doseBins(results)
    return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/+<dorms>')
def histoDorm(dorms):
    data = getData(dorms.strip().split('+'))
    return render_template('dorm2.html', data=data)


if __name__ == "__main__":
    app.debug = True
    manager.run()
