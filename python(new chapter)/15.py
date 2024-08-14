# temps=[0,33.5,40,100]
# F_temps= map(lambda x : (9/5)* x + 32 ,temps)
# for x in F_temps:
#     print(x)

# print([*map(lambda x , y : x +y, [1,2,3,4],[5,6,7,8])])

# print([*map(lambda x , y : x +y, [1,2,3,4],[5,6,7])])

# from functools import reduce
# print(reduce(lambda x , y : x + y, [1,2,3,4]))

# def maxi(num1 , num2):
#     if num1>num2:
#         return num1
#     else:
#         return num2
# print(reduce(maxi,[1,23,49,5,10]))

# print(reduce(lambda x,y : x if x>y else y ,[1,23,49,5,10]))

# print([*filter(lambda x : x%2==0 , [1,2,3,4,5,6,7,8])])

# d1={'a':1,'b':2}
# d2={'c':3,'d':4}
# print([*zip(d1,d2)])
# print([*zip(d1,d2.items())])
# print(dict([*zip(d2,d1.values())])) 

# def swich(n1):
#     return dict([*zip(n1.values(),n1)])
# print(swich(d1))

# def swich_all(n1,n2):
#     r=dict()
#     for i , n in zip(n1,n2.values()):
#         r[i]=n
#     return r   
# print(swich_all(d1,d2))

# def enum(squ , start=0):
#     for i in squ:
#         yield start,i
#         start+=1

# print([*enum(['a','b','c'])])
# print([*enumerate(['a','b','c'])])
# my_l=['a','b','c','d','e']

# for i,sq in enumerate(my_l):
#     if i>2 :
#         break
#     else:    
#         print(f'index:{i} value:{sq}')

# lst=[True,True,False,True]
# print(all(lst))
# print(any(lst))