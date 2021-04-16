print("Hi! This is a trivia game. For each question, type in the correct answer.")
print(" ")
p=0

user=input("What is the capital of New Zealand? ")
if (user=="Wellington" or user=="wellington"):
    print("CORRECT! 1 point!")
    p=p+1
else:
    print("WRONG! Answer is Wellington.")
print(" ")


user2=input("TRUE OR FALSE : The flag of Mauritius has 3 colours. ")
if (user2=="False" or user2=="false"):
    print("CORRECT! 1 point!")
    p=p+1
else:
    print("WRONG! Answer is False.")
print(" ")


user3=input("Who invented the first computer? ")
print(user3.lower())
if (user3.lower()=="charles" or user3.lower()=="babbage" or user3.lower()=="charles babbage"):
    print("CORRECT! 1 point!")
    p=p+1
else:
    print("WRONG! Answer is Charles Babbage.")
print(" ")

user4=input("how many noses does a snail have? ")
if (user4=="4" or user4=="four"):
    print("CORRECT! 1 point!")
    p=p+1
else:
    print("WRONG! Answer is 4.")
print(" ")
user5 = input("Who was the first person to land on the moon?  ")
print(user5.lower())
if (user5.lower()=="neil" or user5.lower()=="armstrong" or user5.lower()=="neil armstrong"):
    print("CORRECT! 1 point!")
    p=p+1
else:
    print("WRONG! Answer is Neil Armstrong")
print(" ")
if p<3:
    print("Better luck next time! You got",p,"out of 5.")
else:
    print("Good job! You got",p,"out of 5.")
