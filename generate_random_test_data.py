import random
import string
import json

# generating random email for valid user email signup 
def generate_random_email(domain="example.com"):
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_string}@{domain}"


test_data_file = 'test_data.json'

with open(test_data_file, 'r') as f:
    data = json.load(f)

random_email = generate_random_email()
data["valid_user_signup"]["email"] = random_email


with open(test_data_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Updated test_data.json with the new email: {random_email}")
