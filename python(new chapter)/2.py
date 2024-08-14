# if False :
#     print('action1')
# elif True :
#     print('action2')
# elif True :
#     print('action3')
# else :
#     print('action4')


# name='masud'
# match name :
#     case 'oo' :
#         print('hi')
#     case 'masud' :
#         print('that is it ')
#     case other :
#         print('nothing')


# while False :
#     print('ok')
# else :
#     print('not ok')



# while True :
#     a=str(input('do you want to continue? '))
#     if a== 'yes' :
#         continue
#     elif a== 'yes':
#         print('ok')
#     else :
#         break


# x=0
# while x<=10 :
#     if x%2==0 :
#         print(f'{x} is odd')
#         x+=1
#         continue
#     else:
#         print(f'{x} is not odd')
#         x+=1
# else : print('all done')

# list=[1,2,3,4,5,6,7,8,9,10]
# for num in list :
#     print(num)


# x=iter([1,2,3,4])
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# y=iter('hello')
# print(y)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

# z=iter({'k1':100 , 'k2':200})
# print(z)
# print(next(z))
# print(next(z))

# mylist=[1,2,3,4,5,6,7,8,9,10]

# for num in mylist :
#     if num%2==0 :
#         print(num)
#     else:
#         print(f'odd {num}')

# sum=0
# for num in mylist :
#     sum+=num
# print(sum)
 
# for letter in 'hello how are you' :
#     print(letter)

# tup_on=(1,)
# tup= 1,2,3,4,5,6
# tup1 , tup2 , tup3 , tuo4 , tup5 , tup6 = tup
# print(tuo4 , tup5 , tup6)

# list2=[(1,2),(3,4),(5,6)]

# for t in list2 :
#     print(t)

# for t1 , t2 in list2 :
#     print(t1 , t2)

# d= {'k1':100 , 'k2':200 , 'k3':300}

# for item in d :
#     print(item)

# for item in d :
#     print( item , d[item])

# for k , v in d.items() :
#     print(k , v)

# for a in range(1,101) :
#     if a%2==0 :
#         print(a)

# num_index=0
# for letter in 'abcdef' :
#     print(f'at index {num_index} the letter is {letter}')
#     num_index+=1

# for i , a in enumerate('abcdef') :
#     print('at index {} the letter is {}'.format(i , a))

# list1=[1,2,3,4]
# list2=['a','b','c','d','e ']
# print(zip(list1,list2))
# print(list(zip(list1,list2)))

# for one , two in zip(list1 , list2) :
#     print(one , two)

# list3=[1,2,3,4,5,6]
# print(min(list3))
# print(max(list3))
# print(sum(list3))

# from random import shuffle
# list4=[1,2,3,4,5,6,7,8,9,10]
# shuffle(list4)
# print(list4)

# from random import randint
# print(randint(0,100))
# print(randint(0,100))

# list5=[]
# for i in range(1,11):
#     result=i**3
#     list5.append(result)
# print(list5)

# list6=[i**3 for i in range (1,11)]
# print(list6)

# list7=[x for x in 'hello world']
# print(list7)

# list8=[x**3 for x in range(1,11) if x%2==0]
# print(list8)

# celsius=[0,10,20.1,34.6]
# fahrneheits=[((9/5)*temp)+32 for temp in celsius]
# print(fahrneheits)

# list9=[i*2 for i in[x**3 for x in range(11)]]
# print(list9)