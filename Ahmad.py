
print('Hello, welcome to Trivia!')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. What is my favourite video game? ')
    if ans.lower() == 'minecraft':
        score+= 1
       
        print('Correct')
    else:
        print('Incorrect, The answer was minecraft!')

    ans = input('2. What is 90 * 8 + 7 - 184? ')
    if ans.lower() == '543':
        score += 1
        print('Correct')

    else:
        print('Incorrect, The answer was 727!')

    ans = input('3. What is my favourite sport? ')

    if ans.lower() == 'badminton':
        score += 1
        print('Correct')

    else:
        print('Incorrect, The answer was badminton! ')
       
    ans = input('4. Who is the best soccer player? ')
   
    if ans.lower() == 'ronaldo':
        score += 1
        print('Correct')
       
    else:
        print('Incorrect, The answer was ronaldo!')

    ans = input('5. What is the best programming language? ')
    if ans.lower() == 'python':
        score += 1
        print('Correct')
       
    else:
        print('Incorrect, The answer was Python!')
       
    ans = input('6. Who is the worst presedant of America? ')
    if ans.lower() == 'donald trump' or ans.lower() == 'george bush':
        score += 1
        print('Correct')
       
    else:
        print('Incorrect, The answer was donald trump, or george bush!')
       
    ans = input('7. When did World war 1 begin? ')
    if ans.lower() == '1914':
        score += 1
        print('Correct')
       
    else:
        print('Incorrect, It was 1914!')
       
    ans = input('8. What is the largest river in the world? There are multipale answers')
    if ans.lower() == 'amazon river':
        score += 1
        print('Correct')
       
    else:
        print('Incorrect, The answer was amazon river!')

    ans = input('9. What is the most dangerous animal in the world? ')
    if ans.lower() == 'king cobra' or ans.lower() == 'scorpion' or ans.lower() == 'komodo dragon' or ans.lower() == 'box jelly fish' or ans.lower() == 'great white shark':
        score += 1
        print('Correct')
       
    else:
        print('Incorrect, The answer was king cobra, scorpion, komodo dragon, box jelly fish, and great white shark ')

    print('The last question is the hardest you can do it!')
    print()

    ans = input('10. What is the hardest game in the world? ')
    if ans.lower() == 'worlds hardest game':
        score += 5
        print('Correct, You got it!')
    else:
        print('Incorrect, The answer was worlds hardest game! ')
       
print('Thank you for playing, you got ', score, " questions correct.")
print()
mark = (score/total_q) * 100

print('Mark: ', str(mark) + '%')
print('Goodbye, Good luck next time!!')
