# text='the phone number is smt call soon'
# print('phone' in text)

# import re
# pattern='phone'
# print(re.search(pattern,text))
# print(re.search('NOT IN TEXT',text))
 
# ma=re.search('soon',text)
# print(ma.span())
# print(ma.start())
# print(ma.end())

# text2='my phone is phone and it is a new phone'
# ma2=re.search('phone',text2)
# print(ma2.span())

# ma3=re.findall('phone',text2)
# print(ma3)

# for i in re.finditer('phone',text2): 
#     print(i)

# text3='my phone number is 408-555-1234'
# print(re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text3).group())

# print(re.search(r'\d{3}-\d{3}-\d{4}',text3).group())

# text4='my phone number is 408-555-1234 402-555-9823'
# print(re.findall(r'\d\d\d-\d\d\d-\d\d\d\d',text4))

# def find_patern(p,t):
#     for i in p:
#         print(f"searching for {i} in '{t}' :")
#         print(re.findall(i,t))
# find_patern([r'\d+',r'\w*'],text4)

# text5='hi how i am hi'
# print(re.findall(r'[hi]',text5))
# print(re.findall(r'[hi]{2}',text5))

# patern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# print(re.search(patern,text4).group())
# print(re.search(patern,text4).group(1))
# print(re.search(patern,text4).group(3))

# text6='this man was here'
# print(re.search(r'man|woman',text6).group())

# print(re.findall(r'.at','cat has a hat'))
# print(re.findall(r'.at','the bat went splat'))

# print(re.findall(r'.{4}at','cat has a hat'))
# print(re.findall(r'.{4}at','the bat went splat'))

# print(re.findall(r'\S+at','the bat went splat'))

# print(re.findall(r'^\d','1 is the loneliest number'))
# print(re.findall(r'\d$','this ends with 2'))

# print(re.findall(r'[^\d]','there are 3 numbers 34 inside 5 this'))
# print(re.findall(r'[^\d]+','there are 3 numbers 34 inside 5 this'))
# print(' '.join(re.findall(r'[^!?.\s]+','hi ! where? ok.')))

# text7='hello, would you like some catfish'
# text8='hello, would you like to take a catnap'
# text9='hello, have you seen this caterpiller'

# print(re.search(r'cat(fish|nap|claw)',text7))
# print(re.search(r'cat(fish|nap|claw)',text8))
# print(re.search(r'cat(fish|nap|claw)',text9))