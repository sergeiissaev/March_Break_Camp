import sys
health=100
print ('Welcome to the Computer Trivia!!!!!!!!!!!')
print ()
print ('You have 100 health. For each question you get correct you get +50 health,')
print ('for each incorrect question, you will lose 60 health. The max health you can')
print ('get is 500 health. If you have 0 health then GAME OVER!! And you cant use any')
print (' search engine for eg. Bing, Google, etc. You cant do an invalid choice or the')
print (' game will be over. Good Luck player')
#Question 1
user_input= input('Do you want to play(1) or quit(2)?:  ')
if user_input=='1':
    print('Get ready for the 1st question!')
    print ()
    q1= input('''What storage device has a disk that spins?
(1)HDD (2) SSD (3)Flash Storage:  ''')
    if q1=='1':
        print ('CORRECT. You get +50 health')
        health+=50
        print ('Your health is', health)
    elif q1=='2':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
    elif q1=='3':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
    else:
        print ('INVALID ENTRY, BYE')
        sys.exit()
elif user_input=='2':
    print ('Your health is:',health)
    print ('BYE')
    sys.exit()
else:
    print ('INVALID ENTRY, BYE')
    sys.exit()
#QUESTION 2
print()
user_input= input('Do you want to play(1) or quit(2)?:  ')
if user_input=='1':
    print('Get ready for the 2nd question!')
    print ()
    q1= input('''What does the motherboard do?
(1)Removes Malvare (2) It passes electricity from one component to another (3)It Is a Storage Device:  ''')
    if q1=='2':
        print ('CORRECT. You get +50 health')
        health+=50
        print ('Your health is', health)
    elif q1=='1':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    elif q1=='3':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    else:
        print ('INVALID ENTRY, BYE')
        sys.exit()
elif user_input=='2':
    print ('Your health is:',health)
    print ('BYE')
    sys.exit()
else:
    print ('INVALID ENTRY, BYE')
    sys.exit()
#QUESTION 3
print()
user_input= input('Do you want to play(1) or quit(2)?:  ')
if user_input=='1':
    print('Get ready for the 3rd question!')
    print ()
    q1= input('''What is Trojan?
(1)It is a storage device (2)It is a hardware component (3)It is a Computer Virus:  ''')
    if q1=='3':
        print ('CORRECT. You get +50 health')
        health+=50
        print ('Your health is', health)
    elif q1=='1':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    elif q1=='2':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    else:
        print ('INVALID ENTRY, BYE')
        sys.exit()
elif user_input=='2':
    print ('Your health is:',health)
    print ('BYE')
    sys.exit()
else:
    print ('INVALID ENTRY, BYE')
    sys.exit()
#QUESTION 4
print()
user_input= input('Do you want to play(1) or quit(2)?:  ')
if user_input=='1':
    print('Get ready for the 4th question!')
    print ()
    q1= input('''What kind of storage do phones use?
(1)Floppy Disk (2)CD storage (3)Flash Storage:  ''')
    if q1=='3':
        print ('CORRECT. You get +50 health')
        health+=50
        print ('Your health is', health)
    elif q1=='1':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    elif q1=='2':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    else:
        print ('INVALID ENTRY, BYE')
        sys.exit()
elif user_input=='2':
    print ('Your health is:',health)
    print ('BYE')
    sys.exit()
else:
    print ('INVALID ENTRY, BYE')
    sys.exit()
#QUESTION 5
print()
user_input= input('Do you want to play(1) or quit(2)?:  ')
if user_input=='1':
    print('Get ready for the 5th question!')
    print ()
    q1= input('''What kind of operating system is Android, or IOS?
(1)DOS (2)LINUX (3)UNIX:  ''')
    if q1=='2':
        print ('CORRECT. You get +50 health')
        health+=50
        print ('Your health is', health)
    elif q1=='1':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    elif q1=='3':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    else:
        print ('INVALID ENTRY, BYE')
        sys.exit()
elif user_input=='2':
    print ('Your health is:',health)
    print ('BYE')
    sys.exit()
else:
    print ('INVALID ENTRY, BYE')
    sys.exit()
#QUESTION 6
print()
user_input= input('Do you want to play(1) or quit(2)?:  ')
if user_input=='1':
    print('Get ready for the 6th question!')
    print ()
    q1= input('''What kind of operating system is UBUNTU?
(1)QDOS (2)UNIX (3)LINUX:  ''')
    if q1=='3':
        print ('CORRECT. You get +50 health')
        health+=50
        print ('Your health is', health)
    elif q1=='1':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    elif q1=='2':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    else:
        print ('INVALID ENTRY, BYE')
        sys.exit()
elif user_input=='2':
    print ('Your health is:',health)
    print ('BYE')
    sys.exit()
else:
    print ('INVALID ENTRY, BYE')
    sys.exit()
#QUESTION 7
print()
user_input= input('Do you want to play(1) or quit(2)?:  ')
if user_input=='1':
    print('Get ready for the 7th question!')
    print ()
    q1= input('''(Fill in the blank) Kali __ is an OS used for hacking?
(1)MSDOS (2)LINUX (3)UNIX:  ''')
    if q1=='2':
        print ('CORRECT. You get +50 health')
        health+=50
        print ('Your health is', health)
    elif q1=='3':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    elif q1=='1':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    else:
        print ('INVALID ENTRY, BYE')
        sys.exit()
elif user_input=='2':
    print ('Your health is:',health)
    print ('BYE')
    sys.exit()
else:
    print ('INVALID ENTRY, BYE')
    sys.exit()
#QUESTION 8
print()
user_input= input('Do you want to play(1) or quit(2)?:  ')
if user_input=='1':
    print('Get ready for the 8th question!')
    print ()
    q1= input('''What does Trojan do?
(1)It helps remove malware (2)It hacks your computer and encrypts your files (3)It is an antivrus:  ''')
    if q1=='2':
        print ('CORRECT. You get +50 health')
        health+=50
        print ('Your health is', health)
        print ('YOU WIN WITH', health, 'HEALTH')
    elif q1=='3':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    elif q1=='1':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    else:
        print ('INVALID ENTRY, BYE')
        sys.exit()
elif user_input=='2':
    print ('Your health is:',health)
    print ('BYE')
    sys.exit()
else:
    print ('INVALID ENTRY, BYE')
    sys.exit()
#QUESTION 9
print()
user_input= input('Do you want to play(1) or quit(2)?:  ')
if user_input=='1':
    print('Get ready for the 9th question!')
    print ()
    q1= input('''Is windows 10 more secure than Linux?
(1)Yes (2)No (3)They both are same:  ''')
    if q1=='1':
        print ('CORRECT. You get +50 health')
        health+=50
        print ('Your health is', health)
        print ('YOU WIN WITH', health, 'HEALTH')
    elif q1=='3':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    elif q1=='2':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    else:
        print ('INVALID ENTRY, BYE')
        sys.exit()
elif user_input=='2':
    print ('Your health is:',health)
    print ('BYE')
    sys.exit()
else:
    print ('INVALID ENTRY, BYE')
    sys.exit()
#QUESTION 10
print()
user_input= input('Do you want to play(1) or quit(2)?:  ')
if user_input=='1':
    print('Get ready for the 10th question!')
    print ()
    q1= input('''What is LINUX based on?
(1)MSDOS (2)UNIX (3)QDOS:  ''')
    if q1=='2':
        print ('CORRECT. You get +50 health')
        health+=50
        print ('Your health is', health)
        print ('YOU WIN WITH', health, 'HEALTH')
    elif q1=='3':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    elif q1=='1':
        print ('INCORRECT You get -60 health')
        health-=60
        print ('You have', health, 'health')
        if health<=0:
            print ('GAME OVER')
            sys.exit()
    else:
        print ('INVALID ENTRY, BYE')
        sys.exit()
elif user_input=='2':
    print ('Your health is:',health)
    print ('BYE')
    sys.exit()
else:
    print ('INVALID ENTRY, BYE')
    sys.exit()
