from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurant.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

@app.route('/')
@app.route('/hello')

def HelloWorld():
    restaurant = session.query(Restaurant).first()
    menuitems = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output = ''
    for i in menuitems:
        output += i.name
        output += '</br>'
        output += i.price
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
