import string, random

def passGen(length):
    characters = string.ascii_letters + string.digits
    passwd = ""
    for c in range(length):
        passwd += random.choice(characters)
    print(passwd)


length = input("Quantos digitos? ")
passGen(length)
