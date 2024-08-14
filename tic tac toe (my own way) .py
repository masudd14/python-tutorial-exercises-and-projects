from random import randint
list=['   ','   ','   ']
list2=['   ','   ','   ']
list3=['   ','   ','   ']
print('[0,1,2]\n[3,4,5]\n[6,7,8]')
while True :
    def change():
        global a
        global b 
        global c
        global d
        def input1() :
            global a
            global b 
            global c
            global d
            while True:
                a=input('enter a number(player 1): ')
                if a.isdigit() :
                    if int(a) in range(0,3) :
                        print('good! ')
                        b=int(a)
                        c=100
                        d=100
                        break
                    elif int(a) in range(3,6):
                        print('good! ')
                        c=int(a)
                        b=100
                        d=100
                        break
                    elif int(a) in range(6,9):
                        print('good! ')
                        d=int(a)
                        b=100
                        c=100
                        break
                    else: #int(a) not in range(0,11):
                        print('the number that you enterd is not available')
                else: #not a.isdigit() :
                    print('intiger number!!!!!!!!!!!  ')
        input1()
        if b in range (0,3):
            if list[b] !=' x ' :
                list[b]=' o '
            else:
                print('you can not put anything there')
        elif c in range(3,6):
            c-=3
            if list2[c] !=' x ' :
                list2[c]=' o '
            else:
                print('you can not put anything there')                
        elif d in range(6,9):
            d-=6
            if list3[d] !=' x ':
                list3[d]=' o '
            else:
                print('you can not put anything there')
        print(list)
        print(list2)
        print(list3)
    change()
    def change1():
        global a
        global b 
        global c
        global d
        def input1() :
            global a
            global b 
            global c
            global d
            while True:
                a=input('enter a number (player 2): ')
                if a.isdigit() :
                    if int(a) in range(0,3) :
                        print('good! ')
                        b=int(a)
                        c=100
                        d=100
                        break
                    elif int(a) in range(3,6):
                        print('good! ')
                        c=int(a)
                        b=100
                        d=100
                        break
                    elif int(a) in range(6,9):
                        print('good! ')
                        d=int(a)
                        b=100
                        c=100
                        break
                    else: #int(a) not in range(0,11):
                        print('the number that you enterd is not available')
                else: #not a.isdigit() :
                    print('intiger number!!!!!!!!!!!  ')
        input1()
        if b in range (0,3):
            if list[b] !=' o ':
                list[b]=' x '
            else:
                print('you can not put anything there')
        elif c in range(3,6):
            c-=3
            if list2[c] !=' o ':
                list2[c]=' x '
            else:
                print('you can not put anything there')                
        elif d in range(6,9):
            d-=6
            if list3[d] !=' o ' :
                list3[d]=' x '
            else:
                print('you can not put anything there')
        print(list)
        print(list2)
        print(list3)
    change1()
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
    
###############################################################################

# def input1() :
#     while True:
#         a=input('enter a number(player 1): ')
#         if a.isdigit() :
#             if int(a) in range(0,3) :
#                 print('good! ')
#                 b=int(a)
#                 c=100
#                 d=100
#                 return b
#             elif int(a) in range(3,6):
#                 print('good! ')
#                 c=int(a)
#                 b=100
#                 d=100
#                 return c
#             elif int(a) in range(6,9):
#                 print('good! ')
#                 d=int(a)
#                 b=100
#                 c=100
#                 return d
#             else: #int(a) not in range(0,11):
#                 print('the number that you enterd is not available')
#         else: #not a.isdigit() :
#             print('intiger number!!!!!!!!!!!  ')
# # aa=input1()

# def change(h):
#     if h in range (0,3):
#         if list[h] !=' x ' :
#             list[h]=' o '
#         else:
#             print('you can not put anything there')
#     elif h in range(3,6):
#         h-=3
#         if list2[h] !=' x ' :
#             list2[h]=' o '
#         else:
#             print('you can not put anything there')                
#     elif h in range(6,9):
#         h-=6
#         if list3[h] !=' x ':
#             list3[h]=' o '
#         else:
#             print('you can not put anything there')
#     print(list)
#     print(list2)
#     print(list3)
# # change(aa)

# def input2() :
#     while True:
#         a=input('enter a number(player 2): ')
#         if a.isdigit() :
#             if int(a) in range(0,3) :
#                 print('good! ')
#                 b=int(a)
#                 c=100
#                 d=100
#                 return b
#             elif int(a) in range(3,6):
#                 print('good! ')
#                 c=int(a)
#                 b=100
#                 d=100
#                 return c
#             elif int(a) in range(6,9):
#                 print('good! ')
#                 d=int(a)
#                 b=100
#                 c=100
#                 return d
#             else: #int(a) not in range(0,11):
#                 print('the number that you enterd is not available')
#         else: #not a.isdigit() :
#             print('intiger number!!!!!!!!!!!  ')
# # bb=input2()

# def change2(h):
#     if h in range (0,3):
#         if list[h] !=' o ' :
#             list[h]=' x '
#         else:
#             print('you can not put anything there')
#     elif h in range(3,6):
#         h-=3
#         if list2[h] !=' o ' :
#             list2[h]=' x '
#         else:
#             print('you can not put anything there')                
#     elif h in range(6,9):
#         h-=6
#         if list3[h] !=' o ':
#             list3[h]=' x '
#         else:
#             print('you can not put anything there')
#     print(list)
#     print(list2)
#     print(list3)
# # change2(bb)

# while True:
#     i=0
#     d=''
#     list=['   ','   ','   ']
#     list2=['   ','   ','   ']
#     list3=['   ','   ','   ']
#     print('[0,1,2]\n[3,4,5]\n[6,7,8]')
#     while True:
#         while i!=0:
#             d=input('do you want to continue (y/n)? ').lower()
#             if d =='y' :
#                 print('OK !')
#                 break
#             elif d=='n' :
#                 print('BYE ! ')
#                 break
#             else :
#                 print('pleas anwser with y/n ')
#                 continue
#         if d=='n':
#             break
#         i+=1
#         aa=input1()
#         change(aa)
#         bb=input2()
#         change2(bb)
#     if d=='n':
#             break