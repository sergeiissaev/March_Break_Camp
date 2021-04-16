print("10 fun trivia questions!")
I = input ("If ready to answer all questions enter yes: ")
score = 0
totalP = 10


if I == "yes":
    I = input(" 1) How many legs does a spider have: ")
    if I == "8":
        print("correct")
        score = score + 1
        print ("Your score is", score)
    else:
        print ("incorrect")
        score = 0
        print("Your score is", score)
else:
    print("Alright then, bye I guess.")
    quit()

print("")    

planets = input("2) How many planets are in the solar system: ")
if planets == "8":
    print("correct")
    score = score + 1
    print ("Your score is", score) 
else:
    print ("incorrect")
    score = score - 1
    print("Your score is", score)

print("")   
    
p = input("3) What color is the maple leaf on the canadian flag: ")
if p == "red":
    print("correct")
    score = score + 1
    print ("Your score is", score) 
else:
    print ("incorrect")
    score = score - 1
    print("Your score is", score)
    
print("")   
    
v = input("4) Which movie is Elsa in: ")
print("You input is", v)
if v == "Frozen" or v == "frozen":
    print("correct")
    score = score + 1
    print ("Your score is", score) 
else:
    print ("incorrect")
    score = score - 1
    print("Your score is", score)

print("")
    
o = input("5) Which Dutch artist painted “Girl with a Pearl Earring”?: ")
if o == "Vermeer" or o == "vermeer":
    print("correct")
    score = score + 1
    print ("Your score is", score) 
else:
    print ("incorrect")
    score = score - 1
    print("Your score is", score)
    
print("")
    
n = input("6) What is the rarest M&M color: ")
if n == "Brown" or n == "brown":
    print("correct")
    score = score + 1
    print ("Your score is", score) 
else:
    print ("incorrect")
    score = score - 1
    print("Your score is", score)    
    
print("")
    
q = input("7) In which European city would you find Orly airport: ")
if q == "Paris" or q == "paris":
    print("correct")
    score = score + 1
    print ("Your score is", score) 
else:
    print ("incorrect")
    score = score - 1
    print("Your score is", score)    
 
print("")
    
e = input("8) Which country consumes the most chocolate per capita: ")
if e == "Switzerland":
    print("correct")
    score = score + 1
    print ("Your score is", score) 
else:
    print ("incorrect")
    score = score - 1
    print("Your score is", score) 
    
print("")
    
w = input("9) Which of Shakespeare’s plays is the longest: ")
if w == "Hamlet":
    print("correct")
    score = score + 1
    print ("Your score is", score) 
else:
    print ("incorrect")
    score = score - 1
    print("Your score is", score)    
 
print("")
    
a = input("10) In what year were the first Air Jordan sneakers released: ")
if a == "1984":
    print("correct")
    score = score + 1
    print ("Your score is", score) 
else:
    print ("incorrect")
    score = score - 1
    print("Your score is", score) 
    
print ("Thanks for playing!")
