import random
import string

def generate_password(length):
    if length < 1:
        print("Password length should be at least 1.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f'Generated Password: {password}')

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    generate_password(length)
