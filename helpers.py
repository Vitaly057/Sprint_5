import random
import string

def generate_random_email() -> str:
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_part}@test.ru"
