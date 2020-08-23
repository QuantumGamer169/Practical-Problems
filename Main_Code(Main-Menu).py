#imports the PythagorasSolver into it
from PythagorasSolver import PSoption1
from PythagorasSolver import PSoption2
from PythagorasSolver import PSoption3
#imports the PythagorasSolver into it
from RockPaperScissors import RockPaperScissors
from LoginServer import Login
from LoginServer import login2
from LoginServer import Create

#Main Menu
print("(------------Main Menu------------)")
print("1. Pythagoras Solver")
print("2. Rock, Paper, Scissors")
print("3. Login Server")
print("4. Battle of the Bands")
print("5. Password Reminder")
print("Please enter a number.")
choice = int(input("Choose an option: "))

#Main menu While loop and error checker
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
	print("1. Login ")
	print("2. Create New")
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