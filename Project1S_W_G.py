import random
print("🎮 Welcome to Snake-Water-Gun Game!")
print("Choose: snake \"s\" | water \"w\" | gun \"g\" \n")
players = input("Choose : \"M\" for Multipler Player Or \"S\" for Single Player :  ").lower()

round = int(input("How many round you want to play? "))

#When player want to play with computer 
if players == "s":
    print("You choose Single Player Game \n")
    computer = random.choice([1,-1,0])
    # input from users
    youdict = {"s": 1, "w": -1 ,"g": 0}
    reversedict = {1:"Snake", -1:"Water" , 0:"Gun"}
    Ycount=0
    Compcount=0
    # for loop exist until the total round entered by the user
    for i in range(0,round):

        youstr = input("Enter your choice: ")
        you = youdict[youstr]
        print(f"You choose {reversedict[you]} \ncomputer choose {reversedict[computer]}")
        # condition of game

        if(computer == you):
            print("It's a Draw")
        else:
            if(computer == 1 and you == -1):# s vs w
                print("you loose!!")
                Compcount += 1

            elif(computer == 1 and you == 0):# s vs g
                print("you win!!")
                Ycount += 1

            elif(computer == -1 and you == 0):# w vs g
                print("you loose!!")
                Compcount += 1

            elif(computer == -1 and you == 1):# w vs s
                print("you win!!")
                Ycount += 1

            elif(computer == 0 and you == 1):# g vs s
                print("you loose!!")
                Compcount += 1

            elif(computer == 0 and you == -1):# g vs w
                print("you win!!")
                Ycount += 1
            else:
                print("Something went wrong!")
    # total score 
    print("___________________________________________________")   
    print("Score Board ")
    print(f"Computer : {Compcount}")
    print(f"You      : {Ycount}")
    if(Compcount > Ycount):
        print("Computer win!!")
    elif(Compcount == Ycount):
        print("It's a Draw!!")
    else:
        print("You win!!")

# Elif block for multiplayer game
elif players == "m":
    print("You choose Multiplayer Game \n")
    PLdict = {"s": 1, "w": -1 ,"g": 0}
    reversedict = {1:"Snake", -1:"Water" , 0:"Gun"}
    pl1count=0
    pl2count=0
    
    # for loop exist until the total round entered by the user
    for i in range(0,round):
        Player1 = input("Enter your choice [Player 1]: ")
        Pl1 = PLdict[Player1]
        Player2 = input("Enter your choice [Player 2]: ")
        Pl2 = PLdict[Player2]
        print(f"You choose {reversedict[Pl1]} \ncomputer choose {reversedict[Pl2]}")
        
        # condition of game rules
        if(Pl1 == Pl2):
            print("It's a Draw")
        else:
            if(Pl1 == 1 and Pl2 == -1):# s vs w
                print("Player 1 win!!")
                pl1count += 1

            elif(Pl1 == 1 and Pl2 == 0):# s vs g
                print("Player 2 win!!")
                pl2count += 1

            elif(Pl1 == -1 and Pl2 == 0):# w vs g
                print("Player 1 win!!")
                pl1count += 1

            elif( Pl1 == -1 and Pl2 == 1):# w vs s
                print("Player 2 win!!")
                pl2count += 1

            elif(Pl1 == 0 and Pl2 == 1):# g vs s
                print("Player 1 win!!")
                pl1count += 1

            elif(Pl1 == 0 and Pl2 == -1):# g vs w
                print("Player 2 win!!")
                pl2count += 1
            else:
                print("Something went wrong!")
    # score board 
    print("___________________________________________________")   
    print("Score Board ")
    print(f"Player 1 : {pl1count}")
    print(f"Player 2 : {pl2count}")
    if(pl1count > pl2count):
        print("Player 1 win!!")
    elif(pl1count == pl2count):
        print("It's a Draw!!")
    else:
        print("Player 2 win!!")