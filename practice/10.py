import functools
from time import sleep
# def timer(func):
#     '''calculating wate of the time'''
#     @functools.wraps(func)
#     def wrapper_timer(*args,**kwargs):
#         o=(time.perf_counter())
#         u=func(*args,**kwargs)
#         o1=(time.perf_counter())
#         o1-=o
#         print(f'finished in : {o1 : 0.5f}')
#         return u
#     return wrapper_timer

# @timer
# def prime(num):
#     for _ in range(num):
#         sum([i**2 for i in range(999)])
# print(prime(999))


# def debug(func):
#     '''this is a decorator to debug the code'''
#     @functools.wraps(func)
#     def wrapper_debug(*args,**kwargs):
#         arg=[repr(a) for a in args]
#         dic=[f'{b!r}={c!r}' for b,c in kwargs.items()]
#         end=arg+dic
#         print(f"calling {func.__name__!r}({' , '.join(end)})")
#         p=func(*args,**kwargs)
#         print (f"{func.__name__!r} returned {p}")
#         return p
#     return wrapper_debug

# @debug
# def make_greeting(name, age=None):
#     if age!=None:
#         return f'whoa {name}! {age} already, you are growing up!'
#     else:
#         return f'whoa {name}!'
# print(make_greeting('Richard',age=112))
# print(make_greeting('masud'))

# import math

# math.factorial=debug(math.factorial)

# def ee(terms=18):
#     return sum(1 / math.factorial(a) for a in range(terms))
# print(ee(20))

# def slow_down(func):
#     '''this is a decorator to slow the prosses down'''
#     @functools.wraps(func)
#     def wrapper_slow_down(*args,**kwargs):
#         for i in range(5,0,-1):
#             print(f'{i} seccod remaining')
#             time.sleep(1)
#         func(*args,**kwargs)
#     return wrapper_slow_down

# @slow_down
# def test():
#     print('this is a test')
# test()

# def slowly(func):
#     '''this is a decorator to slow the prosses down'''
#     @functools.wraps(func)
#     def wrapper_slowly(*args,**kwargs):
#         time.sleep(2)
#         func(*args,**kwargs)
#     return wrapper_slowly

# @slowly
# def countdown(num):
#     if num < 1:
#         print('liftoof')
#     else:
#         print(num)
#         countdown(num-1) 
# countdown(10)

# def slow_it_down(_func=None,*,time_s=0):
#     def decorator_slow_it_down(func):
#         '''this is a doc str'''
#         @functools.wraps(func)
#         def wrapper_slow_it_down(*args,**kwargs):
#             for i in range(time_s,0,-1):    
#                 print(i)
#                 sleep(1)
#             return func(*args,**kwargs)
#         return wrapper_slow_it_down
#     if _func is None:
#         return decorator_slow_it_down
#     else: 
#         return decorator_slow_it_down(_func)

# @slow_it_down(time_s=3)
# def say_st():
#     print('something')

# say_st()

# def singleton(cls):
#     @functools.wraps(cls)
#     def wrapper_singleton(*args,**kwargs):
#         if not wrapper_singleton.instance:
#             wrapper_singleton.instance=cls(*args,**kwargs)
#         return wrapper_singleton.instance
#     wrapper_singleton.instance=None
#     return wrapper_singleton  

# @singleton
# class r:
#     pass

# S=r
# D=r
# print(id(S))
# print(id(D))
# print(S is D)

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
# def fibo(num):
#     if num < 2:
#         return num
#     return fibo(num-1)+fibo(num-2)
# print(fibo(10))

# def cache(func):
#     @functools.wraps(func)
#     def wrapper_cache(*args,**kwargs):
#         cache_key= args + tuple(kwargs.items())
#         if cache_key not in wrapper_cache.cache:
#             wrapper_cache.cache[cache_key]= func(*args,**kwargs)
#         return  wrapper_cache.cache[cache_key]
#     wrapper_cache.cache=dict()
#     return wrapper_cache

# @cache
# @count
# def fibo(num):
#     if num < 2:
#         return num
#     return fibo(num-1)+fibo(num-2)
# print(fibo(10))

# @functools.lru_cache(maxsize=4)
# def fibo(num):
#     if num < 2:
#         return num
#     print('..')
#     return fibo(num-1)+fibo(num-2)
# print(fibo(10))