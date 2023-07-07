from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

#=========================================================================================================================================================================================#

#========================================================================   ENTITIES    ==================================================================================================#

#=========================================================================================================================================================================================#

class Entity(Base):
    __tablename__ = 'entities'
    id = Column(Integer, autoincrement=True, unique=True)
    description = Column(Test, nullable=True)
    properties = Column(JSON, nullable=True)

    def __str__(self):
        return f"Entity(id={self.id}, description={self.description},  properties={self.properties})"

class Item(Base):
    __tablename__ = 'items'
    id  = Column(Integer, autoincrement=True, unique=True)
    item_name = Column(String)
    item_description = Column(Text, nullable=True)
    item_value = Column(Integer, nullable=True)
    item_weight = Column(Integer, nullable=True)
    is_quest_item = Column(Boolean, nullable=True)
    stolen = Column(Boolean, nullable=True)
    item_properties = Column(JSON, nullable=True)
    
    container = relationship("Container", backref="items")

    def __str__(self):
        return f"Item(id={self.id}, item_name={self.item_name}, item_description={self.item_description}, item_value={self.item_value}, item_weight={self.item_weight}, is_quest_item={self.is_quest_item}, stolen={self.stolen}, item_properties={self.item_properties})"

class Container(Base):
    __tablename__ = 'containers'
    id = Column(Integer, autoincrement=True, unique=True)
    owner_id = Column(Integer, secondary_key=True, ForeignKey('characters.character_id'), nullable=True)
    items_id = Column(Integer, ForeignKey('items.item_id'), nullable=True)
    container_name = Column(String, nullable=True)
    container_location = Column(String, nullable=True)
    container_value = Column(Integer, nullable=True)
    container_ownership = Column(Boolean, nullable=True)
    container_shared = Column(Boolean, nullable=True)
    container_capacity = Column(Integer, nullable=True)
    container_properties = Column(JSON, nullable=True)
    
    # Relationship to Item
    items = relationship("Item", backref="container")

    def __str__(self):
        return f"Container(id={self.id}, object_id={self.object_id}, container_id={self.container_id}, owner_id={self.owner_id}, container_name={self.container_name}, container_location={self.container_location}, container_value={self.container_value}, container_ownership={self.container_ownership}, container_shared={self.container_shared}, container_capacity={self.container_capacity}, container_properties={self.container_properties})"

        
class Object(Base):
    __tablename__ = 'objects'
    id = Column(Integer, autoincrement=True, unique=True)
    description = Column(Test, nullable=True)
    properties = Column(JSON, nullable=True)

    def __str__(self):
        return f"Entity(id={self.id}, description={self.description},  properties={self.properties})"

#=========================================================================================================================================================================================#

#=======================================================================     PEOPLE      =================================================================================================#

#=========================================================================================================================================================================================#


class Character(Entity):
    __tablename__ = 'characters'
    id = Column(Integer, autoincrement=True, unique=True)
    character_id = Column(Integer, primary_key=True, ForeignKey('entity.entity_id'))
    inventory_id = Column(Integer, primary_key=True, ForeignKey('inventories.container_id'))
    type = Column(String)
    race = Column(String)
    stats = Column(JSON, nullable=True)
    properties = Column(JSON)

    def __str__(self):
        return f"Character(id={self.id}, character_id={self.character_id}, inventory_id={self.inventory_id}, type={self.type}, race={self.race}, stats={self.stats}, properties={self.character_properties})

class Player(Character):
    __tablename__ = 'players'
    id = Column(Integer, autoincrement=True, unique=True)
    character_id = Column(Integer, ForeignKey('characters.character_id'), unique=True)
    player_id = Column(Integer, primary_key=True, ForeignKey('players.player_id'), unique=True)
    inventory_id = Column(Integer, primary_key=True, ForeignKey('inventories.container_id'), unique=True)
    name = Column(String)
    player_title = Column(String, nullable=True)
    stats = Column(JSON)
    level = Column(Integer, nullable=True)
    experience = Column(Integer, nullable=True)
    player_properties = Column(JSON, nullable=True)

    def __str__(self):
        return f"Player(id={self.id}, character_id={self.character_id}, inventory_id={self.inventory_id}, player_id={self.player_id}, player_name={self.name}, stats={self.stats}, level={self.level}, experience={self.experience}, player_properties={self.player_properties})"

class NPC(Character):
    __tablename__ = 'npcs'
    id = Column(Integer, autoincrement=True, unique=True)
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    inventory_id = Column(Integer, primary_key=True, ForeignKey('inventories.container_id'))
    name = Column(String, nullable=True)
    unit_type_name = Column(String, nullable=True)
    unit_type = Column(String, nullable=True)
    unit_affiliation = Column(String, nullable=True)
    stats = Column(JSON)
    level = Column(Integer, nullable=True)
    experience = Column(Integer, nullable=True)
    properties = Column(JSON, nullable=True)

    def __str__(self):
        return f"NPC(id={self.id}, character_id={self.character_id}, inventory_id={self.inventory_id}, name={self.name}, unit_name={self.unit_name}, unit_type_name={self.unit_type_name}, unit_affiliation={self.unit_affiliation}, stats={self.stats}, level={self.level}, experience={self.experience}, properties={self.properties})"        

#=========================================================================================================================================================================================#

#======================================================================     WILDLIFE     =================================================================================================#

#=========================================================================================================================================================================================#

class Creature(Entity):
    __tablename__ = 'animals'
    id = Column(Integer, autoincrement=True, unique=True)
    creature_id = Column(Integer, primary_key=True, ForeignKey('entity.entity_id'))
    inventory_id = Column(Integer, primary_key=True, ForeignKey('inventories.container_id'), nullable=True)
    type = Column(String, nullable=True)
    stats = Column(JSON, nullable=True)
    properties = Column(JSON, nullable=True)

    def __str__(self):
        return f"Creature(id={self.id}, creature_id={self.creature_id}, inventory_id={self.inventory_id}, type={self.type}, stats={self.stats}, properties={self.properties})

#=========================================================================================================================================================================================#

#======================================================================     FACTIONS     =================================================================================================#

#=========================================================================================================================================================================================#

class Group(Entity):
    __tablename__ = 'groups'
    id = Column(Integer, autoincrement=True, unique=True)
    group_id = Column(Integer, primary_key=True, ForeignKey('entity.entity_id'), autoincrement=True)
    culture = Column(Boolean, nullable=True)
    interactable = Column(Boolean, nullable=True)
    unit_roster = Column(Boolean, nullable=True)
    faction = Column(Boolean, nullable=True)
    joinable = Column(Boolean, nullable=True)
    description = Column(Text, nullable=True)
    properties = Column(JSON, nullable=True)

    def __str__(self):
        return f"Entity(id={self.id}, group_id={self.group_id}, culture={self.culture}, interactable={self.interactable}, unit_roster={self.unit_roster}, faction={self.faction}, joinable={self.joinable}, description={self.description},  properties={self.properties})"

#=========================================================================================================================================================================================#

#======================================================================     STORAGE     ==================================================================================================#

#=========================================================================================================================================================================================#

class Inventory(Container):
    __tablename__ = 'inventories'
    id = Column(Integer, autoincrement=True, unique=True)
    container_id = Column(Integer, ForeignKey('containers.containers_id'), autoincrement=True, unique=True)
    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, secondary_key=True, ForeignKey('characters.character_id'), unique=True)
    inventory_name = Column(String, nullable=True)
    inventory_value = Column(Integer, nullable=True)
    inventory_capacity = Column(Integer, nullable=True)
    inventory_properties = Column(JSON, nullable=True)
    
    def __str__(self):
        return f"Inventory(id={self.id}, inventory_id={self.inventory_id}, owner_id={self.owner_id}, inventory_name={self.inventory_name}, inventory_value={self.inventory_value},inventory_capacity={self.inventory_capacity}, inventory_properties={self.inventory_properties})"

class Storage(Container):
    __tablename__ = 'storages'
    id = Column(Integer, autoincrement=True, unique=True)
    container_id = Column(Integer, ForeignKey('containers.container_id'))
    shared = Column(Boolean)
    owner_id = Column(Integer, ForeignKey('characters.character_id'))
    storage_name = Column(String, nullable=True)
    storage_type = Column(String, nullable=True)
    storage_location = Column(String, nullable=True)
    storage_value = Column(Integer, nullable=True)
    storage_ownership = Column(Boolean, nullable=True)
    storage_shared = Column(Boolean, nullable=True)
    storage_capacity = Column(Integer, nullable=True)
    storage_properties = Column(JSON, nullable=True)
    
    def __str__(self):
        return f"Storage(id={self.id}, container_id={self.container_id}, shared={self.shared}, owner_id={self.owner_id}, storage_name={self.storage_name}, storage_type={self.storage_type}, storage_location={self.storage_location}, storage_value={self.storage_value}, storage_ownership={self.storage_ownership}, storage_capacity={self.storage_capacity}, storage_properties={self.storage_properties})"

#=========================================================================================================================================================================================#

#======================================================================    MECHANICS    ==================================================================================================#

#=========================================================================================================================================================================================#


#=========================================================================================================================================================================================#

#======================================================================    GAME WORLD    =================================================================================================#

#=========================================================================================================================================================================================#