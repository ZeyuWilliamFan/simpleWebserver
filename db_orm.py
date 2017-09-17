import sqlalchemy

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class MenuItem(Base):
    __tablename__ = 'menuitem'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(String(8))
    course = Column(String(250))
    description = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(
        Restaurant, backref=backref('menuitems',
                                    uselist=True,
                                    cascade='delete,all'))

# engine = create_engine('sqlite:///restaurant.db')
# # Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
