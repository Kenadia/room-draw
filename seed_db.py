from roomdraw import db
from roomdraw import Room
from collections import defaultdict


if __name__ == '__main__':
    data = open("data.csv").read()
    lines = data.split("\n")[1:]
    rooms = defaultdict(list)
    for l in lines:
        room, term, draw = l.strip().split(',')
        if draw:  # Davis 007
            hall = room.split()[0]
            room_number = room.split()[1]
            draw_number = int(draw)
            year = int(term[:2]) + 2000
            rooms[year].append((hall, room_number, draw_number, year))
    rooms = {year: sorted(rooms[year], key=lambda x: x[1]) for year in rooms}
    for year in rooms:
        for i, r in enumerate(rooms[year]):
            hall, room_number, draw_number, year = r
            x = Room(hall, room_number, draw_number, i + 1, year)
            db.session.add(x)
    db.session.commit()
