# import csv
# d=open('G:\\projects\\csv,pdf\\example.csv',encoding='utf-8')
# print(d)
# d_r=csv.reader(d)
# lst=[*d_r]
# print([*d_r][:3])

# for i in lst[:5]:
#     print(i[3])

# new=open('test.csv','w',newline='\n')
# new_r=csv.writer(new,delimiter=',')
# new_r.writerow(['a','b','c'])
# new_r.writerows([[1,2,3],[4,5,6],[7,8,9]])
# new.close()

# f=open('G:\\projects\\csv,pdf\\to_save_file.csv','a',newline='\n')
# f_r=csv.writer(f)
# f_r.writerow([171,181,191])
# f.close()

# import PyPDF2,time

# g=open('G:\\projects\\csv,pdf\\Working_Business_Proposal.pdf','rb')
# g_r=PyPDF2.PdfReader(g)
# g_w=g_r.pages[0]
# gg=PyPDF2.PdfWriter()
# gg.add_page(g_w)
# ggg=open('csv,pdf//Some_New_Doc.pdf','wb')
# gg.write(ggg)
# g.close()

# r=open('G:\\projects\\csv,pdf\\Working_Business_Proposal.pdf','rb')
# rr=PyPDF2.PdfReader(r)
# for i in range(len(rr.pages)):
#     print(rr.pages[i].extract_text())
#     time.sleep(2)
#     print('\n************************************************************************************')