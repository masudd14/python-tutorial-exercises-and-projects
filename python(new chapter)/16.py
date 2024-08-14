# from collections import Counter

# lst=[1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
# print(Counter(lst))

# stri='hello how are you'
# print(Counter(stri)) 

# stri2='how many times does each word show up in this sentence word times each each word'
# print(Counter(stri2.split()))

# c=Counter(stri)
# print(c.most_common())

# from collections import defaultdict
# d=dict()
# print(d.get('one'))
# d1=defaultdict(lambda:0)
# print(d1)
# print(d1['one'])
# print(d1)
# print(d1[1])
# print(d1)
# d1[14]='masud'
# print(d1)

# from collections import namedtuple
# dog=namedtuple('dog',['age','breed','name'])
# sam= dog(age=2,breed='huski',name='sam')
# print(sam)
# alex= dog(age=3,breed='lab',name='alex')
# print(alex)

# import os
# print(os.getcwd())  
# print(os.listdir())

# import shutil
# import send2trash

# import datetime

# t=datetime.time(2,22,17)
# print(t)
# print(f'second : {t.second}')
# print(f'minute : {t.minute}')
# print(f'hour : {t.hour}')

# print(datetime.time.min)
# print(datetime.time.max)
# print(datetime.time.resolution)


# today=datetime.date.today()
# today=datetime.date(2024,7,28)
# print(today)
# print(today.ctime())
# print(today.timetuple())
# print(today.toordinal())
# print(today.year)
# print(today.month)
# print(today.day)
# d2=today.replace(year=2012)
# print(d2)
# print(today-d2)

# print(datetime.datetime.now().hour)

# import math

# help(math)

# value=4.35
# print(math.floor(value))
# print(math.ceil(value))
# print(round(value ))

# print(f'{math.pi} , {math.e}, {math.tau}')
# math.inf=4202 
# print(math.inf)
# math.nan=1239
# print(math.nan) 

# print(math.log(math.e))
# print(math.log(0))
# print(math.log(100,10))

# print(math.sin(10))
# print(math.degrees(math.pi/2))
# print(math.degrees(180))

# import random

# print(random.randint(1,100)) 
# random.seed(100)
# print(random.randint(1,100))
# print(random.randint(1,100))
# print(random.randint(1,100))

# mylist=['hi','bye',1,'2']
# print(random.choice(mylist))

# mylist2=[*range(21)]
# print(random.choices(population=mylist2,k=10))
# print(random.sample(population=mylist2,k=10))

# mylist3=[1,2,3,4,5,6,7]
# random.shuffle(mylist3)
# print(mylist3)

# print(random.uniform(a=0,b=100))

# print(random.gauss(mu=0,sigma=1))

# import pdb

# x=[1,2,3]
# y=2
# z=3
# result= y + z
# print(result)

# pdb.set_trace()
 
# result2= x + y
# print(result2)

# import time

# def func_1(n):
#     return [str(num) for num in range(n)]

# def func_2(n):
#     return [*map(str,range(n))]

# start= time.time()
# func_1(1000000)
# end= time.time()
# print(end-start)

# start2= time.time()
# func_2(1000000)
# end2= time.time()
# print(end2-start2)

# import timeit

# setup1=''' 
# def func_3(n): 
#     return [*map(str,range(n))]
# '''
# stmt1='func_3(1000)'
# print(timeit.timeit(stmt1,setup1,number=1000))

# a=open('new_file.txt',"w+")
# a.write('this is a test')
# a.close()

# b=open('new_file2.txt','w+')
# b.write('this is a test 2')
# b.close()

# import zipfile

# c=zipfile.ZipFile('prz.zip','w')
# c.write('new_file.txt',compress_type=zipfile.ZIP_DEFLATED)
# c.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)

# d=zipfile.ZipFile('prz.zip','r')
# d.extractall('extract')

# import shutil

# path='G:\\projects\\zip'
# name='shutilzz'
# shutil.make_archive(name,'zip',path)
# shutil.unpack_archive(name,'unzip','zip')