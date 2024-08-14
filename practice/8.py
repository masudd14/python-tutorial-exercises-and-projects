# try :
#     for i in ['a','b','c']:
#         print(i**2)
# except TypeError:
#     print('you can not use power for str ! ')


# x=5
# y=0
# try:
#     z=x/y
# except ZeroDivisionError as er:
#     print('can not be done !')
#     print(er)
# else:
#     print('all done !')
# finally:
#     print('end of the trying process. ')


# def ask():
#     while True:
#         try:
#             b=int(input('enter an intiger : '))
#         except:
#             print('you did not enter an intiger!!! ')
#             continue
#         else:
#             print('good you entered an intiger. ')
#             break
#     print(b**2)
# ask()