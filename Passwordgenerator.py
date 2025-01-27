import string
import random

def get_user_input():
     
    length = int(input("Enter password length (minimum 5 characters): "))
    while length < 5:
        print("Password length should be at least 5.")
        length = int(input("Enter password length (minimum 5 characters): "))
    
     
    print("\nWhat types of characters should the password include?")
    lowercase = input("Include lowercase letters (y/n): ").lower() == 'y'
    uppercase = input("Include uppercase letters (y/n): ").lower() == 'y'
    digits = input("Include digits (y/n): ").lower() == 'y'
    specials = input("Include special characters (y/n): ").lower() == 'y'
    
    return length, lowercase, uppercase, digits, specials
def build_char_pool(lowercase, uppercase, digits, specials):
 
    pool = ''
    if lowercase:
        pool += string.ascii_lowercase
    if uppercase:
        pool += string.ascii_uppercase
    if digits:
        pool += string.digits
    if specials:
        pool += string.punctuation
    return pool

def generate_password(length, pool):
     
    if len(pool) == 0:
        print("Error: No character types selected.")
        return None
    
    password = ''.join(random.choice(pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Custom Password Generator!")

     
    length, lowercase, uppercase, digits, specials = get_user_input()


    pool = build_char_pool(lowercase, uppercase, digits, specials)

    
    password = generate_password(length, pool)

    if password:
        print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
