import random
def RockPaperScissors():
    print("(------------Rock, Paper, Scissors------------)")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors ")
    PlayersChoice = int(input("Please enter 1, 2 or 3:  "))
    while PlayersChoice != 1 and PlayersChoice != 2 and PlayersChoice != 3:
        print("(------------ERROR------------)")
        PlayersChoice = int(input("Please enter 1, 2 or 3:  "))
    while PlayersChoice != 0:
        computer = (random.randint(1, 3))
        print(computer)
        if computer == PlayersChoice:
            print("(------------Draw------------)")
        elif computer == 1 and PlayersChoice == 3:
            print("(------------Computer wins------------)")
        elif computer == 2 and PlayersChoice == 1:
            print("(------------Computer wins------------)")
        elif computer == 3 and PlayersChoice == 1:
            print("(------------Computer wins------------)")
        elif computer == 3 and PlayersChoice == 2:
            print("(------------Computer wins------------)")
        elif computer == 3 and PlayersChoice == 1:
            print("(------------You win------------)")
        elif computer == 1 and PlayersChoice == 2:
            print("(------------You win------------)")
        elif computer == 1 and PlayersChoice == 3:
            print("(------------You win------------)")
        elif computer == 2 and PlayersChoice == 3:
            print("(------------You win------------)")
        PlayersChoice = int(input("Please enter 1, 2 or 3(Enter 0 To EXIT):  "))