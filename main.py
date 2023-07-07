from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from schema import Base, Item, Container, Inventory, Player, items_association_table


engine = create_engine('sqlite:///game.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base.metadata.create_all(engine)

# Create entities
player = Player(
    character_name='John',
    player_name='John Player',
    player_stats={},
    player_level=1,
    player_experience=0,
    player_properties={}
)

inventory = Inventory(inventory_name='Backpack', inventory_capacity=10, inventory_value=0)

# Add the player to the inventory
item1 = Item(item_name='Sword', item_description='A powerful sword')
inventory.items.append(item1)

# Add the item to the container
item1.containers.append(inventory)

session.add_all([player, inventory, item1])
session.commit()

# Retrieve the player and their inventory
player = session.query(Player).first()
inventory = session.query(Inventory).first()

print("Player:")
print(player)

print("Inventory:")
print(inventory)
print("Items in Inventory:")
for item in inventory.items:
    print(item)
