import string, random

def passGen(length):
    nice_string_punctuation = string.punctuation[2:5] + string.punctuation[-6] + string.punctuation[-11]
    characters = string.ascii_letters + string.digits + nice_string_punctuation
    passwd = ""
    for c in range(length):
        passwd += random.choice(characters)
    print(passwd)


length = input("Quantos digitos? ")
passGen(length)


