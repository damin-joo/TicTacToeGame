import random

print("Tic Tac Toe Game")

print("In the two digit below, the first digit represents row, and second digit represents column")
game=[["00","01","02"],["10","11","12"],["20","21","22"]]

while(True):
    #use for loop to iterate the array
    for rows in game:
        for columns in rows:
           print(columns,end=" ")
        print()
    
    while(True):
        userinputR = input("Enter the row from 0, 1, 2: ")
        userinputC = input("Enter the column from 0, 1, 2: ")
        
        if ("2" or "1" or "0") in (userinputR, userinputC):
            game[int(userinputR)][int(userinputC)] = "X"
            break
        else:
            print("Invalid input")
    
    compChoiceR = random.randint(0,2)
    compChoiceC = random.randint(0,2)
    game[compChoiceR][compChoiceC] = "O"
    
    #game runs until all inputs are "X" or "O"
    for rows in game:
        if ("X" or "O") in rows
        for columns in rows:
            if ("X" or "O") in columns
            print(columns,end=" ")
            break
        print()
