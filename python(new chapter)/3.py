# def f(f1,f2):
#     print(f'his firstname is {f1} and the lastname is {f2}')
# f('empty','none')
# f('1','2')


# def add(a,b,c):
#     result=a+b+c
#     print(f'result: {result} ')
# add(10,12,3)


# def a(num,name,price):
#     b=price/num
#     print(b)
# a(price=30,name='something',num=2)


# def b(item,num,price=5):
#     print(f'{num} of {item} costs {price:.2f}')
# b(item='something',num=10)


# def c(my_list=[]):
#     my_list.append('##')
#     print(my_list)
#     return my_list
# c()
# c()
# c([1,2,'hi'])
# c()


# def f(fx):
#     print(fx)
#     fx=10
#     print(fx)
# x=5
# f(x)
# print(x)


# def d(A):
#     print(A,'\t',id(A))
#     A='hi'
#     print(A,'\t',id(A))
# e=10
# d(e)
# print(e,'\t',id(e))


# def f(g):
#     print(g,'\t',id(g) )
#     g=[1,2,3]
#     print(g,'\t',id(g))
# h=[4,5,6]
# f(h)
# print(h,'\t',id(h))


# def i(j):
#     print(j,'\t',id(j))
#     j[4]=13
#     print(j,'\t',id(j))
# k=[1,2,3,4,5,6]
# i(k)
# print(k,'\t',id(k))


# def l(m):
#     print(m,'\t',id(m)) 
#     m[4]=13
#     print(m,'\t',id(m))
# n=[1,2,3,4,5,6]
# l(n.copy())
# print(n,'\t',id(n)) 


# def o():
#     print('hi')
#     print('bye')
#     return
#     print('ok')
# o()


# def p():
#     return 'hi'
# q=p()
# print(q)


# def r():
#     return dict(k1=1 , k2=2 , k3=3)
# print(r())
# s=r()
# print(s['k2']**2)


# def t():
#     return [1,2,3,4,5]
# print(t())
# u=t()
# print(u[2]*10)
# print(t()[::-1])


# def v():
#     return 'one','two','three','four'
# print(v())
# w1,w2,w3,w4=v()
# print(w2,w4)


# def x(num1,num2):
#     sum=num1+num2
#     ave=sum//2
#     return [sum,ave]
# print(x(6,4))
# print(x(6,4)[0]*10)


# def y(z):
#     num=0
#     i=0
#     for a1 in z :
#         num+=a1
#         i+=1
#     return num/i
# print(y([2,3,4,6,7]))


# def b1(*args):
#     print(args)
#     sum=0
#     for c1 in args:
#         sum+=c1
#     return sum/len(args)
# print(b1(1,2,3,4))


# def d1(x,y,z):
#     print(f'x : {x}')
#     print(f'y : {y}')
#     print(f'z : {z}')
# d1(*[1,'hi',3]) 


# def e1(**kwargs):
#     for f1,g1 in kwargs.items():
#         print(f'{f1}\t{g1}')
#     print(kwargs.get('sport'))
# e1(math=20,history=18,behavier=1)


# def h1(i1,j1,k1):
#     print(f'i1 : {i1}')
#     print(f'j1 : {j1}')
#     print(f'k1 : {k1}')
# h1(**{'i1':11,'j1':22,'k1':33})


# def l1(m1,*args,**kwargs):
#     print(f'm1 : {m1}')
#     print(f'args : {args}')
#     print(f'kwargs : {kwargs}')
# l1(13,11,22,33,44,k1=1,k2=2,k3=3)


# list_01=[1,2,3,4,5]
# list_o2=[]
# def n1(o1):
#     return o1**2
# print(list(map(n1,list_01)))
# def p1(q1):
#     for i in q1 :
#         list_o2.append(i**2)
#     return list_o2
# print(p1(list_01))
# print([*map(n1,list_01)])


# def r1(s1):
#     if len(s1)%2==0:
#         return 'even'
#     else:
#         return s1[0]
# str=['john','cindy','sarah','kelly','mike']
# print([*map(r1,str)])


# def t1(u1):
#     return u1%2==0
# list_u1=[0,1,2,3,4,5,6,7,8,9,10]
# print([*filter(t1 ,list_u1)])


# def v1(w1): return w1**2
# print(v1(5))

# x1=lambda w1 : w1**2
# print(x1(8))

# lambda_list=[1,2,3,4,5]
# print([*map(lambda a : a**2 , lambda_list)])

# lambda_list1=[0,1,2,3,4,5,6,7,8,9,10]
# print([*filter(lambda b : b%2==0 , lambda_list1) ])


# y1=lambda a : a[0]
# print(y1('Hello'))

# z1= lambda n :n[::-1]
# print(z1('Hello'))

# a2= lambda k,j : k+j
# print(a2(5 ,6))


# name='this is a test'
# def b2():
#     name='m'
#     def c2():
#         print('hi '+name)
#     c2()
# b2()
# print(name)


# name1='this is a test'
# def d2():
#     def e2():
#         print('hi '+name1)
#     e2()
# d2()


# print(print)
# print(id)
# print(abs)


# h2=15
# def i2():
#     h2=30
#     print(h2)
# i2()
# print(h2)


# f2=15
# def g2():
#     global f2
#     print(f2)
#     f2=30
#     print(f2)
# g2()
# print(f2)

