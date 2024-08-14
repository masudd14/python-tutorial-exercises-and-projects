while True:
    pp=input('enter the first players name: ')
    pp2=input('enter second players name: ')
    while True:
        b=input(f'{pp} choose a number between 1 to 3 (1_paper,2_rock,3_scissor) : ')
        if b.isdigit():
            if int(b) in range(1,4):
                b=int(b)
                break
            else:
                print('enter a number between 1 to 3 ')
                continue
        else:
            print('enter number')
            continue
    # while True:
    #     c=input(f'{pp2} choose a number between 1 to 3 (1_paper,2_rock,3_scissor) : ')
    #     if c.isdigit():
    #         if int(c) in range(1,4):
    #             c=int(c)
    #             break
    #         else:
    #             print('enter a number between 1 to 3 ')
    #             continue
    #     else:
    #         print('enter number')
    import random
    comuter=[1,2,3]
    c= random.choice(comuter)
    print(c)

    if (b==1 and c==2) or (b==2 and c==3) or (b==3 and c==1):
        print(f'{pp} wins ! ')
    elif (c==1 and b==2) or (c==2 and b==3) or (c==3 and b==1):
        print(f'{pp2} wins ! ')
    else:
        print('draw ! ')
    while True :
        d=input('do you want to continue (y/n)? ').lower()
        if d =='y' :
            print('OK !')
            break
        elif d=='n' :
            print('BYE ! ')
            break
        else :
            print('pleas anwser with y/n ')
            continue
    if d=='n':
        break

import random
comuter=[1,2,3]
c= random.choice(comuter)
# print(comuter_choice)