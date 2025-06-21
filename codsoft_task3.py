import random
import string

print("---- Password Maker ----")

length = input("How long should your password be? ")

try:
    length = int(length)
except:
    print("Please enter a number only.")
    quit()

if length < 4:
    print("Password should be at least 4 characters.")
    quit()

chars = string.ascii_letters + string.digits + "!@#$%^&*()"

result = ""
for i in range(length):
    result += random.choice(chars)

print("Here’s your password:", result)