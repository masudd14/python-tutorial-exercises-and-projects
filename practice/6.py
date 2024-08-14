# def a(b):
#     return (4/3)*3.14*(b**3)
# print(a(2))


# import math 
# def a(b):
#     return (4/3)*(math.pi)*(b**3)
# print(a(2))


# def c(num,low,high):
#     if low <= num <= high :
#         return f'{num} is in range between {low} and {high}'
#     else :
#         return 'the number is outside of the range'
# print(c(5,2,7))
# print(c(7,8,19))


# def c(num,low,high):
#     if num in range(low,high+1):
#         return True
#     else :
#         return False
# print(c(5,2,7))
# print(c(7,8,19))


# def d(str):
#     list_upper=[]
#     list_lower=[]
#     for i in str:
#         if i.isupper():
#             list_upper.append(i)
#         elif i.islower() :
#             list_lower.append(i)
#     return f'{len(list_upper)} upper word and {len(list_lower)} lower word '
# print(d(' Hello Mr. Rogers, How Are You In This Fine Tuesday?'))


# def d(str):
#     dic={'upper': 0 , 'lower': 0}
#     for i in str:
#         if i.isupper():
#             dic['upper']+=1
#         elif i.islower() :
#             dic['lower']+=1 
#     return f'{dic["upper"]} upper word and {dic["lower"]} lower word '
# print(d(' Hello Mr. Rogers, How Are You In This Fine Tuesday?'))


# def c(nums):
#     return [*set(nums)]
# print(c([1,1,1,1,2,2,3,3,3,3,4,5]))


# def c(nums):
#     x=[]
#     for i in nums :
#         if i in x :
#             pass
#         else :
#             x.append(i)
#     return x
# print(c([1,1,1,1,2,2,3,3,3,3,4,5]))


# def d(list):
#     power= 1
#     for i in list:
#         power*=i
#     return power
# print(d([1,2,3,-4]))


# def e(text):
#     if text.lower()==text[::-1].lower():
#         return True
#     else :
#          return False
# print(e('Madam'))


# def e(text):
#     s=text.replace(' ','')
#     if s.lower()==s[::-1].lower():
#         return True
#     else :
#          return False
# print(e('NursesRun'))


# import string
# en=string.ascii_lowercase
# en1=set(en)
# def f(text):
#     x=text.replace(' ','')
#     x_lower=x.lower()
#     x1=set(x_lower)
#     if en1 == x1:
#         return True
#     else:
#         return False
# print(f('the quick brown fox jumps over the lazy dog'))


# import string
# sentence='i am melanee 44*#&*!'
# def srting(a):
#     list=[]
#     for i in a:
#         if i.isalpha():
#             list.append(i)
#         elif i==' ':
#             list.append(i)
#         elif i.isdigit():
#             list.append(i)
#         else:
#             pass
#     return ''.join(list)
# print(srting(sentence))


# def a(*args):
#     sum=0
#     for i in args:
#         for i2 in i:
#             sum+=i2
#     return sum
# print(a([1,2,3],[4,5,6],[7,8,9]))


# def a(*args):
#     sum1=0
#     for i in args:
#         sum1+=sum(i)
#     return sum1
# print(a([1,2,3],[4,5,6],[7,8,9]))


# def a(b):
#     list1=[]
#     for i in b:
#         if i==1 or i==5:
#             list1.append(i)
#     print(list1)
#     for i2 in range(0, len(list1)-2):
#         if list1[i2]==1 and list1[i2+1]==1 and list1[i2+2]==5:
#             return True
#     return False
# print(a([9,1,5,1,0,2,1,8,7]))