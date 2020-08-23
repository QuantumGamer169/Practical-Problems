def Login():
	#loads usernames in a list
	file = open("UserInfo.txt", "r")
	line = file.read()
	data = line.split(",")
	file.close()
	UsernamesList = []
	for i in range (len(data)):
		UsernamesList.append(data[i])
	file.close()

	#loads passwords in a list
	file = open("UserInfoP.txt", "r")
	line = file.read()
	data = line.split(",")
	file.close()
	PasswordList = []
	for i in range (len(data)):
		PasswordList.append(data[i])

	#main login code
	print("(------------Login1------------)")
	username1 = str(input("Please enter username? "))
	password1 = str(input("Please enter password? "))
	correct = (False)
	print(UsernamesList)
	print(PasswordList)
	for i in range(len(data)):
		if UsernamesList[i] == username1 and PasswordList[i] == password1:
			print("(------------Welcome------------)")
			correct = (True)
			break
		elif UsernamesList[i] == username1 and PasswordList[i] != password1:
			print("(------------Wrong Password------------)")
			login2()
			break
		elif UsernamesList[i] != username1 and PasswordList[i] != password1:
			print("(------------Wrong Username------------)")
			login2()
			break
		break
	print("(------------Welcome------------)")
	#End For

def login2():
	#loads usernames in a list
	file = open("UserInfo.txt", "r")
	line = file.read()
	data = line.split(",")
	file.close()
	UsernamesList = []
	for i in range (len(data)):
		UsernamesList.append(data[i])
	file.close()

	#loads passwords in a list
	file = open("UserInfoP.txt", "r")
	line = file.read()
	data = line.split(",")
	file.close()
	PasswordList = []
	for i in range (len(data)):
		PasswordList.append(data[i])
	print(UsernamesList)
	print(PasswordList)
	#main login code
	print("(------------Login2------------)")
	username1 = str(input("Please enter username? "))
	password1 = str(input("Please enter password? "))
	correct = (False)
	print("(------------Welcome------------)")
	#End For


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