from string import Template

a = Template('hi my name is $name')
b='masud'
c=a.substitute(name=b)
print(c)


x=0
n=int(input('adad'))
fact=1
i=1
while i<n :
    i+=1
    fact*=i
print(fact)

n1=int(input('adad1 '))
sum=0
if n1%2==0 :
    sum=2*n1+5
elif not n1%2==0 :
    sum=3*n1-5
print(sum)

n2=int(input('adada 2  '))
i2=0
sum2=0
while i2<n2 :
    i2+=1
    sum2+=i2
print(sum2)

 