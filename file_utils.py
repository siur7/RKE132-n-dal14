import random

def get_random_file_name(filename):
    
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    items = []
        
    for line in lines:
        new_item = line.strip()
        items.append(new_item)

    random_item = random.choice(items)

    return random_item