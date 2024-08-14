# import csv,PyPDF2,re

# a=open('G:\\projects\\csv,pdf\\Exercise_Files\\find_the_link.csv',encoding='utf=8')
# aa=csv.reader(a)
# ii=0
# lst1=[]
# for i in [*aa]:
#     lst1.append(i[ii])
#     ii+=1
# print(''.join(lst1))

# b=open('G:\\projects\\csv,pdf\\Exercise_Files\\Find_the_Phone_Number.pdf','rb')
# bb=PyPDF2.PdfReader(b)
# for i in bb.pages:
#     if re.search(r'\d{3}.\d{3}.\d{4}',i.extract_text()):
#         print(re.search(r'\d{3}.\d{3}.\d{4}',i.extract_text()).group())