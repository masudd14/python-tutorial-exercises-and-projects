import winsound


a=input('what is your name? ')
print('hi',a,'welcome')

b=input('how old are you? ')
print('you are',b,'years old')

c=input('how tall are you?(cm) ')
d=int(c)
print('it is',d/100,'M')

e=input('what is your weght?(kg) ')
f=float(e)
print('it is',f*1000,'(g)')

for g in range(1500,2500,200):
    print('sound',g)
    winsound.Beep(g,1500)

