# class Line:
#     def __init__(self,coor1,coor2):
#         self.coor1=coor1
#         self.coor2=coor2
#         self.x1,self.y1=coor1
#         self.x2,self.y2=coor2
#     def distance(self):
#         return ((self.x1-self.x2)**2+(self.y1-self.y2)**2)**0.5
#     def slope(self):
#         return (self.y2-self.y1) / (self.x2-self.x1)
# coor1=(3,2)
# coor2=(8,10)
# li=Line(coor2,coor1)
# print(li.distance()) 
# print(li.slope())


# class Cylinder:
#     def __init__(self, height=1,radius=1):
#         self.height=height
#         self.radius=radius
#     def volume(self):
#         return ((self.radius**2)*3.14)*self.height
#     def surface_area(self):
#         return (((self.radius*2)*3.14)*self.height) + (((3.14*self.radius**2))*2)
# c=Cylinder(2,3)
# c2=Cylinder()
# print(c.volume())
# print(c.surface_area())
# print(c2.height)
# print(c2.radius)
# print(c2.volume())
# print(c2.surface_area())


# class account:
#     def __init__(self,owner,credit=0):
#         self.owner=owner
#         self.balance=credit
#     def get(self,value):
#         if self.balance>=value:
#             self.balance-=value
#             print('Accepted')
#         else:
#             print(f'dear {self.owner} ,you do not have enough money')
#     def give(self,cash):
#         self.balance += cash
#         print('Accepted')
#     def __str__(self):
#         return f'Account owner: {self.owner} \nAccount balance: ${self.balance}'
    
    
# bank1=account('sam',100)
# print(bank1)
# print(bank1.owner)
# bank1.give(50)
# print(bank1.balance)
# bank1.get(75)
# print(bank1.balance)
# bank1.get(500)