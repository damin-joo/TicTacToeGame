import random
import array

print("Tic Tac Toe Game")

 T = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"]]
 
#while(True):
    
  #  while(True):
        #collect user input 
      #  userxpos = input("Enter the x position of your input from 0, 1, 2: ")
       # userypos = input("Enter the y position of your input from 0, 1, 2: ")
        
        T = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"]]
        
        for r in T:
           for c in r:
              print(c,end = " ")
           print()
        
        """
        #translates string to int value
        if(userinput == "Rock"):
            print("Userinput is " + userinput)
            x = 1
            break
        elif(userinput == "Paper"):
            print("Userinput is " + userinput)
            x = 2
            break
        elif(userinput == "Scissor"):
            print("Userinput is " + userinput)
            x = 3
            break
        else:
            print("Wrong user input. Please choose between Rock Paper or Scissor")
     
    #computer chooses rock, paper, or scissor
    compChoice = random.randint(1,3)   
     
    #prints out computer choice  
    if(compChoice == 1):
        print("Computer chose Rock")
    elif(compChoice == 2):
        print("Computer is Paper")
    elif(compChoice == 3):
        print("Computer is Scissor")
    
    #compares the values to determine winner
    if(x == compChoice):
        print("It is a tie")
    elif(x == 1):
        if(compChoice == 2):
            print("The User Wins")
        else:
            #x == 3
            print("The Computer Wins")
    elif(x == 2):
        if(compChoice == 1):
            print("The Computer Wins")
        else:
            #x == 3
            print("The User Wins")
    elif(x == 3):
        if(compChoice == 1):
            print("The User Wins")
        else:
            #x == 2
            print("The Computer Wins")
    else:
        print("Error occured. Please try again")
    
    
    playAgain = input("Wanna play again? Y/N: ")
    
    if(playAgain == "N"):
        break

    """

    
