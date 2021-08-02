"""
    Dictionary in python is like as JSON
    Key, Value pair
    {'name': 'akash', 'age': 20}

"""

person = {'name': 'akash', 'age': 20}

print(f"Name : {person['name']} , Age : {person['age']} is a {type(person['age'])}")

person['country'] = 'IND'

print(person)

# We can creat a dictionary by calling method dict()

address = dict(state='HARYANA', pin=121106, district='PALWAL')
print(address)
person['address'] = address
print(person)

for k in person.keys():
    print(k + ' ---> ' + str(person[k]) + ' ---- ' + str(type(person[k])))
