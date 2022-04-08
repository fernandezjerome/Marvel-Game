from PIL import Image


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
        else :
            image0 = Image.open("img/image0.jpg")
            image0.show()
            return 1   
    else:
        return 0