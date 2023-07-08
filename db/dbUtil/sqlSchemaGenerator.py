from sqlalchemy import create_engine, MetaData
from schema import Base

# Create an engine and connect to the database
engine = create_engine('sqlite:///game.db')

# Create the metadata object
metadata = MetaData()

# Generate the SQL statements
sql_file_path = 'schema.sql'  # Path to the output SQL file
sql_file = open(sql_file_path, 'w')
sql_file.write('')
sql_file.close()

# Create the tables in the database and generate the SQL file
Base.metadata.create_all(engine, checkfirst=False)