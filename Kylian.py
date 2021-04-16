choice = 1
choice1 = 2


import time

print("you woke up")

time.sleep(1)

print("10:00 a.m")

time.sleep(2)

print("you don't remember what happen!")

time.sleep(2)

print("you are hungry but have nothing to eat.")
time.sleep(2)
num1 = input("(1)you see a bird and try to catch it,(2) you try to eat some fruits that fell on the ground.")
num1 = int(num1)


time.sleep(2)
if num1 == 2:
    print("you eat a half eaten mango on the ground and suddenly start vomitting...in some hours you die.")
   
if num1 == 1:
    print("while you were trying to catch it, you fell into a ditch and found some abandoned camping site and find some food to eat. ")
    time.sleep(2)
    print("you are done eating and you try to find a shelter.")
    time.sleep(2)
    num2 = input("(1)try to find wood to make a shelter on the trees or (2) you decide to stay in the camp.")
   
    num2 = int(num2)
   
time.sleep(2)
if num2 == 1:
    print("while building your treehouse you fell and broke your neck...you die on the spot.")
if num2 == 2:
    print("while searching the camp, you find a shed in good shape and some more resources.")
    time.sleep(2)
    print("8:00 p.m")
    time.sleep(2)
num3 = input("(1)you go for a good night sleep or (2) try and hunt for more resources.")

num3 = int(num3)

time.sleep(2)

if num3 == 1:
    print("your she collapses during the night, you start to bleed.")
    time.sleep(2)
   
    print("12:00 a.m")
   
    time.sleep(2)
   
    print("you die of blood loss.")
   

if num3 == 2:
    print("you manage to capture a deer and return home")
    time.sleep(2)
    print("1:00 a.m")
    time.sleep(2)
    print("you arive and you find your shed on the ground, you save all the recources and spend the night in the main tent.")
    time.sleep(2)
    print("you wake up")
    time.sleep(2)
    print("9:00 a.m")
    time.sleep(2)
    print("you decide to mave after what happened that night.")
    time.sleep(2)
    num4 = input("(1) you try to follow a river or(2) follow the sun.")

num4 = int(num4)

if num4 == 1:
    print("you find a village, you are saved")
   
   
if num4 == 2:
    print("while looking at the sun you become blind and walk insadi a lion's den...you were there for dinner.")
