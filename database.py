from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
db_url = 'sqlite:///your_database_name.db'  # Replace 'your_database_name' with your desired database name

# Create the engine
engine = create_engine(db_url)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session
session = Session()
