# def g_square(n):
#     for i in range(1,n+1):
#         yield i**2
# for x in g_square(10):
#     print(x)


# from random import randint
# def g_randint(mini,maxi,n):
#     for _ in range(n):
#         yield randint(mini,maxi)
# for x in g_randint(1,10,12):
#     print(x)


# s='hello'
# a=iter(s)
# print(next(a))
# print(next(a))
# print(next(a))


# my_list=[1,2,3,4,5]
# ge=(item for item in my_list if item>3)
# for x in ge:
#     print(x)