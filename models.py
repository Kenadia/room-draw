from sqlalchemy import Column, Integer, String
from database import Base


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    hall = Column(String(60), unique=False)
    draw_number = Column(Integer, unique=False)
    room_number = Column(String(10), unique=False)
    year = Column(Integer, unique=False)

    def __init__(self, hall=None, draw_number=None, room_number=None, year=None):
        self.hall = hall
        self.draw_number = draw_number
        self.room_number = room_number
        self.year = year

    def __repr__(self):
        return '<Room: %r hall>' % (self.hall)
