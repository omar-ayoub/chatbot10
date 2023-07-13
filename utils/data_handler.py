import json

def load_property_data():
    with open('data/properties.json', 'r') as file:
        data = json.load(file)
    return data

def save_user_data(user_data):
    with open('data/user_data.json', 'r') as file:
        existing_data = json.load(file)

    existing_data.append(user_data)

    with open('data/user_data.json', 'w') as file:
        json.dump(existing_data, file)

# Add more functions as needed for data retrieval and storage


