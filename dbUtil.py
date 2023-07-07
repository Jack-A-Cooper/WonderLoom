from sqlalchemy import inspect
from tabulate import tabulate

def tabularize_table(table):
    columns = table.__table__.columns.keys()
    rows = [[column] for column in columns]
    return rows

def print_table(tabular_data):
    headers = tabular_data[0]
    rows = tabular_data[1:]

    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

def print_table_info(table):
    columns = table.__table__.columns.keys()
    tabular_data = [["Table:", table.__tablename__], ["Columns:"] + list(columns)]
    print_table(tabular_data)
    print()

def print_relationships(table1, table2):
    relationships = []

    for column in table1.__table__.columns:
        foreign_keys = column.foreign_keys

        for fk in foreign_keys:
            if fk.references(table2.__table__):
                relationships.append(column.name)

    if relationships:
        print(f"Table '{table1.__tablename__}' has a relationship with table '{table2.__tablename__}'.")
        for relationship in relationships:
            print(f"Relationship: {relationship}")
    else:
        print(f"No relationship found between table '{table1.__tablename__}' and table '{table2.__tablename__}'.")
    print("\n")

