from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from enum import Enum
from server import Base

class Listing(Base):
    __tablename__ = 'listings'
    id = Column('listing_id', Integer, primary_key=True)
    street_address = Column('street_address', String(250))
    city = Column('city', String(250))
    state = Column('state', String(2))
    zip = Column('zip', String(15))
    num_kids = Column('num_kids', Integer)   # TODO: add validation (can only be one or two)
    has_nanny = Column('has_nanny', String(50))
    time_frame = Column('time_frame', String(50))
    email = Column('email', String(250))
    age_group = Column('age_group', String(300))
    latitude = Column('latitude', Float)
    longitude = Column('longitude', Float)

    def __repr__(self):
        return str(self.id)

class AgeGroups(Enum):
    zero_to_six = '0 - 6 months'
    seven_to_eighteen = '7 - 18 months'
    nineteen_to_three = '18 months - 3 years'
    over_three = '3 years +'

class TimeFrame(Enum):
    next_thirty = 'next 30 days'
    thirty_to_sixty = '30-60 days'
    sixty_plus = '60 days +'
