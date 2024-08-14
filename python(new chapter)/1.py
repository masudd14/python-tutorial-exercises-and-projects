# print(2e6)
# print(15%2)
# print(5+10*10+3)
# a=27
# print(a**(1/3))
# print(id(a))
# tax=0.1
# income=100
# my_tax= tax*income
# print(my_tax)
# b=[1,{'firstname': 'masud','age': 18 , 'status':True },2,4]
# print(type(b))
# print(b[1]['firstname'])
# firstname='masud'
# lastname='out'
# fullname=[]
# fullname.append(firstname)
# fullname.append(lastname)
# print(fullname)
# print(b[1]['status'])
# _list=[3,'none',{'firstname':'name','lastname':'family','age':18 , 'status': True},13,14,17]
# print(len(_list))
# print(_list[2]['age'])
# print(len(_list[2]))
# print(_list[2])
# print(firstname[-1])
# a11='abcdefaa'
# print(a11[0:5:2])
# print(firstname[::-1])
# a11.upper()  
# print(a11.upper()) 
# print(a11)
# e=a11.upper()
# print(e)
# print(a11.count('a'))
# print(a11.replace('a','13'))
# a22='  hello world  '
# print(a22)
# print(a22.upper())
# print(a22.lower())
# print(a22.capitalize())
# print(a22.replace('ll','3'))
# print(a22.strip())
# print(a22.lstrip())
# print(a22.rstrip())
# print(a22.split('o'))
# print(a22.count('l'))
# print(a22.find('o'))
# print('i\'m gonig to inject %s here' %'something')
# print('my name is %s' %'masud')
# print('hi my name is %r and i am %s years old' %('masud','18')) 
# print('this is %1.2f' %32.14444)
# print('i\'m gonig to inject {} here'.format('something'))
# print('hi my name is {} and im {} years old'.format('masud','18'))
# h1='i\'m {2} and i\'m {0} and my lastname is {1}'.format('18','none','masud')
# print(h1)
# print(f'hi my name is {firstname}')
# name='masud'
# age='18'
# print('hi my name is %s adn im %s' %('masud', '18'))
# print('hi my name is {1} and im {0}'.format('18','masud'))    
# print(f'hi my name is {name} and im {age}')  
# print('name:{0:<10} | age:{1:^15}'.format('masud','18'))  
# #from string import template                                           tempalteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
# from string import Template
# a=Template('hi my name is $name')
# b='masud' 
# c=a.substitute(name = b)
# print(c)
# mylist=[1,'12',{}]
# print(len(mylist))
# print({} in mylist) 
# mylist=33
# print(33 is mylist)
# c=[]
# c.append(b)
# print(c)
# c.append(age)
# print(c)
# list=[1,2,3,4]
# list=list+['masud']
# print(list)
# list=list*2
# print(list)
# list.extend(['hi', 'bye'])
# print(list)
# list.insert(1 , 'str')
# print(list)
# list.pop(5)
# print(list)
# list=['hello']+list
# print(list)
# list+= 'string'
# print(list)
# print(list[0][1])
# list1=[1,2,3,4,1,1,'masud']
# list1.remove('masud')
# print(list1) 
# del list1[3:]
# print(list1)
# list2=[1,2,3,4,1,1,'masud']
# list2.reverse()
# print(list2)
# newlist=[3,9,54,56,213,45,1,4]
# newlist.sort()
# print(newlist)
# newlist.sort(reverse=True)
# print(newlist)
# newlist3=['a','b','c','d','e']
# newlist3[1:4]=[1,2,3,4,5,6,7]
# print(newlist3)
# newlist3[:5]=['b','v']
# print(newlist3)
# lst1=[1,2,3]
# lst2=[4,5,6]
# lst3=[7,8,9]
# matrix=[lst1,lst2,lst3]
# print(matrix[1][2])
# x=['a',['bb',['ccc','ddd'],'ee','ff'],'g',['hh','ii'],'j']
# print(x[1][1][1][2].upper())
# t=(1,2,3,'hi',1)
# print(t.index('hi'))
# print(t.count(1))
# t2=(1,2,(3,4),[1,2,3])
# t2[3][1]='hi'
# print(t2)
# t3= 1,2,'masud',4
# print(type(t3))
# tu1 , tu2 , tu3 , tu4 = t3
# print(tu1 , tu2 , tu3 , tu4)
# print(tu2)
# dic={'firstname': 'm' , 'lastname' : 'v' , 'age' : 18 }                    # first way
# print(dic['age'])
# dic1= dict([('firstname','m'),('lastname','v'),('age', 18)])               # second way
# print(dic1['lastname'])
# edic1= dict( firstname='masud' , lastname='none')
# print(edic1['lastname'])
# dic['status']= True
# print(dic)
# dic2={'name':'masud',  'dci':['hello' , 2 ,3] , 'age': 18 }
# print(dic2['dci'][1])
# print(dic2['dci'][0].upper())
# dic3={}                                                                    # third way
# dic3['name']='masud'
# dic3['age']= 18
# print(dic3)
# dic4={'key':{'name':{'masoud':{'age': 18}}}}
# print(dic4['key']['name'])
# print(dic4['key']['name']['masoud']['age'])
# dic4={'key1': 1 , 'key2':2 , 'key3':3}
# print(dic4.keys())
# print(dic4.values())
# print(dic4.items())
# print(dic4.get('key4'))
# print(dic4)
# print(dic4.pop('key1'))
# print(dic4)
# print(dic4.popitem())
# print(dic4)
# m = set()
# m.add(1)
# m.add(2)
# m.add(1)
# print(m)
# lst4=[1,1,1,1,2,2,3,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,8]
# m2 = set(lst4)
# print(m2)
# lst5= list(m2)
# print(lst5)
# t4= tuple(lst5)
# print(t4)
# print(set('hello'))
# mm2 = None
# m2 = mm2
# print( m2 is mm2)
# print(1>3)
# print(2>1)
# my_file= open('G:\\projects\\python(new chapter)\\test.txt')                          #file has been deleted if you wanna run this create the file again
# print(my_file.read())
# print(my_file.seek(0))
# print(my_file.readlines())
# my_file.close()
# my_file=open('G:\\projects\\python(new chapter)\\test.txt','w+')                      #w+ 
# my_file.write('this is a test')
# print(my_file.read())
# my_file.close()
# my_file=open('G:\\projects\\python(new chapter)\\test.txt','a+')                      #a+
# my_file.write('\nbye')
# print(my_file.read())
# my_file.close()
# city=str(input('enter the name of city '))
# name2=str(input('enter the name '))
# age=int(input('enter the age '))
# print(f'i have a body in {city} her name is {name2} and she is {age} years old ')
# v=3
# vv=4
# print(vv==v)
# print(vv!=v) 
# print(vv>v)
# print(vv<v)
# v1=[1,2,3]
# vv1=v1
# print(vv1 is v1)
# vve=2
# print(vve in v1)
# vv2= 0.3 + 0.4
# print(vv2)
# print(vv2==0.7)
# tolerance=0.001
# vv3=  0.1 + 0.2
# print(abs(vv3 - 0.3) < tolerance)
# aaa= True 
# bbb= False
# print(aaa or bbb)
# print( aaa and bbb)
# aaa1=False
# bbb1=False
# print(aaa1 or bbb1)
# print(aaa1 and bbb1)
# print(bool([]))
# print(bool([1,2,3]))
# print(bool({'key':'value'}))
# print( 2>0 or 2 or 5!=5 or True)
# print(2 and 5==5 and 5!=6 and False and 3>1)
# x1= input('enter something') or 'Empty'
# print(x1)
# print(1<2<3)
# print(1<3>2)