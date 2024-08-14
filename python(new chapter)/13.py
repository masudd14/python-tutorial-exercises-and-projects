import functools,time
# def say_hello(name):
#     return f'hi {name}'

# def great(fun):
#     return fun('masud')

# print(great(say_hello))

# aa=say_hello
# aa1= lambda x : x+1

# print(say_hello('masud1'))
# print(aa('masud2'))
# print(aa1(4))

# def parents():
#     print('parents are speaking')
#     def first_child():
#         print('first child is speaking')
#     def second_child():
#         print('second child is speaking')
#     second_child()
#     first_child()

# parents()

# def parents2(num):
#     def first_child():
#         return 'first child is speaking'
#     def second_child():
#         return 'second child is speaking'
#     if num==1:
#         return second_child
#     else:
#         return first_child

# A=parents2(1)
# B=parents2(2)
# print(A())
# print(B())

# def a(func):
#     def b():
#         print('before')
#         func()
#         print('after')
#     return b

# def say_whee():
#     print('wheee!')

# def say_yoo():
#     print('yooo!')

# bb=a(say_whee)
# bb()
# say_yoo=a(say_yoo)
# say_yoo()

# from datetime import datetime

# def night(func):
#     def ccc():
#         '''doc string must be writen if you want to be shown in help;'''
#         if 7<= datetime.now().hour <= 22:
#             func()
#         else:
#             print('go to bed!')
#     return ccc

# @night
# def say_poo():
#     print('pooo!')

# from decoratrors import my_deco

# @my_deco
# def goo(name):
#     print('creating greeting')
#     return f'goooo {name}!'

# print(goo('masud'))

# print(len.__name__)
# help(print)

# print(say_poo)
# print(say_poo.__name__)
# help(say_poo)

# print(goo)
# print(goo.__name__)
# help(goo)

# import decoratrors

# class timewaster:
#     @decoratrors.debug
#     def __init__(self, maxnum):
#         self.maxnum=maxnum
#     @decoratrors.timer
#     def wate_time(self,numtimes):
#         for _ in range (numtimes):
#             sum([i**2 for i in range(numtimes)])

# tw=timewaster(1000) 
# tw.wate_time(999)

# @decoratrors.timer
# class timewaster2:
#     def __init__(self, maxnum):
#         self.maxnum=maxnum
#     def wate_time(self,numtimes):
#         for _ in range (numtimes):
#             sum([i**2 for i in range(numtimes)])
# tw2=timewaster2(1000) 
# tw2.wate_time(999)

# @decoratrors.debug
# @decoratrors.slow_down
# def great(name):
#     print(f'{name} hi !')
# great('masud')

# def repeat(num_times):
#     def decorator_repeat(func):
#         '''this is a test'''
#         @functools.wraps(func)
#         def wrapper_repeat(*args,**kwargs):
#             for i in range(num_times):
#                 func(*args,**kwargs)
#             return func(*args,**kwargs)
#         return wrapper_repeat
#     return decorator_repeat

# @repeat(5)
# def great2(name):
#     print(f'HELLO {name} !')
# great2('masud')

# def count(func):
#     '''this is a test'''
#     @functools.wraps(func)
#     def wrapper_count(*args,**kwargs):
#         wrapper_count.num_calls+=1
#         print(f'{func.__name__} has ran {wrapper_count.num_calls} times')
#         return func(*args,**kwargs)
#     wrapper_count.num_calls=0
#     return wrapper_count

# @count
# def say_whatup():
#     print('what up!')
# say_whatup()
# say_whatup()
# say_whatup()
# print(say_whatup.num_calls)

# class conter:
#     def __init__(self, start=0):
#         self.count= start
#     def __call__(self):
#         self.count+=1
#         print(f'count is {self.count}')
# A=conter()
# A()
# A()
# A()

# class counter:
#     def __init__(self,func):
#         functools.update_wrapper(self,func)
#         self.count=1
#         self.func=func
#     def __call__(self,*args,**kwargs):
#         print(f'count is {self.count}') 
#         self.count+=1
#         return self.func(*args,**kwargs)
    
# @counter
# def say_whatup():
#     print('what up!')

# say_whatup()
# say_whatup()