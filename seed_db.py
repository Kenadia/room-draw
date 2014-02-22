from roomdraw import db
from roomdraw import Room


if __name__ == '__main__':
    data = open("data.csv").read()
    lines = data.split("\r\n")[1:]
    for l in lines:
        room, term, draw = l.split(',')
        if draw:  # Davis 007
            hall = room.split()[0]
            room_number = room.split()[1]
            draw_number = int(draw)
            year = int(term[:2]) + 2000
            x = Room(hall, room_number, draw_number, year)
            db.session.add(x)
    db.session.commit()
