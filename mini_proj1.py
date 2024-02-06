#building a guessing game in python
import random

x=int(input("Enter the number till where you want to guess the game : "))
def guess_the_num(x):
    random_number=random.randint(1,x)
    guess=int(input("Guess a number between 1 and {x} "))
    while guess != random_number:
     if guess < random_number:
        print('Sorry , please guess again . Too low')
     elif guess > random_number:
        print('sorry , guess again . Too high')
     
    print(f'congratulations you have guessed the number {random_number}')
    
guess_the_num(10)   
