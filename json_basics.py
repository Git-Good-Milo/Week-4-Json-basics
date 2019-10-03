import json

car_data = {
    'engine': 'electric',
    'brand': 'Peugeot',
    'price': 13000,
    'model': 'Ze'
}

print(type(car_data))

# dict to str using json.dumps(dict)
car_data_json_string = json.dumps(car_data)

print(car_data_json_string)
print(type(car_data_json_string))

# Write a json file so we can send it
car_data = {'engine': 'electric', 'brand': 'Peugeot', 'price': 13000, 'model': 'Ze'}

with open('new_json_file.json', 'w') as jasonfile:
    json.dump(car_data, jasonfile)

    # this json.dump(arg1, arg2) --> .json file
        # Arg1 is a dictionary and arg 2 is the file to dump the json.