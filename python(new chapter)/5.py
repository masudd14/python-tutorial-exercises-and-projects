n=int(input('enter the num '))
sum=0
i=0
while i<n :
    b=int(input('enter the point of each lesson '))
    i+=1
    sum+=b
print(float(sum/n))



x=0
n=int(input('adad'))
fact=1
i=1
while i<n :
    i+=1
    fact*=i
print(fact)


n=int(input('adad : '))
a= 1
b=1
i=1
fib=0
if n==1 or n==2 :
    print(f'{n} as fib ')
else :    
    while i<n :
        fib=a+b
        b=a
        a=fib
        i+=1
    print(f'{fib} as fib ')