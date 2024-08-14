# class Account:
#     def __init__(self, owner,balance=0):
#         self.owner=owner
#         self._balance=balance                  #none-public method
#     def get_balance(self):
#         return self._balance
# ac1=Account('someone',100)
# print(ac1.get_balance())
 

# class Test:
#     def __init__(self):
#         self.__x=1
#         self.y=2
#     def __fo(self):
#         print('private')
#     def mo(self):
#         print('public')
# obj1=Test()
# print(vars(obj1))
# print(obj1._Test__x)                          #none-public method
# obj1._Test__fo()                              #none-public method
# print(obj1.y)
# obj1.mo()


# class Counter:
#     num=0
#     def __init__(self):
#         type(self).num+=1
# x1=Counter()
# x2=Counter()
# x3=Counter()
# print(x1.num)
# print(Counter.num)
# Counter1=Counter()
# print(Counter1.num)
 

# class Co:
#     num=0
#     def __init__(self):
#         self.num+=1
# x1=Co()
# x2=Co()
# x3=Co()
# print(x1.num)
# print(Co.num)
# Co1=Co() 
# print(Co1.num)    


# class sample:
#     class_atr=100
#     def __init__(self,a):
#         self.a=a
#     def b(self):
#         print('hi')
# print(sample.class_atr)
# print(sample.__dict__)
# print(sample.__dict__['class_atr']) 
# aa=sample('good')
# aa.b()
# print(aa.__dict__)
# print(vars(aa))
# print(aa.__dict__['a'])
# aa.__dict__['a']='bye'
# print(aa.__dict__['a'])


# class r:
#     pass
# oo=r()
# di={'name':'masud','last_name':'none','status':True}
# for i,b in di.items():
#     setattr(oo,i,b)
# print(oo.name)
# print(oo.last_name)
# print(oo.status)
 

# class Q:
#     pass
# asd=Q()
# asd.name='masud'
# asd.last_name='none'
# asd.status=True
# print(asd.name)
# print(asd.last_name)
# print(asd.status)


# class w:
#     pass
# def __init__(self,name,last_name,status):
#     self.name=name
#     self.last_name=last_name
#     self.status=status
# w.__init__=__init__
# pp=w('masud','none',True)
# print(pp.__dict__)


# class threeD:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __iter__(self):
#         yield from (self.x,self.y,self.z)
#     @classmethod
#     def from_sequence(cls,sequence):
#         return cls(*sequence)
#     @staticmethod
#     def show_intro_message(name):
#         print(f'hi {name} welcome! ')
#     def __repr__(self):
#         return f'{type(self).__name__}({self.x}, {self.y}, {self.z})'
# yy=threeD(2,4,7)
# xx=threeD.from_sequence((7,9,1))
# zz=threeD(2,0,1)
# zz.from_sequence((33,55,11))


# class person:
#     def __init__(self,name):
#         self.set_name(name)
#     def get_name(self):
#         return self._name 
#     def set_name(self,value):
#         self._name=value
# jane=person('jane')
# print(jane.get_name())
# jane.set_name('jane doe')
# print(jane.get_name())


# class prs:
#     def __init__(self,name):
#         self.name=name
#     @property
#     def name(self):
#         return self._name 
#     @name.setter
#     def name(self,value):
#         self._name=value.upper()
# masud=prs('masud')
# print(masud.name)
# masud.name='none'
# print(masud.name)


# from dataclasses import dataclass
# @dataclass
# class threed:
#     x: int | float 
#     y: int | float
#     z: int | float
#     @classmethod
#     def from_sequence(cls,sequence ):
#         return cls(*sequence)
#     @staticmethod
#     def show_intro_message(name):
#         print(f'hi {name} welcome !')
# p1=threed(0.1,0.2,0.3)
# p2=threed(1,2,3)
# print(p1==p2) 


# from enum import Enum 
# class weekDay(Enum):
#         monday=1
#         tuesday=2
#         wednesday=3
#         thursday=4
#         friday=5
#         saturday=6
#         sunday=7
#         @classmethod
#         def favorite(cls):
#                 return cls.sunday
# print(list(weekDay))
# print(weekDay.monday)
# print(weekDay(4))
# print(weekDay['sunday'])
# print(weekDay.friday.name)
# print(weekDay.friday.value)
# for day in weekDay:
#         print(f'name: {day.name} , value: {day.value}')
# 


# class animal:
#     def __init__(self,name,sex,habitat):
#         self.ame=name
#         self.sex=sex
#         self.habitat=habitat
# 
# class mammal(animal):
#     feature='mammary glands'
#
#  class bird(animal):
#     feature='feathers'
# 
# class fish(animal):
#     feature='gills'
# 
# class dog(mammal):
#     def walf(self):
#         print('the dog is walking')
# 
# class cat(mammal):
#     def walk(self):
#         print('the cat is walking')
# 
# class eagle(bird):
#     def fly(self):
#         print('the eagle is flying')
# 
# class penguin(bird):
#     def swim(self):
#         print('the penguin is swimming')
# 
# class shark(fish):
#     def swim(self):
#         print('the shark is swimming')


# class aircraft:
#     def __init__(self,thrust,lift,max_speed):
#         self.thrust=thrust
#         self.lift=lift
#         self.max_speed=max_speed
#     def show_info(self):
#         print(f'thrust : {self.thrust} kw')
#         print(f'lift : {self.lift} kg')
#         print(f'max speed : {self.max_speed} km/h')
# 
# class helicopter(aircraft):
#     def __init__(self, thrust, lift, max_speed,num_rotors):
#         super().__init__(thrust, lift, max_speed)                              #extened
#         self.num_rotors=num_rotors
#     def show_info(self):
#         super().show_info()                                                    #extened
#         print(f'number of rotors : {self.num_rotors}')
# h1=helicopter(100,200,490,2)
# print(h1.__dict__)


# class worker:
#     def __init__(self,name,address,hourly_salary):
#         self.name=name
#         self.address=address
#         self.hourly_salary=hourly_salary
#     def show_profile(self):
#         print('==worker profile==')
#         print(f'name : {self.name}')
#         print(f'address : {self.address}')
#         print(f'hourly salary : {self.hourly_salary}')
#     def calculate_payroll(self,hour=40):
#         return self.hourly_salary * hour
# 
# class managers(worker):
#     def __init__(self, name, address, hourly_salary,bonus):
#         super().__init__(name, address, hourly_salary)                                 #extened
#         self.bonus=bonus
#     def show_profile(self):
#         super().show_profile()                                                         #extened
#         print(f'bonus : {self.bonus}')
#     def calculate_payroll(self, hour=40):
#         return (self.hourly_salary + self.bonus )*hour                                 #override


# class vehicle: 
#     def __init__(self,make,model,color):    
#         self.make=make
#         self.model=model
#         self.color=color
#     def start(self):
#         print('starting the engine ... ')
#     def stop(self):
#         print('stopping the engine ... ')
#     def show(self):
#         print(f'make : {self.make}')
#         print(f'model : {self.model}')
#         print(f'color : {self.color}')

# class car(vehicle):
#     def drive(self):
#         print('deiving on the road...')

# class Aircraft(vehicle):
#     def fly (self):
#         print('flying in  thr sky ... ')

# class flyingcar(car,Aircraft):
#     pass

# ll=flyingcar('moon',1999,'black')
# print(ll.model)
# ll.show()
# ll.drive()
# ll.fly()


# class A:
#     def method(self):
#         print('method A')
# class B(A):
#     def method(self):
#         print('method B')
# class C(A):
#     def method(self):
#         print('method C')
# class D(B,C) :
#     pass

# print(D.__mro__)
# xx=D()
# xx.method()


# import json
# import pickle

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
# class mixin:
#     def json(self):
#         return json.dumps(self.__dict__)
#     def pickle(self):
#         return pickle.dumps(self.__dict__)
    
# class employee(mixin,person):
#     def __init__(self, name, age,salary):
#         super().__init__(name, age)
#         self.salary=salary

# m=employee('masud',19,100000)
# print(m.json())
# print(m.pickle())


# class body:
#     def __init__(self):
#         self.rotation=0                                                                          
#     def rotate_left(self,degrees=10):
#         self.rotation-= degrees                                      #degreed = درجه
#         print(f'rotating body {degrees} degrees to left ...')
#     def rotate_right(self,degrees=10):
#         self.rotation+=degrees
#         print(f'rotating body {degrees} degrees to right ...')

# class arm:
#     def __init__(self):
#         self.position=0
#     def move_up(self,distance=1):
#         self.position+=distance
#         print(f'moving arm {distance} cm up ...')
#     def move_down(self,distance=1):
#         self.position-=distance
#         print(f'moving arm {distance} cm down ...')
#     def weld(self):
#         print('welding !')

# class robot:
#     def __init__(self):
#         self.arm=arm()
#         self.body=body()
#     def rotate_body_left(self,degrees=10): 
#         self.body.rotate_left(degrees)
#     def rotate_body_right(self,degrees=10):
#         self.body.rotate_right(degrees)
#     def move_arm_up(self,distance=1):
#         self.arm.move_up(distance)
#     def move_arm_down(self,distance=1): 
#         self.arm.move_down(distance)
#     def weld(self):
#         self.arm.weld()
    
# robot1=robot()
# robot1.move_arm_up(11)
# robot1.rotate_body_left(30)
# robot1.weld()
# print(vars(robot1))
# print(robot1.arm)
# print(robot1.body)


# class stack:
#     def __init__(self,item=None):
#         if item == None:
#             self._item=[]
#         else:
#             self._item=list(item)
#     def push(self,item):
#         self._item.append(item)
#     def pop(self):
#         return self._item.pop()
#     def __repr__(self) -> str:
#         return f'{type(self).__name__}({self._item})'
    
# ss=stack([1,2,3])
# ss.push(4)
# ss.push(5)
# print(ss.pop())
# print(dir(ss))
# print(ss)


# from abc import ABC , abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def set_perimeter(self):
#         pass

# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def get_area(self):
#         return 3.14 * self.radius **2
#     def set_perimeter(self):
#         return 3.14 * self.radius
    
# class square(shape):
#     def __init__(self,side):
#         self.side=side
#     def get_area(self):
#         return self.side **2
#     def set_perimeter(self):
#         return 4 * self.side 