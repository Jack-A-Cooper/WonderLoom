import json
import random
from models import Character
from tabulate import tabulate

# ========== Functions ========== #

def print_fields_recursive(json_data, depth=0):
    indent = "  " * depth

    if isinstance(json_data, dict):
        for field, value in json_data.items():
            print(f"{indent}{field}")
            print_fields_recursive(value, depth + 1)
    elif isinstance(json_data, list):
        for item in json_data:
            print_fields_recursive(item, depth + 1)
    else:
        print(f"{indent}{json_data}")

def explore_json_fields(json_data, category, field_dict=None, prefix=''):
    if field_dict is None:
        field_dict = {}

    if isinstance(json_data, dict):
        for field, value in json_data.items():
            if field == category:
                field_dict[prefix + field] = value
            elif isinstance(value, (dict, list)):
                if prefix:
                    updated_prefix = f"{prefix}{field}."
                else:
                    updated_prefix = f"{field}."
                explore_json_fields(value, category, field_dict, prefix=updated_prefix)
    elif isinstance(json_data, list):
        for index, item in enumerate(json_data):
            if isinstance(item, (dict, list)):
                explore_json_fields(item, category, field_dict, prefix=f"{prefix}{index}.")
    return field_dict


def print_json_fields(field_dict):
    for field, value in field_dict.items():
        print(f"{field}: {value}")
        
def search_and_choose(json_obj, field, level=0):
    if isinstance(json_obj, dict):
        if field in json_obj:
            subfield = json_obj[field]
            if isinstance(subfield, dict):
                random_subfield = random.choice(list(subfield.keys()))
                print("Searching at Level", level, "Field:", random_subfield)
                return subfield[random_subfield]
    elif isinstance(json_obj, list):
        for item in json_obj:
            result = search_and_choose(item, field, level+1)
            if result:
                return result
    return None

def find_subfield(json_obj, subfield):
    if isinstance(json_obj, dict):
        if subfield in json_obj:
            return json_obj[subfield]
        else:
            for value in json_obj.values():
                result = find_subfield(value, subfield)
                if result:
                    return result
    elif isinstance(json_obj, list):
        for item in json_obj:
            result = find_subfield(item, subfield)
            if result:
                return result
    return None

def get_randomized_name_list(json_data, type_of_category, character_field_to_replace, key):
    # key = 'first_names' or 'last_names' - else abort
    if (key == 'first_names' or 'last_names'):
        # Extract the subfields dynamically - use key: "key"
        subfields = list(data[type_of_category][0].keys())

        # Randomly select a subfield
        selected_theme = random.choice(subfields)

        # Extract the selected subfield
        subfield = data[type_of_category][0][selected_theme]

        # Create a new JSON object called current_selection with the extracted subfield - the subfield from original data parse
        current_selection = {
            selected_theme: subfield
        }
        
        # Access the key in the new JSON object
        list = current_selection[selected_theme][key]

        # Replace character's property randomly
        character.character_field_to_replace = random.choice(list)
    else:
        print("Key must be 'first_names' or 'last_names'!\n")
        print("Defaulting {character.character_field_to_replace} to NULL!\n")
        character.character_field_to_replace = NULL

def randomize_character_property(json_data, type_of_category, character_field_to_replace, key):
    # Extract the subfields dynamically - use key: "key"
    subfields = list(data[type_of_category][0].keys())

    # Randomly select a subfield
    selected_theme = random.choice(subfields)

    # Extract the selected subfield
    subfield = data[type_of_category][0][selected_theme]

    # Create a new JSON object called current_selection with the extracted subfield - the subfield from original data parse
    current_selection = {
        selected_theme: subfield
    }
    
    # Access the key in the new JSON object
    list = current_selection[selected_theme][key]

    # Replace character's property randomly
    character.character_field_to_replace = random.choice(list)
    
def randomize_character_equipment(json_data, type_of_category, character_field_to_replace):
    # Extract the subfields dynamically - use key: "equipment"
    subfields = list(data[type_of_category][0].keys())

    # Randomly select a subfield
    selected_theme = random.choice(subfields)

    # Extract the selected subfield
    equipment_slot = data[type_of_category][0][selected_theme]

    # Create a new JSON object called current_selection with the extracted subfield - from original data parse
    current_selection = {
        selected_theme: equipment_slot
    }

    # Replace the second occurrence in the previous response with replacement2
    character.equipment[equipment_slot] = random.choice()

# ========== Random Character Generation From JSON ========== #

# Read the json file and convert it to a json object
with open('random.json') as file:
    json_data = json.load(file)

# Create a new character object
character = Character()

# Initialize the equipment slots
character.equipment = {
    'head': None,
    'body': None,
    'hands': None,
    'right_hand': None,
    'left_hand': None,
    'feet': None
}

# Create the name object with subfields
character.name = {
    'full_name': '',
    'first_name': '',
    'last_name': ''
}

# ========== Name Generation ========== #

# ========== First Name Generation ========== #

# Parse the existing JSON structure
data = json_data

# Extract the subfields dynamically - use key: "names"
subfields = list(data["names"][0].keys())

# Randomly select a subfield
selected_theme = random.choice(subfields)

# Extract the selected subfield
first_names = data["names"][0][selected_theme]

# Create a new JSON object called current_selection with the extracted subfield - first_names from original data parse
current_selection = {
    selected_theme: first_names
}

# Access the 'first_names' key in the new JSON object
first_names_list = current_selection[selected_theme]["first_names"]

# Set character's first name with random choice from the randomly chosen first names list by theme
character.name['first_name'] = random.choice(first_names_list)

# ========== Last Name Generation ========== #

# Extract the subfields dynamically - use key: "names"
subfields = list(data["names"][0].keys())

# Randomly select a subfield
selected_theme = random.choice(subfields)

# Extract the selected subfield
last_names = data["names"][0][selected_theme]

# Create a new JSON object called current_selection with the extracted subfield - last_names from original data parse
current_selection = {
    selected_theme: last_names
}

# Access the 'last_names' key in the new JSON object
last_names_list = current_selection[selected_theme]["last_names"]

# Set character's last name with random choice from the randomly chosen last names list by theme
character.name['last_name'] = random.choice(last_names_list)

# ========== Full Name Generation ========== #

# Combine the first name and last name to update the full name field
character.name['full_name'] = character.name['first_name'] + " " + character.name['last_name']

# Add a new field called name to the character object
character.name['name'] = character.name['full_name']



# ========== Description Generation ========== #

character.description = "debug"
'''
# Extract the subfields dynamically - use key: "descriptions"
subfields = list(data["descriptions"][0].keys())

# Randomly select a subfield
selected_theme = random.choice(subfields)

# Extract the selected subfield
descriptions = data["descriptions"][0][selected_theme]

# Create a new JSON object called current_selection with the extracted subfield - last_names from original data parse
current_selection = {
    selected_theme: descriptions
}

# Access the 'descriptions' key in the new JSON object
descriptions_list = current_selection[selected_theme]["descriptions"]

# Set character's last name with random choice from the randomly chosen last names list by theme
character.description = random.choice(descriptions_list)

# ========== Equipment Generation ========== #

equipment = explore_json_fields(json_data, "equipment")

for slot, items in equipment.items():
    if isinstance(items, list) and items:
        item = random.choice(items)
        character.equipment[slot] = item
'''
# ========== Relationship Generation ========== #

relationships = []

# Generate a random amount of names (2-7)
num_names = random.randint(2, 7)

for _ in range(num_names):
    relationship = {}
    
    # Extract the subfields dynamically - use key: "names"
    subfields = list(data["names"][0].keys())

    # Randomly select a subfield
    selected_theme = random.choice(subfields)

    # Extract the selected subfield
    first_names = data["names"][0][selected_theme]

    # Create a new JSON object called first_names_current_selection with the extracted subfield - first_names from original data parse
    first_names_current_selection = {
    selected_theme: first_names
    }

    # Access the 'first_names' key in the new JSON object
    first_names_list = first_names_current_selection[selected_theme]["first_names"]
    
    # Extract the subfields dynamically - use key: "names"
    subfields = list(data["names"][0].keys())

    # Randomly select a subfield
    selected_theme = random.choice(subfields)

    # Extract the selected subfield
    last_names = data["names"][0][selected_theme]

    # Create a new JSON object called last_names_current_selection with the extracted subfield - last_names from original data parse
    last_names_current_selection = {
    selected_theme: last_names
    }

    # Access the 'last_names' key in the new JSON object
    last_names_list = last_names_current_selection[selected_theme]["last_names"]

    # Pick a random element from first_names and add it to the relationship
    random_first_name = random.choice(first_names_list)

    # Pick a random element from last_names and add it to the relationship
    random_last_name = random.choice(last_names_list)

    # Combine the first name and last name to create the full name
    relationship['Character'] = random_first_name + " " + random_last_name

    # Pick a random type of relationship (ally, enemy, neutral)
    relationship['type'] = random.choice(['ally', 'enemy', 'neutral'])

    relationships.append(relationship)

# Populate the character's relationships field with the generated names
character.relations = relationships

# ========== Statistics Generation ========== #

statistics = ['Strength', 'Perception', 'Endurance', 'Charisma', 'Agility', 'Intelligence', 'Luck']
character.statistics = {stat: random.randint(1, 10) for stat in statistics}

# ========== Character ID Generation ========== #

# Randomize the character_id field with an integer (1-99999999)
character.character_id = random.randint(1, 99999999)

# ========== Properties Generation ========== #

# Randomize the properties field with a random amount (0-3) of RPG properties/flags
num_properties = random.randint(0, 3)
rpg_properties = [
    "buffs", "debuffs", "titles", "ranks", "has_bounty"
]
character.properties = random.sample(rpg_properties, num_properties)

# ========== Equipment Generation ========== #

# ========== Head Slot Generation ========== #

# Extract the subfields dynamically - use key: "equipment"
subfields = list(data["equipment"][0].keys())

find_subfield(data, "equipment")

# Randomly select a subfield
selected_theme = random.choice(subfields)

# Extract the selected subfield
equipment_slot = data["equipment"][0][selected_theme]

# Create a new JSON object called current_selection with the extracted subfield - head from original data parse
current_selection = {
    selected_theme: equipment_slot
}

# Access the 'head' key in the new JSON object
random_selection = current_selection[selected_theme]

# Set character's equipment slot with a random choice from the randomly chosen list by theme
character.equipment['head'] = random.choice(random_selection)

# ========== Body Slot Generation ========== #

# Extract the subfields dynamically - use key: "equipment"
subfields = list(data["equipment"][0].keys())

# Randomly select a subfield
selected_theme = random.choice(subfields)

# Extract the selected subfield
equipment_slot = data["equipment"][0][selected_theme]

# Create a new JSON object called current_selection with the extracted subfield - body from original data parse
current_selection = {
    selected_theme: equipment_slot
}

# Access the 'body' key in the new JSON object
random_selection = current_selection[selected_theme]

# Set character's equipment slot with a random choice from the randomly chosen list by theme
character.equipment['body'] = random.choice(random_selection)

# ========== Hands Slot Generation ========== #

# Extract the subfields dynamically - use key: "equipment"
subfields = list(data["equipment"][0].keys())

# Randomly select a subfield
selected_theme = random.choice(subfields)

# Extract the selected subfield
equipment_slot = data["equipment"][0][selected_theme]

# Create a new JSON object called current_selection with the extracted subfield - hands from original data parse
current_selection = {
    selected_theme: equipment_slot
}

# Access the 'hands' key in the new JSON object
random_selection = current_selection[selected_theme]

# Set character's equipment slot with a random choice from the randomly chosen list by theme
character.equipment['hands'] = random.choice(random_selection)

# ========== Right Hand Slot Generation ========== #

# Extract the subfields dynamically - use key: "equipment"
subfields = list(data["equipment"][0].keys())

# Randomly select a subfield
selected_theme = random.choice(subfields)

# Extract the selected subfield
equipment_slot = data["equipment"][0][selected_theme]

# Create a new JSON object called current_selection with the extracted subfield - right_hand from original data parse
current_selection = {
    selected_theme: equipment_slot
}

# Access the 'right_hand' key in the new JSON object
random_selection = current_selection[selected_theme]

# Set character's equipment slot with a random choice from the randomly chosen list by theme
character.equipment['right_hand'] = random.choice(random_selection)

# ========== Left Hand Slot Generation ========== #

# Extract the subfields dynamically - use key: "equipment"
subfields = list(data["equipment"][0].keys())

# Randomly select a subfield
selected_theme = random.choice(subfields)

# Extract the selected subfield
equipment_slot = data["equipment"][0][selected_theme]

# Create a new JSON object called current_selection with the extracted subfield - left_hand from original data parse
current_selection = {
    selected_theme: equipment_slot
}

# Access the 'left_hand' key in the new JSON object
random_selection = current_selection[selected_theme]

# Set character's equipment slot with a random choice from the randomly chosen list by theme
character.equipment['left_hand'] = random.choice(random_selection)

# ========== Feet Slot Generation ========== #

# Extract the subfields dynamically - use key: "equipment"
subfields = list(data["equipment"][0].keys())

# Randomly select a subfield
selected_theme = random.choice(subfields)

# Extract the selected subfield
equipment_slot = data["equipment"][0][selected_theme]

# Create a new JSON object called current_selection with the extracted subfield - feet from original data parse
current_selection = {
    selected_theme: equipment_slot
}

# Access the 'feet' key in the new JSON object
random_selection = current_selection[selected_theme]

# Set character's equipment slot with a random choice from the randomly chosen list by theme
character.equipment['feet'] = random.choice(random_selection)

# ========== Inventory Generation ========== #

# Randomize the number of items within the valid range
num_items = random.randint(0, min(30, 75))

# Initialize character.inventory as an empty list or dictionary
character.inventory = []

for _ in range(num_items):
    # Extract the subfields dynamically - use key: "items"
    subfields = list(data["items"][0].keys())

    # Randomly select a subfield
    selected_theme = random.choice(subfields)

    # Extract the selected subfield
    items = data["items"][0][selected_theme]

    # Create a new JSON object called current_selection with the extracted subfield - items from original data parse
    current_selection = {
        selected_theme: items
    }

    # Access the 'items' key in the new JSON object
    items_list = current_selection[selected_theme]

    # Select an item from the theme to add to the character's inventory
    item_to_add = random.choice(items_list)

    # Add the selected item to the character's inventory JSON object
    character.inventory.append(item_to_add)

# ========== Print Out Generated Character ========== #

# Print the character object fields
print(f"Character ID: {character.character_id if character.character_id else 'No character id'}")
print(f"Name: {character.name['full_name'] if character.name['full_name'] else 'Unknown'}")
print(f"Description: {character.description if character.description else 'No description'}")
print(f"Equipment: {character.equipment if character.equipment else 'No equipment'}")
print(f"Relations: {character.relations if character.relations else 'No relations'}")
print(f"Statistics: {character.statistics if character.statistics else 'No Statistics'}")
print(f"Properties: {character.properties if character.properties else 'No properties'}")
print(f"Inventory: {character.inventory if character.inventory else 'No inventory'}")

# ========== DEBUG ========== #

'''
# Specify the category to find
category = 'items'

# Explore the JSON fields and obtain the dictionary
json_fields = explore_json_fields(json_data, category)

# Print the JSON fields dictionary
print("Fields found in the JSON object:")
print_json_fields(json_fields)

# Print the fields found in the JSON object
print("Fields found in the JSON object:")
print_fields_recursive(json_data)

# Iterate through the names key and generate random names for relationships
names = explore_json_fields(json_data, "names")

# Search for the field "names" and choose a random subfield
random_subfield = search_and_choose(json_data, "first_names")
print("Random Subfield from 'names':", random_subfield)

# Parse the existing JSON structure
names = json_data

# Extract the subfields dynamically
subfields = list(names["names"][0].keys())

# Randomly select a subfield
selected_subfield = random.choice(subfields)

# Extract the selected subfield
subfield = names["names"][0][selected_subfield]

# Create a new JSON object with the extracted subfield
new_json_obj = {
    selected_subfield: subfield
}

# Convert the new JSON object to a string
new_json_str = json.dumps(new_json_obj, indent=4)

print(new_json_str)
'''


'''
NOTE: Equipment generation needs to be fixed to put equipment into the correct slot! - BUG (e.g., "Gloves on feet!")
NOTE: Description generation is currently bugged
'''