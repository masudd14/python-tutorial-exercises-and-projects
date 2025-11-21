import random
from string import ascii_lowercase as al
from time import sleep
a=input('enter password: ')
al=list(al)
al.append(' ')
al.extend(['1','2','3','4','5','6','7','8','9','0'])
c=[]
for i in a:
    while True:
        b=random.choice(al)
        if i.lower()==b:
            c.append(i)
            print(''.join(c))
            sleep(0.08)
            break
        else:
            print(f"{''.join(c)}{b}")
            sleep(0.08)
            continue
print(f"your password is {''.join(c)}")


