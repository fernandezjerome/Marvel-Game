from gameComponents import gameQuestions, design
from PIL import Image
import time, os

def cls(): # this function clear screen
    os.system("clear")

def new_round(): # this function for new marvel game
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in gameQuestions.questions:
        cls()
        print(design.marvel)
        print(design.guessingGame)
        print(key)
        for i in gameQuestions.options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_marvel_answer(gameQuestions.questions.get(key), guess)
        question_num += 1

    display_percent_score(correct_guesses, guesses)

# this function  will determine if the answers were correct
def check_marvel_answer(answer, guess):

    if answer == guess:
        # print("CORRECT!")
        
        if answer == "D":
            image3 = Image.open("img/image3.jpg")
            image3.show()
      
            return 1
        elif answer == "C":
            image2 = Image.open("img/image2.jpg")
            image2.show()
            return 1
        elif answer == "B":
            image1 = Image.open("img/image1.jpg")
            image1.show()
            return 1
        else:
            image0 = Image.open("img/image0.jpg")
            image0.show()
            return 1   
    else:
        # print("WRONG!")
        return 0

# this function will show the scores
def display_percent_score(correct_guesses, guesses):
    cls()
    print(design.marvel)
    time.sleep(.5)
    print(design.guessingGame)
    time.sleep(.5)
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")
    print("Answers: ", end="")
    for i in gameQuestions.questions:
        print(gameQuestions.questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(gameQuestions.questions))*100)
    print("Your score is: "+str(score)+"%")
    if correct_guesses == 1:
        twen = Image.open("img/20.jpg")
        twen.show()
    elif correct_guesses == 2:
        forty = Image.open("img/40.jpg")
        forty.show()
    elif correct_guesses == 3:
        sixty = Image.open("img/60.jpg")
        sixty.show()
    elif correct_guesses == 4:
        eigthy = Image.open("img/80.jpg")
        eigthy.show()
    elif correct_guesses == 5:
        perfect = Image.open("img/80.jpg")
        perfect.show()                 
    else:
        zero = Image.open("img/00.jpg")
        zero.show()    

# this fuction will ask the player if you will play again
def new_game():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
new_round()

while new_game(): # This fucntion for a new game
    new_round()

print("Byeeeeee!")


