from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

def clear_database(connection_url):
    engine = create_engine(connection_url, pool_pre_ping=True)
    metadata = MetaData(bind=engine, reflect=True)
    metadata.drop_all()

def create_database(connection_url, database_name):
    engine = create_engine(connection_url, pool_pre_ping=True)
    engine.execution_options(isolation_level="AUTOCOMMIT").execute("CREATE DATABASE {}".format(database_name))

def reset_database(connection_url):
    clear_database(connection_url)
    create_database(connection_url, "game")

def connect_to_database(connection_url):
    engine = create_engine(connection_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def get_classes(connection_url):
    engine = create_engine(connection_url, pool_pre_ping=True)
    metadata = MetaData(bind=engine, reflect=True)
    return metadata.tables.keys()

def print_relationships(connection_url):
    engine = create_engine(connection_url, pool_pre_ping=True)
    metadata = MetaData(bind=engine, reflect=True)
    for table in metadata.sorted_tables:
        print(table.name)
        for fk in table.foreign_keys:
            print("  |-->", fk.column.table.name)
