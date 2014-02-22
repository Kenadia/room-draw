from roomdraw import db
from roomdraw import Room

data = open("data.csv").read()
lines = data.split("\r\n")[1:]

db.create_all()

for l in lines:
    room, term, draw = l.split(',')
    hall = room.split()[0]
    room_number = room.split()[1]
    draw_number = int(draw)
    year = int(term[:2]) + 2000
    x = Room(hall, room_number, draw_number, year)
    db.session.add(x)

db.session.commit()
