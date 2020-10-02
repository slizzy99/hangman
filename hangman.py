
import random
def hangman():
    words = ["penis","fatbastard","austinpowers","jackblack","garry","cheatur",
             "preyz"]
    rand = random.randint(0,6)
    word = words[rand]
    stages = ["",
             "________        ",
             "|      |        ",
             "|      |        ",
             "|      0        ",
             "|     /|\       ",
             "|     / \       ",
             "|               "]
    wrong = 0
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome To Hangman")
    while wrong < len(stages) - 2:
        print("\n")
        msg = "Guess a letter! "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
            print(" ".join(board))
        else:
            wrong += 1
            print(" ".join(board))
            e = wrong + 1
            print("\n".join(stages[1: e]))
        if "__" not in board:
            print("\n")
            print("You Won!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n")
        print("\n".join(stages))
        print("You lost fucker! The word was {}!".format(word))
        print("2020-10-01")
       
hangman()
