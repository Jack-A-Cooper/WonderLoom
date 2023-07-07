from database import engine, session
from schema import MyTable1, MyTable2, Base
from dbUtil import print_table_info, print_relationships, tabularize_table, print_table

# Create the table
Base.metadata.create_all(engine)

# Print table information in a tabular format
print("Table information:")
print_table_info(MyTable1)
print_table_info(MyTable2)

# Print relationships between tables
print("Relationships between tables:")
print_relationships(MyTable1, MyTable2)

# Create five entries and add them to the session
entries1 = [
    MyTable1(id=1),
    MyTable1(id=2),
    MyTable1(id=3),
    MyTable1(id=4),
    MyTable1(id=5)
]

entries2 = [
    MyTable2(id=1),
    MyTable2(id=2),
    MyTable2(id=3),
    MyTable2(id=4),
    MyTable2(id=5)
]

print("Adding entries to the tables:")
print("Table:", MyTable1.__tablename__)
for entry in entries1:
    session.add(entry)
    print(f"Entry: {entry}")

print("Table:", MyTable2.__tablename__)
for entry in entries2:
    session.add(entry)
    print(f"Entry: {entry}")

session.commit()

# Print modified table after adding entries
print("Modified table after adding entries:")
print("Table:", MyTable1.__tablename__)
tabular_data = tabularize_table(MyTable1)
print_table(tabular_data)

print("Table:", MyTable2.__tablename__)
tabular_data = tabularize_table(MyTable2)
print_table(tabular_data)

# Drop the table
MyTable1.__table__.drop(engine)
MyTable2.__table__.drop(engine)
