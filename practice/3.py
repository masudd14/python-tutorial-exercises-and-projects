# from random import randint
# while True :
#     c=[]
#     i=1
#     a=randint(1,100)
#     # print(a)
#     while True :
#         b=int(input('guess the number '))
#         c.append(b)
#         if b==a :
#             print('right! ')
#             break
#         if len(c)!=1 :
#             if abs(a-b) < abs(a-c[-2])  :
#                 print('warmer! ')
#             else:
#                 print('colder! ')
#         else :
#             if abs(a-b)<=10 :
#                 print('warm!')
#             else :
#                 print('cold!')
#         i+=1
#     if i==1 :
#         print('congratulations you guessed the right number in one try! ')
#     else :    
#         print(f'i takes {i} times to guess the right number')
#     while True :
#         d=input('do you want to continue (y/n)? ').lower()
#         if d =='y' :
#             print('OK !')
#             break
#         elif d=='n' :
#             print('BYE ! ')
#             break
#         else :
#             print('pleas anwser with y/n ')
#             continue
#     if d=='n':
#          break

    










# from random import randint
# i=1
# b=None
# c=[]
# while True :
#     a=randint(1,100)
#     print(a)
#     while True :
#         b=int(input('guess the number '))
#         c.append(b)
#         print(c)
#         if b==a :
#             print('right!')
#             break
#         if len(c)!=1 :   
#             if abs(a-c[-1]) < abs(a-b) :
#                 print('colder!')
#             else :
#                 print('warmer!')
#         else :
#             if 100<b or b<0 :
#                 print('out of the bound')
#             elif abs((a-b))<=10 :
#                 print('warm!')
#             elif abs((a-b))>10  :
#                 print('cold!')
#         i=1+i
#     if i == 1 :
#         print('congratulation, you guess the right number in only one try  ')
#         break
#     else :
#         print(f'i takes {i} times to guess the right number')
#         break



from random import randint
while True:
    a=randint(1,100)
    print(a)
    d=[]
    i=1
    while True:
        while True :
            b=input("enter the number: ")
            if b.isdigit():
                if int(b) in  range(1,101):
                    break
                else:
                    print("enter a number in range 1,100")
                    continue
            else:
                print("please enter number")
                continue
        c=int(b)
        d.append(c)
        if a==c:
            if i==1:
                print("right, you guess the number in only one time")
            else: 
                print(f'it takes {i} times to guess the right number')
            break
        else:
            if len(d)==1:
                if abs(a-c)>10:
                    print("cold")
                elif abs(a-c)<10:
                    print("warm")
            elif len(d)!=1:
                if abs(a-d[-1])>abs(a-d[-2]):
                    print('colder')
                else:
                    print("warmer")
        i+=1
    while True:
        o=input("do you want to continue?(y/n) ").lower()
        if o=="y":
            print("ok")
            break
        elif o=="n":
            print("bye")
            break
        else:
            print("please answer with y or n")
    if o=='n':
        break