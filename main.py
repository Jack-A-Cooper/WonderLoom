from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, Entity, Item, Container, Character, Player

# Create the engine and bind it to the Base class
engine = create_engine('sqlite:///game.db')
Base.metadata.bind = engine

# Create the session
Session = sessionmaker(bind=engine)
session = Session()

# Create some entities
entity1 = Entity(description="Entity 1", properties={"color": "red"})
entity2 = Entity(description="Entity 2", properties={"color": "blue"})

# Create some items
item1 = Item(item_name="Sword", item_description="A powerful sword", item_value=100)
item2 = Item(item_name="Shield", item_description="A sturdy shield", item_value=50)

# Create a container
container = Container(owner_id=1, container_name="Chest", container_capacity=10)

# Create a character
character = Character(character_id=1, inventory_id=1, type="Warrior", race="Human", stats={"strength": 10})

# Create a player
player = Player(character_id=1, inventory_id=1, player_id=1, name="John", level=5)

# Add the entities, items, container, character, and player to the session
session.add_all([entity1, entity2, item1, item2, container, character, player])
session.commit()

# Query the entities
entities = session.query(Entity).all()
for entity in entities:
    print(entity)

# Query the items
items = session.query(Item).all()
for item in items:
    print(item)

# Query the container
container = session.query(Container).first()
print(container)

# Query the character
character = session.query(Character).first()
print(character)

# Query the player
player = session.query(Player).first()
print(player)
