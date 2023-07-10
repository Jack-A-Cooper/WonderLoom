from models import Entity, Character
import database

# ========== Tests For Classes in Model.py ========== #

# ========== Test: Entity ========== #

def test_entity():
    print("========== Testing Entity Class ==========")

    # Create a new entity
    new_entity = Entity(name='Entity Name', description='I am an entity!',
                        relations={}, properties={})
    database.add_entity(new_entity)
    print("Added entity:", new_entity.name, new_entity.description, new_entity.relations, new_entity.properties)

    # Query all entities
    entities = database.get_all_entities()
    for entity in entities:
        print(entity.name, entity.description, entity.relations, entity.properties)

    # Update an entity
    entity = entities[0]
    entity.description = 'Updated description'
    entity.relations = {'friend': 'NPC'}
    entity.properties = {'alignment': 'Neutral'}
    database.update_entity(entity)
    print("Updated entity:", entity.name, entity.description, entity.relations, entity.properties)

    # Delete an entity
    entity = entities[0]
    database.delete_entity(entity)
    print("Deleted entity:", entity.name)

    # Print entities table
    database.print_table('entities')

# ========== Test: Character ========== #

def test_character():
    print("========== Testing Character Class ==========")

    # Create new characters
    characters = [
        Character(character_id=1, name={'first_name': 'Adam', 'last_name': 'Stone'}, description='I am a character!',
                  inventory={}, equipment={}, relations={}, statistics={}, properties={}, type='npc'),
        Character(character_id=2, name={'first_name': 'Emily', 'last_name': 'Smith'}, description='I am another character!',
                  inventory={}, equipment={}, relations={}, statistics={}, properties={}, type='npc'),
        Character(character_id=3, name={'first_name': 'John', 'last_name': 'Doe'}, description='I am yet another character!',
                  inventory={}, equipment={}, relations={}, statistics={}, properties={}, type='npc')
    ]

    # Add characters to the database
    for character in characters:
        database.add_character(character)
        print("Added character:", character.character_id, character.name, character.description,
              character.inventory, character.equipment, character.relations,
              character.statistics, character.properties)

    # Query all characters
    characters = database.get_all_characters()
    for character in characters:
        print(character.character_id)
        print(character.name)
        print(character.description)
        print(character.inventory)
        print(character.equipment)
        print(character.relations)
        print(character.statistics)
        print(character.properties)

    # Update a character
    character = characters[0]
    character.character_id = 7
    character.description = 'Updated description'
    character.inventory = {'item': 'Sword'}
    character.equipment = {'armor': 'Shield'}
    character.relations = {'friend': 'NPC'}
    character.statistics = {'strength': 10, 'agility': 8}
    character.properties = {'alignment': 'Good'}
    character.type = 'player'
    database.update_character(character)
    print("Updated character:", character.character_id, character.name, character.description,
          character.inventory, character.equipment, character.relations,
          character.statistics, character.properties)

    # Print characters table
    database.print_table('characters')

    # Delete a character
    character = characters[0]
    database.delete_character(character)
    print("Deleted character:", character.name)

    # Print characters table
    database.print_table('characters')

# ========== Test: Database ========== #

def test_database():
    print("========== Testing Database Functions ==========")

    # Print table structures
    database.print_tables()

def main():
    # ========== Database Initialization ========== #

    database.initialize_database()

    # ========== Test Schema Classes ========== #

    test_entity()
    test_character()

    # ========== Test Database Functions ========== #

    test_database()

    # ========== Close Session ========== #

    database.close_session()

if __name__ == '__main__':
    main()
