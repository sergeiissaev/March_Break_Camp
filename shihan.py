import random
alive = True
lives = 3
end = False
for i in range(0, lives):
    alive = True
    if end == True:
        break
    print("The game starts now. You have", lives, "lives")
    print("You wake up in the dark and what seems like a room. There is a door right behind you. \nThere is a lock on the door. Do you (1) try to pick \nthe lock and escape or (2) try to yell for help or (3) lie down and accept that you are trapped. ")
    choice = int(input())
    while alive == True:
        if choice == 1:
            print("You have pick correctly. You start by trying to solve the first lock. It has a keyhole. Do you (1) search for the key (2) try to pick it or (3) try to break the lock with force.")
            choice2 = int(input())
            if choice2 == 1:
                print("The key was in your back pocket you unlock the door and run to the door. \nThe door is jammed. But you see a window. Do you (1) break the window with you hand \n (2) find something to break it with or (3) search for another exit")
                choice3 = int(input())
                if choice3 == 1:
                    print("You broke you hand while trying to escape press q to try again")
                    q2 = input()
                    if q2 == "q" or q2 == "Q":
                        alive = False
                        lives = lives - 1
                elif choice3 == 2:
                    print("You search for something to escape with. You remember the key you used earlier and then you smash the window with the key and escape. End")
                    end = True
                    break
                elif choice3 == 3:
                    print("You search around the house but you walk into someone that made you regret your decision. Press q to restart.")
                    q3 = input()
                    if q3 == "q" or q3 == "Q":
                        alive = False
                        lives = lives - 1
                elif choice3 != 1 or choice3 != 2 or choice3 !=3:
                    print("Not a valid option")
            elif choice2 == 2:
                print("You try to pick it. Soon after someone hears you that when you see him you regret your decision. Press q to restart")
                q4 = input()
                if q4 == "q" or q4 == "Q":
                    alive = False
                    lives = lives - 1
            elif choice2 == 3:
                print("You try to break it. Soon after someone hears you that when you see him you regret your decision. Press q to restart")
                q5 = input()
                if q5 == "q" or q5 == "Q":
                    alive = False
                    lives = lives - 1
            elif choice2 != 1 or choice2 != 2 or choice2 != 3:
                print("Not a valid option")
        elif choice == 2:
            print("You try to shout. You were lucky and someone came but it was someone you probably wouldn't want to open that door. You get knocked out and you don't wake up again. Press q to restart.")
            q = input()
            if q == "q" or q == "Q":
                alive = False
                lives = lives - 1
        elif choice == 3:
            print("You lie down and sleep. The next day someone does come to help you and it was an ally. You are with someone else but you don't know where you are or who this person is. Should you (1) team up with this person or (2) run away from them or (3) take all their supplies and lock them in the room.")
            choice4 = int(input())
            if choice4 == 1:
                print("You teamed up with this person and escaped together. End.")
                end = True
                break
            elif choice4 == 2:
                print("You ran away from this person and you bump into someone that when you see him you regret your decision. Press q to restart")
                q6 = input()
                if q6 == "q" or q6 == "Q":
                    alive = False
                    lives = lives - 1
            elif choice4 == 3:
                print("You stole the person supplies and run away. Your selfishness saved you but you will always regret your \ndecision that let the other person stuck in the house forever. End")
                end = True
                break
            elif choice4 != 1 or choice4 != 2 or choice4 != 3:
                print("Not a valid option")
        elif choice != 1 or choice != 2 or choice != 3:
            print("Not a valid option")
