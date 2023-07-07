from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Character, Player, NPC, Container, Inventory, Storage, Item
from dbUtil import print_table_info, print_relationships, tabularize_table, print_table

# Define the database connection URL
db_url = 'sqlite:///your_database_name.db'  # Replace 'your_database_name' with your desired database name

# Create the database engine and session
engine = create_engine('sqlite:///game.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create the tables in the database
Character.metadata.create_all(engine)
Container.metadata.create_all(engine)
Item.metadata.create_all(engine)

# Create sample data
player = Player(player_name='John Doe', player_level=1)
npc = NPC(npc_name='NPC 1', npc_unit_type='Enemy')
inventory = Inventory(inventory_items=['Item 1', 'Item 2'], inventory_value=100)
storage = Storage(storage_type='Chest', storage_items=['Item 3', 'Item 4'], storage_capacity=10)
item1 = Item(item_name='Sword', item_description='A powerful sword')
item2 = Item(item_name='Potion', item_description='Restores health')

# Add the objects to the session
session.add(player)
session.add(npc)
session.add(inventory)
session.add(storage)
session.add(item1)
session.add(item2)
session.add(inventory)
session.add(storage)
session.commit()

# Print table information
print("Table information:")
print_table_info(Character)
print_table_info(Player)
print_table_info(NPC)
print_table_info(Item)

# Print relationships between tables
print("Relationships between tables:")
print_relationships(Player, NPC)
print_relationships(NPC, Character)
print_relationships(Player, Character)
print_relationships(Inventory, NPC)
print_relationships(NPC, Character)
print_relationships(Storage, Character)
print_relationships(Player, Item)
print_relationships(Container, Character)
print_relationships(Player, Inventory)

# Create example entries
player1 = Player(player_name='John', player_level=10)
player2 = Player(player_name='Alice', player_level=5)
npc1 = NPC(npc_name='Bob', npc_level=8)
npc2 = NPC(npc_name='Eve', npc_level=3)
item1 = Item(item_name='Sword', item_description='A powerful weapon')
item2 = Item(item_name='Potion', item_description='Restores health')
inventory = Inventory(inventory_items=['Item 1', 'Item 2'], inventory_value=100)
storage = Storage(storage_type='Chest', storage_items=['Item 3', 'Item 4'], storage_capacity=10)

# Add entries to the session
session.add_all([player1, player2, npc1, npc2, item1, item2])
session.commit()

# Query and print the characters
print("Characters:")
characters = session.query(Character).all()
for character in characters:
    print(character)

# Query and print the items
print("Items:")
items = session.query(Item).all()
for item in items:
    print(item)
    
# Print modified table after adding entries
print("Modified table after adding entries:")
print("Table:", Character.__tablename__)
tabular_data = tabularize_table(Character)
print_table(tabular_data)

print("Table:", Item.__tablename__)
tabular_data = tabularize_table(Item)
print_table(tabular_data)

print("Table:", Inventory.__tablename__)
tabular_data = tabularize_table(Inventory)
print_table(tabular_data)

print("Table:", Storage.__tablename__)
tabular_data = tabularize_table(Storage)
print_table(tabular_data)

# Drop the tables
Character.metadata.drop_all(engine)
Container.metadata.drop_all(engine)
Item.metadata.drop_all(engine)
