import sys
import sqlalchemy
import json

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, backref, sessionmaker

from sqlalchemy import create_engine

from db_orm import Base, Restaurant, MenuItem

def InitializeDB():
    data = open("restaurant.json")
    json_data = json.load(data)

    for r in json_data["restaurants"]:
        r_entry = Restaurant(name = r["name"])
        for item in r["menuitems"]:
            i = MenuItem(restaurant = r_entry)
            i.name = item["name"]
            i.price = float(item["price"])
            i.description = item["description"]
            # i.restaurant_id = r_entry.id
            session.add(i)
        session.add(r_entry)
        session.commit()

if __name__ == "__main__" :
    engine = create_engine('sqlite:///restaurant.db')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    InitializeDB()
