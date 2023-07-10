from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models import Base, Entity, Character
from tabulate import tabulate

# ========== Database and Session Initialization ========== #

# Create and bind a session with metadata to database defined in config.py
# See config.py for connection types

engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

# ========== Database Initialization and Session Control Functions ========== #

def initialize_database():
    if has_changes_in_schema():
        prompt = input("Changes in the database schema have been detected. Do you want to refresh the database? (y/n): ")
        if prompt.lower() == 'y':
            refresh_database()
        else:
            define_table_names()
    else:
        define_table_names()

def define_table_names():
    metadata.reflect(bind=engine)
    metadata.reflect(views=True, bind=engine)  # Add this line to reflect views
    metadata.tables = {table.name.lower(): table for table in metadata.sorted_tables}

def has_changes_in_schema():
    inspector = inspect(engine)
    current_tables = set(inspector.get_table_names())
    defined_tables = set(metadata.tables.keys())
    return current_tables != defined_tables

def refresh_database():
    metadata.drop_all(engine)  # Drop existing tables
    metadata.create_all(engine)  # Create new tables

def close_session():
    session.close()

# ========== General Database Functions ========== #

# print_tables
# Prints all tables in tabular format to see the column structure of each table in the database.
def print_tables():
    inspector = inspect(engine)
    table_names = inspector.get_table_names()

    for table_name in table_names:
        print_table(table_name)

# print_table_structure
# Prints the structure of a given table in tabular format.
def print_table_structure(table_name):
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)

    column_data = [
        [column['name'], column['type'], column['nullable'], column['default']]
        for column in columns
    ]

    headers = ["Column Name", "Data Type", "Is Nullable", "Default Value"]

    print(f"\nTable Structure - {table_name}:")
    print(tabulate(column_data, headers=headers, tablefmt="fancy_grid"))

# print_table
# Prints the contents of a given table in tabular format.
def print_table(table_name):
    define_table_names()  # Add this line to reflect the updated table names
    table_name_lower = table_name.lower()
    if table_name_lower in metadata.tables:
        table = metadata.tables[table_name_lower]
        columns = table.columns.keys()
        rows = session.query(table).all()
        print(f"{table_name} Table:\n")
        print(tabulate([[getattr(row, column) for column in columns] for row in rows], headers=columns, tablefmt="fancy_grid"))
    else:
        print(f"Table '{table_name}' does not exist.")

# ========== Entity Class ========== #

def add_entity(entity):
    session.add(entity)
    session.commit()

def get_all_entities():
    return session.query(Entity).all()

def update_entity(entity):
    session.commit()

def delete_entity(entity):
    session.delete(entity)
    session.commit()

# ========== Character Class ========== #

def add_character(character):
    session.add(character)
    session.commit()

def get_all_characters():
    return session.query(Character).all()

def update_character(character):
    session.commit()

def delete_character(character):
    session.delete(character)
    session.commit()
