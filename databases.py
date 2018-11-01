from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, Comes_with, Type_of_celebration, price):
	new_object = Product(
		name=name,
		Comes_with=Comes_with,
		Type_of_celebration=Type_of_celebration,
		price=price)
	session.add(new_object)
	session.commit()

def update_product(price, Comes_with):
	new_object=session.query(Product).filter_by(
		price=price).first()
	new_object.Comes_with=Comes_with
	session.commit()

def delete_product(name):
	session.query(Product).filter_by(
		name=name).delete()
	session.commit()

def get_product(id):
  pass
create_product("SUPER EYELASH GLUE", "2 pairs of lashes", "BROTHERS WEDDING", 300)
create_product("NORMAL EYELASH GLUE", "3 pairs of lashes", "UNCLES WEDDING", 400)
delete_product("SUPER EYELASH GLUE")
update_product(800, "10 EYELASHES")