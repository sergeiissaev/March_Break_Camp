print('whats sup peoples, this is a trivia about moi hehehe')

ans = input('do you want to play you wont regret it (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1 what is my top kpop group of all time? ')
    if ans.lower() == 'BTS':
        score+= 1
       
        print('good job')
    else:
        print('WRONG')

    ans = input('2 what shows do i like ')
    if ans.lower() == 'kakegurui,mlb,stranger things,riverdale,erased,':
        score += 1
        print('YES YOU DiD IT')

    else:
        print('WRONG!')

    ans = input('3. what video games do i like? ')

    if ans.lower() == 'minecraft,roblox,gacha life,gacha club':
        score += 1
        print('YAYA YOU GOT IT')

    else:
        print('WRONG! ')
       
    ans = input('4 what are my favourite music genres? ')
   
    if ans.lower() == 'kpop,hip hop,pop,chill':
        score += 1
        print('YOUR THE BEST')
       
    else:
        print('WRONG!')

    ans = input('5 what are my hobbies? ')
    if ans.lower() == 'editing,talking to friends,sleeping lol':
        score += 1
        print('YOUR VERY SMART')
       
    else:
        print('WRONG!')
       
    ans = input('6 who is the queen of rap? ')
    if ans.lower() == 'nicki manaj':
        score += 1
        print('YES')
       
    else:
        print('WRONG')
       
    ans = input('7. what grade am i in? ')
    if ans.lower() == 'grade 7':
        score += 1
        print('yes')
       
    else:
        print('WRONG')
       
   
       
print('wowowowowowowwo you made it to the end, you got ', score, " questions correct.")
print()
mark = (score/total_q) * 100

print('Mark: ', str(mark) + '%')
print('yeeet bai yall!!')
