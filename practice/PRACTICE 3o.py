import winsound

a=input('what is youe name? ')
print('hi',a,'welcome to our class ')

b=input('what is your age? ')
print('you are',b,'years old ')

c=input('what tall are you?(cm) ')
d=int(c)
print('you are',d/100,'m ')

e=input('what is your weght?(k) ')
f=float(e)
print('your weght is',f*1000,'(gm) ')

for g in range(500,3000,200):
    print('freq',g)
    winsound.Beep(g,1500)
    
