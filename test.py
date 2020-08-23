import random
#------------------------------------------------------------------------------------------
def PSoption1():
    SSide = float(input("Please enter the smallest side:  "))
    LSide = float(input("Please enter the Longest side:  "))
    A2 = (SSide * SSide)
    B2 = (LSide * LSide)
    FindHypotenuse = (A2 + B2)
    FindHypotenuse = (FindHypotenuse ** 0.5)
    print("The answer is:", FindHypotenuse)
def PSoption2():
    LSide = float(input("Please enter the Longest side:  "))
    Hypotenuse = float(input("Please enter the Hypotenuse:  "))
    B2 = (LSide * LSide)
    C2 = (Hypotenuse * Hypotenuse)
    FindSSide = (C2 - B2)
    FindSSide = (FindSSide ** 0.5)
    print("The answer is:", FindSSide)
def PSoption3():
    SSide = float(input("Please enter the smallest side:  "))
    Hypotenuse = float(input("Please enter the Hypotenuse:  "))
    A2 = (SSide * SSide)
    C2 = (Hypotenuse * Hypotenuse)
    FindLSide = (C2 - A2)
    FindLSide = (FindLSide ** 0.5)
    print("The answer is:", FindLSide)
#------------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------------
def Login():
    # loads usernames in a list
    file = open("UserInfo.txt", "r")
    line = file.read()
    data = line.split(",")
    file.close()
    UsernamesList = []
    for i in range(len(data)):
        UsernamesList.append(data[i])
    file.close()
    print(data[1])
    print(UsernamesList)

    # loads passwords in a list
    file = open("UserInfoP.txt", "r")
    line = file.read()
    data = line.split(",")
    file.close()
    PasswordList = []
    for i in range(len(data)):
        PasswordList.append(data[i])
    print(data[1])
    print(PasswordList)

    # main login code
    print("(------------Login------------)")
    username1 = str(input("Please enter username? "))
    password1 = str(input("Please enter password? "))
    correct = (False)
    while correct != (True):
        for i in range(len(data)):
            print(len(data))
            if UsernamesList[i] == username1 and PasswordList[i] == password1:
                print("(------------Welcome------------)")
                correct = (True)
                break
            elif UsernamesList[i] == username1 and PasswordList[i] != password1:
                print("(------------Wrong Password------------)")
                password1 = str(input("Please enter password? "))
            elif UsernamesList[i] != username1 and PasswordList[i] != password1:
                print("(------------Wrong Username------------)")
                username1 = str(input("Please enter username? "))
                password1 = str(input("Please enter password? "))
    # End For
# End While
def Create():
    username = input("Please enter username? ")
    password = input("Please enter password? ")
    file = open("UserInfo.txt", "a")
    file.write(username + "\n")
    file.close()
    file = open("UserInfoP.txt", "a")
    file.write(password + "\n")
    file.close()
    Login()
#------------------------------------------------------------------------------------------
# Main Menu
print("(------------Main Menu------------)")
print("1. Pythagoras Solver")
print("2. Rock, Paper, Scissors")
print("3. Login Server")
print("4. Battle of the Bands")
print("5. Password Reminder")
print("Please enter a number.")
choice = int(input("Choose an option: "))

# Main menu While loop and error checker
while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
    choice = int(input("Error, enter 1, 2, 3, 4 or 5: "))
if choice == 1:
    print("(------------Pythagotas Solver------------)")
    # What sides do you know?
    print("What sides do you know?")
    print("1. Longest and Smallest")
    print("2. Longest and Hypotenuse")
    print("3. Smallest and Hypotenuse")
    choice = int(input("Choose an option: "))
    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input("Error, enter 1, 2 or 3: "))
    if choice == 1:
        PSoption1()
    elif choice == 2:
        PSoption2()
    elif choice == 3:
        PSoption3()
    else:
        print("(------------Invalid------------)")
elif choice == 2:
    RockPaperScissors()
elif choice == 3:
    # Main Menu
    print("(------------Login Server------------)")
    print("1. Login 1")
    print("2. Create New 2")
    choice = int(input("Choose an option: "))
    while choice != 1 and choice != 2:
        choice = int(input("Error, enter 1 or 2: "))
    if choice == 1:
        Login()
    elif choice == 2:
        Create()
    else:
        print("Invalid")
elif choice == 4:
    print("4. Battle of the Bands")
elif choice == 5:
    print("Please enter a number.")
else:
    print("(------------Invalid------------)")
#------------------------------------------------------------------------------------------
