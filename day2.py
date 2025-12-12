# Basic lists and dictionaries program #

# Basic list usage #

fruits = ['apple', 'banana', 'cherry']
print("Initial fruit list:", fruits)

fruits.append('date')
print("Updated fruit list:", fruits)

# Basic dictionary usage #

person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Initial person dictionary:", person)

person['age'] = 31
print("Updated person dictionary:", person)

# List Comprehension
squares = [x*x for x in range(1, 11)]
print("Squares:", squares)

# Dictionary Comprehension
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print("Fruit lengths:", fruit_lengths)

# --- Mini Project: Fake Contact Generator ---

import random

first_names = ["Alex", "Sam", "Jordan", "Taylor", "Morgan", "Casey"]
last_names = ["Kim", "Rivera", "Brooks", "Lopez", "Chen", "Walker"]

def generate_contact():
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    phone = f"({random.randint(200, 999)})-{random.randint(100, 999)}-{random.randint(1000,9999)}"
    email = name.replace(" ", ".").lower() + "@example.com"
    return {
        "name": name,
        "phone": phone,
        "email": email
    }

contacts = [generate_contact() for _ in range(20)]

print("\nGenerated Contacts:")
for c in contacts:
    print(c)