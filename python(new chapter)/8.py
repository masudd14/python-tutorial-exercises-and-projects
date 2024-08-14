# class Sample:
#     pass
# x=Sample()
# print(type(Sample( )))

# import math 
# class circle:
#     def __init__(self,radius) :
#         self.radius= radius
#     def calculate(self):
#         return (math.pi*self.radius**2,2)

# xx=circle(42)
# xxx=circle(7)
# print(xx.radius)
# print(xxx.radius)
# print(xx.calculate( ))
# print(xxx.calculate())
# xx.radius=100
# print(xx.calculate())

# class dog:
#     species='mammal'
#     def __init__(self,breed,name):
#         self.breed=breed
#         self.name=name
#         print(type(self).species)              #or dog.species
#     def bark(self):
#         print('wooof!')
# z=dog('huski','jack')
# zz=dog('lab','sam')
# print(zz.name)
# dog.bark(zz)
# print(zz.species)
# z.name='ian'
# print(z.name)


# class animal:
#     result='True'
#     def __init__(self):
#         print('created')
#     def whoAmI(self):
#         print('animal')
#     def eat(self):
#         print('food')


# class dog(animal):
#     def __init__(self):
#         animal.__init__(self)
#     def whoAmI(self):
#         print('dog')
#     def bark(self):
#         print('wooof!')
# ll=dog()
# ll.eat()
# ll.whoAmI()

 
# class dog:
#     def __init__(self, name):
#         self.name= name
#     def speak(self):
#         return self.name + ' says woof !'
    
# class cat:
#     def __init__(self, name):
#         self.name= name
#     def speak(self):
#         return self.name + ' says meow !'
    
# dog1=dog('jack')
# cat1=cat('lousi')
# print(cat1.name)
# print(dog1.name)
# print(dog1.speak())
# print(cat1.speak())

# for pet in [dog1,cat1]:
#     print(pet.speak())
#     print(pet.name)

# def pet_info(pet):
#     print(pet.speak())
#     print(pet.name)

# pet_info(dog1)
# pet_info(cat1)

  
# class animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         raise NotImplementedError('you can not make any changes')
    
# class dog(animal):
#     def speak(self):
#         return self.name + ' says woof !'
    
# class cat(animal):
#     def speak(self):
#         return self.name + ' says meow !'

# pet2=animal('pet')
# dog2=dog('jack 2')
# cat2=cat('lousi 2')  
# print(dog2.speak())
# print(cat2.speak())
# print(pet2.speak())


# class book:
#     def __init__(self,title,author,pages):
#         print('the book is created')
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def __str__(self):
#         return f'title : {self.title} , author : {self.author} , pages : {self.pages}'
#     def __len__(self):
#         return self.pages
#     def __del__(self):
#         print(f'{self.title} is deleted')

# someBook=book('silent moon','unkonwn',300)
# print(someBook.author)
# print(someBook)
# print(len(someBook))
# del someBook