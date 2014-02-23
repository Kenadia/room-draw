from roomdraw import db
from roomdraw import Room


if __name__ == '__main__':
    for r in Room.query.all():
        db.session.delete(r)
    db.session.commit()
