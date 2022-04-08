def new_game():
    response = input("Press (Yes) to play again, Any key to quit\n")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

