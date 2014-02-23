from roomdraw import db
from roomdraw import Room
from collections import defaultdict


if __name__ == '__main__':
    data = open("data.csv").read()
    lines = data.split("\r\n")[1:]
    rooms = defaultdict(list)
    for l in lines:
        room, term, draw = l.split(',')
        if draw:  # Davis 007
            hall = room.split()[0]
            room_number = room.split()[1]
            draw_number = int(draw)
            year = int(term[:2]) + 2000
            rooms[hall].append((hall, room_number, draw_number, year))
    rooms = {hall:sorted(rooms[hall], key=lambda x: x[1]) for hall in rooms}
    for hall in rooms:
        for i, r in enumerate(rooms[hall]):
            hall, room_number, draw_number, year = r
            x = Room(hall, room_number, draw_number, i + 1, year)
            db.session.add(x)
    db.session.commit()
