# conftest.py
import pytest
import random
import string

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = "test.com"
    return f"{username}@{domain}"

@pytest.fixture
def random_email():
    return generate_random_email()
