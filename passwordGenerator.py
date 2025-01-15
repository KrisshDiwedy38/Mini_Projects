''' 
Password Generator that generates strong, random passwords based on user-specified criteria such as length, inclusion of numbers, special characters, and uppercase/lowercase letters.
'''

import random
import string

def __main__():
    length = int(input("Enter the length of the password (for strong password length should be more that 8): "))
    has_numbers = input("Do you want numbers in the password? (y/n): ")
    has_upper = input("Do you want uppercase letters in the password? (y/n): ")
    has_splchar = input("Do you want special characters in the password? (y/n): ")
    has_lower = input("Do you want lowercase letters in the password? (y/n): ")
    
    choices = []    
    password = []  

    for elmt in range(length): 
        if  has_numbers == "y":
            choices.append(random.choice(string.digits))
        if has_lower == 'y':
            choices.append(random.choice(string.ascii_lowercase))
        if  has_upper == 'y':
            choices.append(random.choice(string.ascii_uppercase))
        if  has_splchar == 'y':
            choices.append(random.choice(['@', '#', '$', '%', '&', '*']))

        password.append(random.choice(choices)) 

        choices.clear()  

    
    for elmt in password:
        print(elmt, end="")

__main__()



         



      
      



