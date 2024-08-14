# def cube(num):
#     l=[]
#     for i in range(num):
#         l.append(i**3)
#     return l

# def gen_cube(num):
#     for i in range(num):
#         yield i**3
#         print(i)

# h=gen_cube(10)
# print(next(h))
# print(next(h))
# print(next(h))
# print(next(h))
# print([*h])

# def gen_fibo(num):
#     a=1
#     b=1
#     for i in range(num):
#         yield a
#         a,b=b,a+b

# ac=[a**3 for a in range(10)]
# ag=(a**3 for a in range(10))

# print(ac)
# print(next(ag))
# print(next(ag))
# print(next(ag))
# print(next(ag))
# print(next(ag))

# import sys
# print(sys.getsizeof((a**3 for a in range(1000))))
# print(sys.getsizeof([a**3 for a in range(1000)]))

# import cProfile
# cProfile.run('sum((a**3 for a in range(1000)))')
# cProfile.run('sum([a**3 for a in range(1000 )])')

# def g():
#     while True:
#         x = yield
#         print(x)
# g1=g()
# print(next(g1))
# g1.send(10)
# print(next(g1))

# def gg():
#     try:
#         while True:
#             x = yield
#             print(x)
#     except ValueError:
#         print('stopped !')
# g2=gg()
# print(next(g2))
# g2.send(3)
# g2.throw(ValueError)

# def ggg():
#     try:
#         while True:
#             x = yield
#             print(x)
#     except GeneratorExit:
#         print('closed ! ')    
# g3=ggg()
# print(next(g3))
# g3.close()