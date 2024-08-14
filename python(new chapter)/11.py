# print(0 /0 ))
#print(0 /0 )

# x=10
# if x>5:
#     raise Exception(f'x should not exceed 5 the value of x is {x}')

# import sys
# assert ('linux' in sys.platform), 'this code runs only on linux'
# print(sys.platform)

# x=5
# assert (x==10), f'the value of x is {x}'

# import sys
# def linux():
#     assert ('linux'==sys.platform), 'your platform is not linux'
#     print('ok you are using linux')

# try:
#     linux()
#     print('ok')
# except AssertionError as error:
#     print(error)
#     print('something wnet wronge !!')

# print('end of the program !!')

# try:
#     with open('sss') as file:
#         read_data= file.read()
#     print('succesfull')
# except FileNotFoundError as pp:
#     print(pp)
#     print('could not open file')
# print('goes on !!')     


# def fun():
#     x=5
#     assert (x==10), f'the value of x is {x}'

# try :
#     fun()
#     with open('asd') as file:
#         read_data=file.read()
#     print('ok')
# except AssertionError as error:
#     print(error)
#     print('something went wronge')
# except FileNotFoundError as pp :
#     print(pp)
#     print('Error !!')


# try :
#     with open('asd') as file:
#         read_data=file.read()
#     fun()
#     print('ok')
# except AssertionError as error:
#     print(error)
#     print('something went wronge')
# except FileNotFoundError as pp :
#     print(pp)
#     print('Error !!')

# print('still goes on')


# import sys
# def win():
#     assert ('win32'==sys.platform) ,'you are not using windows'

# try :
#     win()
# except AssertionError:
#     print('change you platform to use this funiction')
# else:
#     print('you are using windows, the funiction is avarible for you')
#     try:
#         with open('gw') as file :
#             read_data=file.read()
#     except FileNotFoundError:
#         print('file not found')
#     else:
#         print('opening ...')
# finally:
#     print('end of the teying process')


# def askint():
#     while True:
#         try :
#             a=int(input('enter an intiger : '))
#         except :
#             print('the input was not digit ') 
#             continue
#         else:
#             print('ok, the input was digit GOOD!')
#             break
#         finally:
#             print('end of the teying process')
#     print(a)
# askint()


# import pylint
# pylint.run_pylint(['G:\\projects\\python(new chapter)\\test.py'])

# import unittest
# import test2

# class testcap(unittest.TestCase):
#     def test_one_word(self):
#         test='python'
#         # result=test2.cap_text(test)
#         self.assertEqual(test2.cap_text('test'),'tt')
#     def several_word(self):
#         test1='hi python'
#         result1=test2.cap_text(test1)
#         self.assertEqual(result1,'Hi Python')   

# if __name__=='__main__':
#     unittest.main()