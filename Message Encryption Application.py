import string
import random

def encrypt(message, key):
    alphabets = string.ascii_letters + string.digits
    #THIS TAKES INPUT AS BOTH UPPER AND LOWERCASE AND NUMBERS

    random.seed(key)
    #TO RANDOMIZE BASED ON A SEED NUMBER RANDOMLY SELECTED

    encrypted1 = ''.join(random.sample(alphabets, len(alphabets)))
    #RANDOMIZATION BASED ON LENGTH OF MESSAGE

    tableNew = str.maketrans(alphabets, encrypted1)
    #MAKE A NEW TABLE AND ASSIGN RANDOMIZED LETTERS TO CORRECT ONES

    return message.translate(tableNew)

message = input("Enter your message: ")
key = input("Enter a random key: ")
encryptedMessage = encrypt(message, key)
print("Incoming message: ", encryptedMessage)
