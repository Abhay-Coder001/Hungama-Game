#                             HANGMAN GAME     
  
# Firstly we import the required modules for this program.        
import random
import time
# Initial steps to invite in the game.
print("\n Welcome to Hangman game \n")
name = input("Enter your name :")
print("Hello"+name+"! Best of luck!")
time.sleep(2) #time.sleep(2) basically 2 indicates here the delay of next line will appear in 2 seconds.
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3) #same goes for here but time delay will be 3 seconds.

#Now we create a main function
def main(): 
    #All these used in below code afterwards..
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    word_to_guess = ["January","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"] #Here we create a list of all the choices we give
    word = random.choice(word_to_guess)
    length = len(word)
    count = 0
    display = '_'*length #This draws a line for us according to the length of word.
    already_guessed = [] #This would contain the string indices of the currently guessed word.
    play_game = ""

# Now we create a loop to re-execute the game when the first round ends.
def play_loop(): #This function takes argument to either continue the game after it is played once or end it according to what user suggest.
    global play_game
    while play_game not in ['Y','y','n','N']:
        play_game = input("Do you want to play again?\n Y = yes   N = no")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for playing ! We expect you back again.")

