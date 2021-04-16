print("You wake up, your eyes are blurry but you see two hazy outlines talking.")
opt_1 = int(input("Your 2 options are 1. you ask where you are or 2. stay still and listen to what the people are saying"))


if(opt_1 == 1):

    print("The people know magic and cast a spell for you to stop talking forever, and you run away as fast as you can")
   
    opt_2 = int(input("1. You find an old kind man who is willing to help you or 2. you can travel on ship away to another place"))
    if (opt_2 == 1):
        print("The old kind man takes you to anither village where you are safe and eventually go home. You win.")

    else:
        print("Invalid Entry picking random choice")

else:
    print("Invalid Entry picking random choice")

    opt_2 = int(input("You end on a cliff, 1.you can either work for the bad people who are chasing you or 2. You can jump into the water and swim away"))
if (opt_2 == 1):
        print("The people eventally kill you and you die. Game over.")
if (opt_2 == 2):
        print("You find a safe village on the end of the other side, where villagers are willing to help you. You win.")
