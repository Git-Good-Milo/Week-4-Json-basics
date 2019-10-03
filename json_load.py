import json

# Here we load / decofe json

with open ('new_json_file.json', 'r') as jsonfile:
    # conert to dictionary
    car_dictionary = json.load(jsonfile)
    print(car_dictionary)
    print(type(car_dictionary))
    print(car_dictionary["brand"])