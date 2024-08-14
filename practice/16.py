# from tkinter import *
# import time

# window=Tk()
# window.geometry('+600+350')
# window.title('clock')
# x=IntVar()
# y=StringVar()
# z=StringVar()
# f=Frame(window,width=10,height=5)
# f.pack()
# Label(f,bg='black',width=10,fg='yellow',textvariable=x,font=('Arial',34,'bold')).pack()
# Label(f,bg='pink',width=14,fg='black',textvariable=z,font=('Ink Free',24,'bold')).pack()
# Label(f,bg='pink',fg='black',width=14,textvariable=y,font=('Ink Free',24,'bold')).pack()
# print(time.ctime()[11:19])
# while True:
#     x.set(f'{time.ctime()[11:19]}')
#     z.set(f'{time.ctime()[:3]}')
#     y.set(f'{time.ctime()[4:10]} , {time.ctime()[20:]}')
#     window.update()

# window.mainloop()