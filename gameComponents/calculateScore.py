from PIL import Image
from gameComponents import gameQuestions, design
import  os

# this function will show the scores
def display_percent_score(correct_guesses, guesses):
    os.system("clear")
    print(design.marvel)
    print(design.guessingGame)
    print(design.resutText)
    print("                                 Answers: ", end="")
    for i in gameQuestions.questions:
        print(gameQuestions.questions.get(i), end=" ")
    print()

    print("                                 Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(gameQuestions.questions))*100)
    print("Your score is: "+str(score)+"%")
    print("You guessed "+str(correct_guesses)+"/5")
    print('')
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
        perfect = Image.open("img/100.jpg")
        perfect.show()                 
    else:
        zero = Image.open("img/00.jpg")
        zero.show()    
