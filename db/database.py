from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models import Base, Character

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def initialize_database():
    Base.metadata.create_all(engine)

def add_character(Character):
    session.add(Character)
    session.commit()

def get_all_characters():
    return session.query(Character).all()

def update_character(Character):
    session.commit()

def delete_character(Character):
    session.delete(Character)
    session.commit()

def close_session():
    session.close()
