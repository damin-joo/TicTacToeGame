import random
from itertools import chain

print("Tic Tac Toe Game")
print("First digit represents row, and second digit represents column")
game=[["00","01","02"],["10","11","12"],["20","21","22"]]

def printGame():
    for rows in game:
        for columns in rows:
           print(columns,end=" ")
        print()
    print(" ")

def compRandom():
    compChoiceR = random.randint(0,2)
    compChoiceC = random.randint(0,2)
    game[compChoiceR][compChoiceC] = " O"


printGame()
compRandom()

while(True):
    #use for loop to iterate the array
    printGame()
    
    while(True):
        userinputR = input("Enter the row from 0, 1, 2: ")
        userinputC = input("Enter the column from 0, 1, 2: ")
        
        if "2" or "1" or "0" in (userinputR, userinputC):
            if " O" in game[int(userinputR)][int(userinputC)]:
                print("Value already exist in the space, input a different value")
            elif " X" in game[int(userinputR)][int(userinputC)]:
                print("Value already exist in the space, input a different value")
            else:
                game[int(userinputR)][int(userinputC)] = " X"
                break
        else:
            print("Invalid input")
    
    printGame()  
        
    compRandom()
    
    game=[[" X"," 2"," X"],[" X","22"," O"],[" 1","01","20"]]
    
    #game stops when a column is all X or all O
    
    #game stops when a row is all X or all O
    
    #game stops when diagonal is all X or all O

    
    #game stops when all inputs are X or O
    if all(all(item == " O" or item == " X" for item in items) for items in game):
        printGame()
        break

        
