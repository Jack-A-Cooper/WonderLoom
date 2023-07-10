from models import Character
import database

def main():
    database.initialize_database()

    # CHARACTER
    
    # Create a new chracter
    new_character = Character(name='Character Name', desc='I am a description!')
    database.add_character(new_character)

    # Query all characters
    characters = database.get_all_characters()
    for character in characters:
        print(character.name, character.desc)

    # Update a character
    character = characters[0]
    character.desc = 'my_desc'
    database.update_character(character)

    # Delete a character
    character = characters[0]
    database.delete_character(character)
    
if __name__ == '__main__':
    main()
