# Create an auto-incrementing ID generator
# Assign IDs to a list of users
# Start from ID 1001

users = ["Alice", "Bob", "Charlie", "David", "Eve"]

import itertools

def id_generator(users):
    print("Output")
    print("User IDs: ")
    for user_id, user in zip(itertools.count(1001), users):
        print(f"{user_id}: {user}")

id_generator(users)