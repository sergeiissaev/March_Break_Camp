print ("Hello there welcome to Medieval Village.")
print ("You have a village that you need to take care of. Choose one of the options to keep the village in good shape 1) Plant and harvest the crops 2) Use resources from the forest near the village 3) Get your defenses up")
user_choice = input()
user_choice = int(user_choice)

if user_choice == 1:
    print("You planted and harvested the crops!")
    print("Now choose from: 2) Use resources from the forest near the village or 3) Get your defenses up ")
    user_choice1 = input()
    user_choice1 = int(user_choice1)
    if user_choice1 == 2 :
        print("You used the resources in the forest.")
        print("Now 3) Get your defenses up")
        user_choice12 = input()
        user_choice12 = int(user_choice12)
        if user_choice12 == 3 :
            print("You got your defenses up! Your village holds strong agianst its invaders!")
            print("Your village is strong! You have nothing to worry about! Game over")
    elif user_choice1 == 3 :
        print("You got your defenses up! Your village holds strong agianst its invaders!")
        print("Now 2) Use resources from the forest near the village")
        user_choice13 = input()
        user_choice13 = int(user_choice13)
        if user_choice13 == 2:
            print("You used resources from the forest.")
            print("Your village is strong! You have nothing to worry about! Game over")

elif user_choice == 2 :
    print("You used the resources in the forest.")
    print("Now choose from: 1) Plant and harvest the crops or 3) Get your defenses up")
    user_choice2 = input()
    user_choice2 = int(user_choice2)
    if user_choice2 == 1:
        print("You harvested the crops!")
        print("Now 3) Get your defenses up")
        user_choice21 = input()
        user_choice21 = int(user_choice21)
        if user_choice21 == 3:
            print("You got your defenses up! Your village holds strong agianst its invaders!")
            print("Your village is strong! You have nothing to worry about! Game over")
    elif user_choice2 == 3:
        print("You got your defenses up! Your village holds strong agianst its invaders!")
        print("Now 1) Plant and harvest the crops")
        user_choice23 = input()
        user_choice23 = int(user_choice23)
        if user_choice23 == 1:
            print("You harvested the crops!")
            print("Your village is strong! You have nothing to worry about! Game over")

elif user_choice == 3:
    print("You got your defenses up! Your village holds strong agianst its invaders!")
    print("Now choose from: 1) Plant and harvest the crops or 2) Use resources from the forest near the village")
    user_choice3 = input()
    user_choice3 = int(user_choice3)
    if user_choice3 == 1:
        print("You harvested the crops!")
        print("Now 2) Use resources from the forest near the village")
        user_choice31 = input()
        user_choice31 = int(user_choice31)
        if user_choice31 == 2:
            print("You used resources from the forest near the village.")
            print("Your village is strong! You have nothing to worry about! Game over")
    elif user_choice3 == 2:
        print("You used resources from the forest near the village.")
        print("Now 1) Plant and harvest the crops")
        user_choice32 = input()
        user_choice32 = int(user_choice32)
        if user_choice32 == 1:
            print("You harvested the crops!")
            print("Your village is strong! You have nothing to worry about! Game over")

else :
    print ("Invalid entry try again!")
