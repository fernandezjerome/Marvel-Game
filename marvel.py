from gameComponents import gameQuestions, design, checkAnswer, calculateScore, newGame
import os

def new_round(): # this function for start/loop to new marvel game
    guesses = [] # empty value for storing the guesses
    correct_guesses = 0 # counter for number of guess
    question_num = 1
    for key in gameQuestions.questions:
        os.system("clear")
        print(design.marvel)
        print(design.guessingGame)
        print(key)
        for i in gameQuestions.options[question_num-1]: # Subtracted 1 in question_num to became 0, the first start of the array in python is 0.
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess) # this will store the 5 guesses
        correct_guesses += checkAnswer.check_marvel_answer(gameQuestions.questions.get(key), guess)
        question_num += 1 # this will go through all questions until reaches the declared how many questions.
    calculateScore.display_percent_score(correct_guesses, guesses)

new_round()

while newGame.new_game():
    new_round()

os.system("clear")
print(design.marvel)
print(design.guessingGame)
print(design.exitText)

