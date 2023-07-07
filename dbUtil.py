from sqlalchemy import inspect

    #Tabularizes the columns of a table.
def tabularize_table(table):
    columns = table.__table__.columns.keys()
    rows = [[column] for column in columns]
    return rows
	
    #Prints the tabular data in a formatted table.
def print_table(tabular_data):
    col_width = max(len(str(item)) for row in tabular_data for item in row) + 2
    for row in tabular_data:
        print("".join(str(item).ljust(col_width) for item in row))

    #Prints the table's name and columns in a tabular format.
def print_table_info(table):
    columns = table.__table__.columns.keys()
    tabular_data = [["Table:", table.__tablename__], ["Columns:"] + list(columns)]
    print_table(tabular_data)
    print()

    #Prints any relationships between two tables.
def print_relationships(table1, table2):
    inspector = inspect(table1)
    relationships = inspector.get_sorted_table_and_fkc_names()
    related_tables = set()
    for relationship in relationships:
        table_name, fk_name = relationship
        if table_name == table2.__tablename__:
            related_tables.add(table_name)
    if related_tables:
        print(f"Table '{table1.__tablename__}' has a relationship with table '{table2.__tablename__}'.")
    else:
        print(f"No relationship found between table '{table1.__tablename__}' and table '{table2.__tablename__}'.")
