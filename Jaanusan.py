print("Welcome to  Goosebumps Terrorville: ")

print(" Your car is stuck in the middle of an abandoned road, But there is a theme park named Terrorville, 1) Go to Terrorville, 2) Stay in the car, 3) Explore through the road. ")

option = input("Enter your Answer: ")

option = int(option)


if option == 1:
    print("Enter Terrorville, prepare for scary fun! Luckily you we out of the van, because it just exploded")

if option == 2:
        print("You've heard an deafening explosion, and you see fire, your car exploded and you died.")
        print("Bad End!")
        "break"
        
        
elif option == 3:
            print("You get lost outside and fall into a giant praying mantis pit, they eat you and you die.")
            print("Bad End!")
            "break"
            
decision = input("You enter Terrorville and see three places, 1) werewolf park,2) zombie plaza, 3) vampire diner:")
decision = int(decision)
if decision == 2:
        print("The zombie plaza was filled with friendly zombies who give you eyeball icecream (disguised vanilla flavor) and you explore futher for more adventure")   
    
    
            
            
            
if decision == 1:
                print(" You come face to face with the werewolf , Unlucky you, you didnt bring any silver so the werewolf eats you and you die.")
                print("Bad End!")
"break"
if decision == 3:
            print("The waitress comes and gives you some drink, Sadly, the waitress was a disguised count and the drink has sleep pills, you sleep and the vampire drink all your blood, turning you into a lifeless vampire .")
            print("Bad End!")
"break"            
  

#Libraries

import random

print("'Slappy'")

print("You were lucky to choose the opinion yourself, but now, its up to the coin to decide your fate.If you get heads, All my fellow monster will haunt you to leading to FTD, but if you get tails,you will be free and get a new car: ")

user_roll = random.randint(1,2)

user_roll = int(user_roll)

if user_roll == 1:

        print("You flipped heads")

        print("Bad End!")

"break"

if user_roll == 2:

            print("You flipped tails")

            print(" Hooray, you go back home with a new car!")
