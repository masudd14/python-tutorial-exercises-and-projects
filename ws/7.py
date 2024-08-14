# myList=[1,2,3,4,5,6,7,8,9,10]

# print(myList[1:4])
# print(myList[1:8:2])
# copyOfNumbers=myList[::-1]
# print(copyOfNumbers)
# print(copyOfNumbers==myList)
# print(copyOfNumbers is myList)
# print(id(copyOfNumbers),'\n',id(myList))

# name=input('enter youe name : ')
# lastName=input('enter your lastname : ')
# re_name=lastName[::-1]
# print(f'{name} {re_name}')

# colors=['red','green','blue','yellow','orange']
# copyOfColors=colors[::-1]
# print(copyOfColors)
# colors.reverse()
# print(colors)

# myNumber=[1,2,3,4,5,6,7,8,9,10]
# doubled_numbers=[]
# for i in myNumber:
#     doubled_numbers.append(i*2)
# print(doubled_numbers)

# a=[i*2 for i in myNumber]
# print(a)

# myName='masud'
# b=[i.upper() for i in myName]
# print(''.join(b))

# c=[f'even : {i}'  for i in myNumber if  i%2==0 ]
# print(c)
# d=[f'odd : {i}'  for i in myNumber if  i%2!=0 ]
# print(d)
# e=[i if i%2==0 else (i*2)+1 for i in myNumber]
# print(e)

# numbers=[1,2,3,4,5,6]
# newNumbers=[[1,2,3],[4,5,6]]
# print(newNumbers[1][1])

# for i in newNumbers:
#     for i2 in i:
#         print(i2)

# aq=[newNumbers[i]  for i in range(0,2)]
# print(aq)

# ss=[['x' if newNum %2==0 else 'o' for newNum in range(1,4)]for num in range(1,4)]
# print(ss)

# aaa=[[i for i in range(1,4)],[i1 for i1 in range(4,7)]]
# print(aaa)