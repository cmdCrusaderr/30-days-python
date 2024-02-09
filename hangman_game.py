#hangman game :
    #logic and help from github and google : https://gist.github.com/lupinetti/8f89e5f33750aa7c91c3

#this function is an intro to the users
def hangman_intro():
    print("welcome to the game called hangman : ")
    print("rules for the game is : One player thinks of a word and the other tries to guess it by suggesting the letters. The word to guess is represented by a row of dashes, giving the number of letters. If the guessing player suggests a letter which occurs in the word, the program writes it in all its correct positions.")

def player1_intro(name,age): #function of the guessing player
    print(f"Hello player ,{name}")
    print(f"Age : {age}")

def player2_intro(name,age):
    print(f"Hello player ,{name}")
    print(f"Age : {age}")
