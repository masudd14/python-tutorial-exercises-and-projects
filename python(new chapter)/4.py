# def list1(get_list): print(get_list)


# def input1() : 
#     while True:
#         a=input('enter a number: ')
#         if a.isdigit() :
#             print('good! ')
#             return int(a)
#         else:
#             print('intiger number!!!!!!!!!!!  ')
#             continue
# print(input1())


# def input1() : 
#     while True:
#         a=input('enter a number: ')
#         if a.isdigit() :
#             if int(a) in range(0,11) :
#                 print('good! ')
#                 return int(a)
#             else: #int(a) not in range(0,11):
#                 print('the number that you enterd is not available')
#         else: #not a.isdigit() :
#             print('intiger number!!!!!!!!!!!  ')
# print(input1())

# def change():
#     global a
#     global b 
#     global c
#     global d
#     list=['','','']
#     list2=['','','']
#     list3=['','','']
#     def input1() :
#         global a
#         global b 
#         global c
#         global d
#         while True:
#             a=input('enter a number: ')
#             if a.isdigit() :
#                 if int(a) in range(0,3) :
#                     print('good! ')
#                     b=int(a)
#                     c=100
#                     d=100
#                     break
#                 elif int(a) in range(3,6):
#                     print('good! ')
#                     c=int(a)
#                     b=100
#                     d=100
#                     break
#                 elif int(a) in range(6,9):
#                     print('good! ')
#                     d=int(a)
#                     b=100
#                     c=100
#                     break
#                 else: #int(a) not in range(0,11):
#                     print('the number that you enterd is not available')
#             else: #not a.isdigit() :
#                 print('intiger number!!!!!!!!!!!  ')
#     input1()
#     print(a)
#     if b in range (0,3):
#         list[b]=0
#     elif c in range(3,6):
#         c-=3
#         list2[c]=0
#     elif d in range(6,9):
#         d-=6
#         list3[d]=0
#     print(list)
#     print(list2)
#     print(list3)
# change()