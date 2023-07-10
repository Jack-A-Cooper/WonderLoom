from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# ========== Entity Class (Base) ========== #

class Entity(Base):
    __tablename__ = 'entities'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(JSON)  # Name of the entity
    description = Column(String)  # Description of the entity
    relations = Column(JSON)  # Relationships or connections with other entities
    properties = Column(JSON)  # Custom properties or attributes specific to the entity
    entity_type = Column(String)  # Type of the entity

    __mapper_args__ = {
        'polymorphic_identity': 'entity',
        'polymorphic_on': entity_type
    }

# ========== Entity Class - Character ========== #

class Character(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    entity_id = Column(Integer, ForeignKey('entities.id'))
    name = Column(JSON)  # Name of the character - JSON so it may have titles, first/last name, and any prefix/suffix possible.
    description = Column(String)  # Description of the character
    inventory = Column(JSON)  # Inventory of the character
    equipment = Column(JSON)  # equipment of the character - the items the player is wielding, wearing, or otherwise using.
    relations = Column(JSON)  # Relationships or connections of the character
    statistics = Column(JSON)  # Statistics or attributes of the character
    properties = Column(JSON)  # Custom properties or attributes specific to the character
    type = Column(String) # Type or category of the character

    entity = relationship(Entity, backref='characters')