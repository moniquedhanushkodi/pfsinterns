#Purpose: Generate Randomized Password
#Used: Python lists, string manipulation, and the random library 

#Created By: Monique Priyan Dhanushkodi
#Created On: February 14, 2025

import random
print("Task 2: Password Generator")

#common variable lists
cv_len_options = ["8", "9", "10", "11", "12"]
cv_scn_options = ["yes", "no", "y", "n"]

#user inputs
i_length = input("Please enter the preferred length of password (8-12): ")
while i_length not in cv_len_options:
    print("Invalid input. Please try again.")
    i_length = input("Please enter the preferred length of password (8-12): ")
i_length = int(i_length)


i_specialChars = input("Should there be special characters in the password (Y/N)? ").lower()
while i_specialChars not in cv_scn_options:
    print("Invalid input. Please try again.")
    i_specialChars = input("Should there be special characters in the password (Y/N)? ").lower()
if i_specialChars == "yes" or i_specialChars == "y":
    i_specialChars = True
else:
    i_specialChars = False

i_numbers = input("Should there be numbers in the password (Y/N)? ").lower()
while i_numbers not in cv_scn_options:
    print("Invalid input. Please try again.")
    i_numbers = input("Should there be numbers in the password (Y/N)? ").lower()
if i_numbers == "yes" or i_numbers == "y":
    i_numbers = True
else:
    i_numbers = False
 
#initializing list
v_password = []
lv_specialChars = ["!", "@", "#", "$", "^", "&", "*", "(", ")"]
lv_alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lv_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#specifying length of characters (special characters, numbers, upper characters)
if i_specialChars:
    n_specialChars = 2 
else:
    n_specialChars = 0
if i_numbers:
    n_numbers = 2
else:
    n_numbers = 0

n_upperChars = 2

#logic starts
while i_length > 0:

    if n_upperChars > 0:
        v_password.append(lv_alphabets[random.randint(0, len(lv_alphabets) - 1)].upper())
        n_upperChars -= 1
        
    elif n_specialChars > 0:
        v_password.append(lv_specialChars[random.randint(0, len(lv_specialChars) - 1)])
        n_specialChars -= 1

    elif n_numbers > 0:
        v_password.append(lv_numbers[random.randint(0, len(lv_numbers) - 1)])
        n_numbers -= 1

    else:
        v_password.append(lv_alphabets[random.randint(0, len(lv_alphabets) - 1)])

    i_length -= 1

#logic ends

#final output
print("Generated Password: " + "".join(v_password))
