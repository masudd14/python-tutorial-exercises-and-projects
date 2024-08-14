# def a(b,c):
#     if b%2==0 and c%2==0 :
#         if b<c :
#             return b
#         else :
#             return c 
#     else :                                              #you can also use max() and min()
#         if b<c :
#             return c
#         else :
#             return b
# print(a(2,4))
# print(a(2,5))


# def d(e):
#     f=e.split()
#     if f[0][0].lower()==f[1][0].lower():
#         return True
#     else:
#         return False
# print(d('Levelheaded Llama'))
# print(d('imperator bozorg'))


# def g(h,i):
#     if (h==20 or i==20) or i+h==20:
#         return True
#     else :
#         return False
# print(g(20,10))
# print(g(12,8))
# print(g(2,3))


# def j(k):
#     if len(k)>3:
#         return k[:3].capitalize()+k[3:].capitalize()
# print(j('macdonald'))

# def l(m):
#     n=m.split()
#     n.reverse()
#     return ' '.join(n)
# print(l('i am home'))
# print(l('we are ready'))


# def o(p):
#     if abs(p-100)<=10 or abs(p-200)<=10:
#         return True
#     else :
#         return False
# print(o(90))
# print(o(104))
# print(o(150))
# print(o(209))


# def q(r):
#     list=[]
#     for a in r :
#         list.append(a)
#         if len(r)!=1 :
#             if r[-1]==3 and r[-2]==3:
#                 return True
#     else: 
#         return False
# print(q([1,3,3]))
# print(q([1,3,1,3]))
# print(q([3,1,3]))


# def s(t):
#     list=[]
#     for u in t:
#         list.append(u*3)
#     return ''.join(list)
# print(s('hello'))
# print(s('mississippi'))


# def v(w,x,y):
#     if (1<w<=11) and (1<x<=11) and (1<y<=11) :
#         if w+x+y<=21:
#             return w+x+y
#         elif w+x+y>21 :
#             if (w+x+y-10 < 21) and (x==11 or w==11 or y==11) :
#                 return w+y+x-10
#             else :
#                return 'Bust'
#     else:
#         return 'enter the number between 1 and 11! '
# print(v(5,6,7))
# print(v(9,9,9))
# print(v(9,9,11))
# print(v(8,6,33))


# def z(a1):
#     b=0
#     i=-1
#     list=[]
#     for b1 in a1 :
#         list.append(b1)
#         if len(list)!=1:
#             if list[-2]==6 :
#                 if list[-1]==9:
#                     return sum(a1)-list[-1]-list[-2]   
#                 else :
#                     print(i)
#                     for xx in range(i,len(a1)):
#                         b+=a1[xx]
#                         if a1[xx]==9:
#                             break
#                     return sum(a1)-b
#         i+=1
#     else:
#         return sum(a1)
            
# print(z([1,3,5]))
# print(z([4,5,6,7,8,9]))
# print(z([2,1,6,9,11]))


# def c1(d1):
#     list=[]
#     for e1 in d1:
#         if e1== 0 or e1==7 :
#             list.append(e1)
#     for i in range(0,len(list)-2):
#         if list[i]==0 and list[i+1]==0 and list[i+2]==7:
#             return True
#     else :
#         return False
# print(c1([1,2,4,0,0,7,5]))
# print(c1([1,0,2,4,0,5,7]))
# print(c1([1,7,2,0,4,5,0]))


# def f1(g1):
#     list=[2]
#     h1=3
#     if g1<2:
#         return 0
#     while h1<=g1:
#         for i1 in range(3,h1,2):
#             if h1%i1==0 :
#                 h1+=2
#         else:
#             list.append(h1)
#             h1+=2
#     print(list)
#     return len(list)
# print(f1(100))



# def h1(i1):
#     if i1.lower()=='a' or i1.lower()=='b' or i1.lower()=='c' or i1.lower()=='d' or i1.lower()=='e' :
#         if i1.lower()=='a' :
#             return ' ****  \n*    * \n*    * \n****** \n*    * \n*    * '
#         elif i1.lower()=='b':
#             return '***** \n*    *\n*    *\n*****\n*    *\n*    *\n*****'
#         elif i1.lower()=='c':
#             return ' **** \n*    *\n*\n*\n*    *\n ****'
#         elif i1.lower()=='d':
#             return '*****\n*    *\n*    *\n*    *\n*    *\n*****'
#         elif i1.lower()=='e':
#             return '*****\n*\n*\n*****\n*\n*\n*****' 
#     else:
#         return 'only support a,b,c,d,e letters! '
# print(h1('a'))
# print(h1('b'))
# print(h1('c'))
# print(h1('d'))
# print(h1('e'))
# print(h1('f'))