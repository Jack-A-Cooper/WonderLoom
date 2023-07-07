from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#=========================================================================================================================================================================================#

#========================================================================   ENTITIES    ==================================================================================================#

#=========================================================================================================================================================================================#

class Entity(Base):
    __tablename__ = 'entity'
    entity_id = Column(Integer, primary_key=True, autoincrement=True)
    entity_name = Column(String, nullable=True)
    entity_type = Column(String, nullable=True)
    entity_race = Column(String, nullable=True)
    entity_stats = Column(JSON, nullable=True)
    entity_state = Column(Boolean, nullable=True)
    entity_location = Column(String, nullable=True)
    entity_properties = Column(JSON, nullable=True)

    def __str__(self):
        return f"Entity(id={self.entity_id}, entity_name={self.entity_name}, entity_type={self.entity_type}, entity_race={self.entity_race}, entity_stats={self.entity_stats}, entity_state={self.entity_state}, entity_location={self.entity_location}, entity_properties={self.entity_properties})"

class Character(Entity):
    __tablename__ = 'characters'
    character_id = Column(Integer, ForeignKey('entity.entity_id'), primary_key=True, autoincrement=True)
    character_name = Column(String, nullable=True)
    character_type = Column(String)
    character_race = Column(String)
    character_stats = Column(JSON, nullable=True)
    character_state = Column(Boolean, nullable=True)
    character_location = Column(String, nullable=True)
    character_properties = Column(JSON)

    def __str__(self):
        return f"Character(id={self.character_id}, character_name={self.character_name}, character_type={self.character_type}, character_race={self.character_race}, character_stats={self.character_stats}, character_state={self.character_state}, character_location={self.character_location}, character_properties={self.character_properties})"

class Player(Character):
    __tablename__ = 'players'
    player_id = Column(Integer, ForeignKey('characters.character_id'), primary_key=True, autoincrement=True)
    player_name = Column(String)
    player_stats = Column(JSON)
    player_level = Column(Integer)
    player_experience = Column(Integer)
    player_properties = Column(JSON)

    def __str__(self):
        return f"Player(player_id={self.player_id}, player_name={self.player_name}, player_stats={self.player_stats}, player_level={self.player_level}, player_experience={self.player_experience}, player_properties={self.player_properties})"

class NPC(Character):
    __tablename__ = 'npcs'
    npc_id = Column(Integer, ForeignKey('characters.character_id'), primary_key=True, autoincrement=True)
    npc_name = Column(String, nullable=True)
    npc_unit_name = Column(String)
    npc_unit_type = Column(String)
    npc_unit_affiliation = Column(String, nullable=True)
    npc_stats = Column(JSON, nullable=True)
    npc_level = Column(Integer, nullable=True)
    npc_experience = Column(Integer, nullable=True)
    npc_properties = Column(JSON, nullable=True)

    def __str__(self):
        return f"NPC(npc_id={self.npc_id}, npc_name={self.npc_name}, npc_unit_name={self.npc_unit_name}, npc_unit_type={self.npc_unit_type}, npc_unit_affiliation={self.npc_unit_affiliation}, npc_stats={self.npc_stats}, npc_level={self.npc_level}, npc_experience={self.npc_experience}, npc_properties={self.npc_properties})"

#=========================================================================================================================================================================================#

#======================================================================     STORAGE     ==================================================================================================#

#=========================================================================================================================================================================================#

class Container(Base):
    __tablename__ = 'containers'
    container_id = Column(Integer, ForeignKey('entity.entity_id'), primary_key=True, autoincrement=True)
    container_name = Column(String, nullable=True)
    container_location = Column(String, nullable=True)
    container_items = Column(JSON, nullable=True)
    container_value = Column(Integer, nullable=True)
    container_ownership = Column(Boolean)
    container_shared = Column(Boolean, nullable=True)
    container_properties = Column(JSON, nullable=True)

    def __str__(self):
        return f"Container(container_id={self.container_id}, container_name={self.container_name}, container_location={self.container_location} container_items={self.container_items}, container_value={self.container_value}, container_ownership={self.container_ownership}, container_shared={self.container_shared}, container_properties={self.container_properties})"

class Inventory(Container):
    __tablename__ = 'inventories'
    inventory_id = Column(Integer, ForeignKey('containers.container_id'), ForeignKey('characters.character_id'), primary_key=True, autoincrement=True)
    inventory_name = Column(String, nullable=True)
    inventory_items = Column(JSON)
    inventory_value = Column(Integer, nullable=True)
    inventory_capacity = Column(Integer, nullable=True)
    inventory_properties = Column(JSON, nullable=True)

    def __str__(self):
        return f"Inventory(inventory_id={self.inventory_id}, inventory_name={self.inventory_name}, inventory_items={self.inventory_items}, inventory_value={self.inventory_value},inventory_capacity={self.inventory_capacity}, inventory_properties={self.inventory_properties})"

class Storage(Container):
    __tablename__ = 'storages'
    storage_id = Column(Integer, ForeignKey('containers.container_id'), ForeignKey('characters.character_id'), primary_key=True, autoincrement=True)
    storage_name = Column(String)
    storage_type = Column(String)
    storage_location = Column(String, nullable=True)
    storage_items = Column(JSON)
    storage_value = Column(Integer, nullable=True)
    storage_ownership = Column(Boolean, nullable=True)
    storage_shared = Column(Boolean, nullable=True)
    storage_capacity = Column(Integer, nullable=True)
    storage_properties = Column(JSON, nullable=True)

    def __str__(self):
        return f"Storage(storage_id={self.storage_id}, storage_name={self.storage_name}, storage_type={self.storage_type},storage_location={self.storage_location}, storage_items={self.storage_items}, storage_value={self.storage_value}, storage_ownership={self.storage_ownership}, storage_capacity={self.storage_capacity}, storage_properties={self.storage_properties})"
        
#=========================================================================================================================================================================================#

#======================================================================    MECHANICS    ==================================================================================================#

#=========================================================================================================================================================================================#


#=========================================================================================================================================================================================#

#======================================================================    GAME WORLD    =================================================================================================#

#=========================================================================================================================================================================================#

class Item(Base):
    __tablename__ = 'items'
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    item_name = Column(String)
    item_description = Column(Text)
    item_value = Column(Integer, nullable=True)
    item_weight = Column(Integer, nullable=True)
    item_properties = Column(JSON)
    is_quest_item = Column(Boolean, nullable=True)

    def __str__(self):
        return f"Item(item_id={self.item_id}, item_name={self.item_name}, item_description={self.item_description}, item_value={self.item_value}, item_weight={self.item_weight}, item_properties={self.item_properties})"
