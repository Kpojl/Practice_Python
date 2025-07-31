import random
import string

def generate_license_plate():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    digits = ''.join(random.choices(string.digits, k=random.choice([3, 4])))
    return digits + letters if len(digits) == 4 else letters + digits

print(generate_license_plate())