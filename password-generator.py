import random
import string
def password_generator():
    try:
        length=int(input("Enter the password length you want:"))
        if length<6:
            print("password should atleast have 6 characters")
        characters=string.ascii_letters+string.digits+string.punctuation
        password=''.join(random.choice(characters)for i in range(length))
        print(f"password:{password}")
    except ValueError:
        print("Enter only digits!!")
password_generator()