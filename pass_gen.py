#writing the code to generate a password generator
import random
import string

print("welcome to password generator")
    #chars is used for containing all the characters
chars = string.ascii_letters + string.digits + string.punctuation

    #now asking the user to ask the user how many passwords they want
num=int(input("Enter the number of passwords you want to generate : "))

    #now asking the user how much is the length of the password :
length=int(input("what is the length of the password : "))
    #considering the case where 8 is the criteria :
if length<8:
         print("the minimum password length is 8. please re-enter again.")
else:
         print("Here is the list of your passwords.")
         #now making the password:
         for _ in range(num):
                         password = ''.join(random.choice(chars) for _ in range(length))
                         print(password)
                         print("\n")
