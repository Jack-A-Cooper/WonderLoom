from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models import Base, User

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def initialize_database():
    Base.metadata.create_all(engine)

def add_user(user):
    session.add(user)
    session.commit()

def get_all_users():
    return session.query(User).all()

def update_user(user):
    session.commit()

def delete_user(user):
    session.delete(user)
    session.commit()

def close_session():
    session.close()
