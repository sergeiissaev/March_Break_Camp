flag = True
dot = input("hi i'm guyman and i kidnapped you. you only have 3 things you can do to survive. type in 1 to hunt, 2 to hide and 3 to swim in the ocean.: ")
if dot == "1":
   print(" you hunted and you ate food so you are safe and not hungry")
elif dot == "2":
    flag = False
    print ("you hide and die of hunger")
elif dot == "3":
   flag = False
   print("you swam and you got eaten by a shark")
if flag == True:
   lot = input("  you know that there is a village west and you want to go there. type in 1 to live in the forest until the sun sets west, 2 to spend the rest of your life in the forest and 3 to walk around until you see a village: ")
if lot == "1":
   print("you found the village and decided to stay there")
elif lot == "2":
   flag = False
   print("you die because of the dangers of the forest")
elif lot == 3:
   flag = False
   print("you bump into a family of bears and die")
if flag == True:
    bot = input("The village is huge and it has electricity but the villagers don't know you arrived there. You call all the villagers and ask them if you could stay there and they said yes. They went to get water and you were alone. You have three choices to live your life. type in 1 to live with the vilagers for the rest of your life, 2 to tear down your house, loot the village and make a house 130 km away and type in 3 to go back to the forest: ")
if bot == "1":
    print("you spend the rest of your life normal")
elif bot == "2":
    print("you have the time of your life because you have everything the villagers owned and you have food to last 70 years")
elif bot == "3":
    flag = False
    print("you die because of the dangers of the forest")
if flag == True:
    print("you win and if you didn't like how your life ended replay the game")
else:
    print ("game over try again")
