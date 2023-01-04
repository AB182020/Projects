import string
import random

if __name__ == '__main__':
    # Get length
    length = int(input("Enter length:"))
    print('''Choose character set for password from these :
         1. Letters
         2. Digits
         3. Special characters
         4. Exit''')
    characterlist = ""
    # getting character set for password
    x = 0
    while x != 3:
        option = int(input("Pick a number "))
        if (option == 1):
            # add letters
            characterlist += string.ascii_letters
            x = x+1
        elif (option == 2):
            # add numbers
            characterlist += string.digits
            x = x+1
        elif (option == 3):
            characterlist += string.punctuation
            x = x+1
        elif (option == 4):
            break
        else:
            print("Please pick valid number")

    pswrd = []

    for i in range(length):
        randchar = random.choice(characterlist)
        pswrd.append(randchar)

 # print password
    print("Generated random password: " + "".join(pswrd))
