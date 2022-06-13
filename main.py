import random


print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")


while True:
    print("Enter choice  Rock, \n  paper, and scissor \n")
     
    # take the input from user
    choice = input("User turn :")
 
    if((choice != "Rock")  or (choice != "paper") or (choice != "scissor")):
        choice = input("Enter valid choice")

    # print user choice
    print("user choice is: " + choice)
    print("\nNow its computer turn.......")
 
    comp_choice = random.randint(1, 3)
  
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
         
    print("Computer choice is: " + comp_choice_name)
 
    print(choice + " V/s " + comp_choice_name)
    #we need to check of a draw
    result = 'expected value'

    if choice == comp_choice:
        print("Draw=> ", end = "")
        result = "Draw"

        if((choice == "Rock" and comp_choice_name == "paper") or
          (choice == "paper" and comp_choice_name =="Rock" )):
            print("paper wins => ", end = "")
            result = "paper"
 
        elif((choice == "Rock" and comp_choice_name == 'scissor') or
            (choice == 'scissor' and comp_choice_name == "Rock")):
            print("Rock wins =>", end = "")
            result = "Rock"
        else:
            print("scissor wins =>", end = "")
            result = "scissor"
     # Printing either user or computer wins or draw
    if result == "Draw":
        print("<== Its a tie ==>")
    if result == choice:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
         
    print("Do you want to play again? (Y/N) \n")
    ans = input().lower
 
 
    # if user input n or N then condition is True
    if ans == 'n':
        break
     
# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")