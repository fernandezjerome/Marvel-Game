from PIL import Image

image0 = Image.open("image0.jpg")
image1 = Image.open("image1.jpg")
image2 = Image.open("image2.jpg")
image3 = Image.open("image3.jpg")


# image0.show()

# this function for new marvel game
def new_round():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_marvel_answer(questions.get(key), guess)
        question_num += 1

    display_percent_score(correct_guesses, guesses)

# this function  will determine if the answers were correct
def check_marvel_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        # return 1
        if answer == "D":
            print('correct one')
            image0 = Image.open("image0.jpg")
            image0.show()
            return 1
        elif answer == "C":
            print('correct two')
            image0 = Image.open("image0.jpg")
            image0.show()

            return 1
        elif answer == "B":
            print('correct Three')               
            image0 = Image.open("image0.jpg")
            image0.show()

            return 1
        else:
            print('corren four')
            image0 = Image.open("image0.jpg")
            image0.show()

            return 1
   
    else:
        print("WRONG!")
        return 0

# this function will show the scores
def display_percent_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# this fuction will ask the player if you will play again
def new_game():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
"who is a Marvel character who's alter ego in a nuclear scientist? ": "D",
"This character played by Tom Holland? ": "C",
"who's the richest character in Marvel'? ": "B",
"He's a disfigured mercenary with the superhuman ability of regeneration and physical prowess? ": "A",
}


options = [["A. Wolverine", "B. Spider-Man","C. Thor", "D. Hulk"],
          ["A. Captain America", "B. Daredevil","C. Spider-Man.", "D. Punisher"],
          ["A. Nightcrawler", "B. Iron Man","C. Ice Man", "D. Colossus"],
          ["A. Deadpool", "B. Spider-Man","C. Silver Surfer", "D. Gambit"]]

# This fucntion for a new game
new_round()

while new_game():
    new_round()

print("Byeeeeee!")
