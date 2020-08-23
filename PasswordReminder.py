def caesar_encrypt(realText, step):
    outText = []
    cryptText = []

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

    for eachLetter in realText:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            crypting = (index + step) % 26
            cryptText.append(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index + step) % 26
            cryptText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)
    return outText

def Storage_Info():
    Account = str(input("Please enter account name:   "))
    Username = str(input("Please enter Username:   "))
    Password = str(input("Please enter Password:   "))
    Length = len(Password)
    EPassword = caesar_encrypt(Password , Length)
    EPassword2 = (''.join(EPassword))
    print (EPassword2)
    file = open("Info.txt", "a")
    file.write(Account + ",")
    file.write(Username + ",")
    file.write(EPassword2 + "\n")
    file.close()

def Login_Info(Account, Username):


Login_Info()




