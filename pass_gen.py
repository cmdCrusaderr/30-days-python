#writing the code to generate a password generator
import random
import string
def pass_generator( len,password[] ):
    #generating a password of length of len
    len=int(input("enter the password : "))
    if(len<=8):

        print("please enter the valid password length again.")
    
    else:
    
        #we will give the choice to the user 
        #how many special char? 1/2
        # Define the special characters
        special_chars = "!@#$%^&*()_+-="
        
        # Ask the user how many special characters they want in their password
        ask = int(input("How many special characters do you want in your password: 1 or 2? "))
        
        # Use match statement to handle user choice
        match ask:
            case 1:
                # Generate a random special character
                random_char = random.choice(special_chars)
                print(f"Random special character: {random_char}")
            case 2:
                # Generate two random special characters
                random_chars = random.choices(special_chars, k=2)
                print(f"Random special characters: {''.join(random_chars)}")
            case _:
                print("Invalid choice. Please select 1 or 2.")
                
        password.append(random_chars)
        