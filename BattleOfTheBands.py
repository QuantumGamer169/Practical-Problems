def BattleOfTheBands():
    print("BattleOfTheBands")
    # Main Info Colection
    list = []
    HowMany = int(input("How many bands are there?  "))
    # What scores the bands got
    for i in range(HowMany):
        Name = str(input("Please enter the name?  "))
        score = int(input("Please enter the score?  "))
        list.append([Name, score])
    print(list)
    list = sorted(list, key=lambda data: data[1])
    print(list)
