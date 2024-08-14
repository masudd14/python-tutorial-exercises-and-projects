# def n1(*args):
#     for m1 in args:
#         if m1%2==0:
#             return True
#     else:
#         return False
# print(n1(1,3))


# def o1(p1):
#     i=1
#     divider=1
#     while i<p1 :
#         if p1%i==0:
#             divider+=1
#         i+=1
#     if divider==2:
#         print('the number is prime ')
#     else:
#         print('the number is not prime  ')
# o1(4)


# def q1(*args):
#     list=[]
#     for r1 in args: 
#         if r1%2==0:
#             list.append(r1)
#     if len(list)!=0:
#         print(list)
#         return True
#     else:
#         return False
# print(q1(1,3,5,7))


# def s1(t1):
#     mylist=[]
#     for u1 in t1 :
#         if u1%2==0:
#             mylist.append(u1)
#     if len(mylist)==0:
#         return False
#     else: 
#         print(mylist)
#         return True
# print(s1([1,3,5,4,7]))


# def v1(w1):
#     divider=1
#     for i in range(1,w1):
#         if w1%i==0 :
#             divider+=1
#     if divider==2 :
#         return True
#     else :
#         return False
# print(v1(3))
        

# def x1(y1):
#     for z1 in range(2,y1):
#         if y1%z1==0:
#             return False
#     else:
#         return True
# print(x1(13))        


# import math
# def a2(b2):
#     if b2%2==0 and b2>2 :
#         return False
#     for c2 in range(1,int(math.sqrt(b2))+1,2):
#         if b2%c2==0:
#             return False
#     return True
