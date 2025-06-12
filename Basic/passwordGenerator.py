''' 
Password Generator that generates strong, random passwords based on user-specified criteria such as length, inclusion of numbers, special characters, and uppercase/lowercase letters.
'''

import random
import string

def __main__():
    #Ask the user for the elements they want in their password
    length = int(input("Enter the length of the password (for strong password length should be more that 8): "))
    has_numbers = input("Do you want numbers in the password? (y/n): ")
    has_upper = input("Do you want uppercase letters in the password? (y/n): ")
    has_splchar = input("Do you want special characters in the password? (y/n): ")
    has_lower = input("Do you want lowercase letters in the password? (y/n): ")
    
    choices = []    
    password = []  

    #Checks if the category of input is to be used or not
    for elmt in range(length): 
        #if yes selects a random element from that category and stores in list 'choices'
        if  has_numbers == "y":
            choices.append(random.choice(string.digits))
        if has_lower == 'y':
            choices.append(random.choice(string.ascii_lowercase))
        if  has_upper == 'y':
            choices.append(random.choice(string.ascii_uppercase))
        if  has_splchar == 'y':
            choices.append(random.choice(['@', '#', '$', '%', '&', '*']))

        #chooses a random element from choices and stores in password
        password.append(random.choice(choices)) 

        #Empty list choice for next iteration
        choices.clear()  

    #Prints the random password
    for elmt in password:
        print(elmt, end="")

__main__()



         



      
      



