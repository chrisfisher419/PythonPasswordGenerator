import random

print("Random Password Generator!")
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=.;<>/{}[]|'
length = input("How long would you like the password to be? Enter a number.")
length = int(length)
count = input("How many passwords would you like to generate?")
count = int(count)
for p in range(count):
    password =''
    for c in range(length):
        password += random.choice(chars)
    print(password)
print("Enjoy your new passwords!")
