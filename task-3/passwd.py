characters = [
    # Lowercase letters
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',

    # Uppercase letters
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',

    # Digits
    '0','1','2','3','4','5','6','7','8','9',

    # Special characters
    '!','@','#','$','%','^','&','*','(',')','-','_','=','+',
    '`','~','[',']','{','}','|','\\',':',';','"',"'",'<','>',',','.','?','/',' '
]

# print(len(characters))
#length of character_list is 95

print("Welcome to my password generator")
desired_length=int(input("Enter your desired length of password: "))

import random


# print(random.choice(characters))
passwrd=""
for i in range(desired_length):
    passwrd+=random.choice(characters)

print(f"Your password is : {passwrd}")