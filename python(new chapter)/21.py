from tkinter import *
# from PIL import Image,ImageTk
# from tkinter import messagebox
# from tkinter import colorchooser
# from tkinter import filedialog
# from tkinter import ttk
# from tkinter.ttk import *
import time

# count=0
# def click():
#     global count
#     count+=1
#     print(count)

# first=Tk()
# first.geometry('840x740+500+150')
# first.title('hiiiii !')
# ph=PhotoImage(file='G:\\projects\\images\\kisspng-black-house-spider-arthropod-5b3aedec5225f8.0512448015305886523365.png') 
# first.iconphoto(True,ph)
# first.config(background='yellow')
# l=Label(first,image=ph,text='hello stupid !!',font=('Arial',40,'bold '),foreground='red',background='black',bd=10,padx=10,pady=20,compound=BOTTOM)
# l.pack()
# # l.place(x=150,y=250)
# ph2=ImageTk.PhotoImage(Image.open('G:\\projects\\images\\—Pngtree—red glossy button_4182376.png'))
# b=Button(first,image=ph2,compound=BOTTOM,text='click here !',font=('Times new Roman',20,'bold'),bg='purple',fg='green',padx=20,activeforeground='yellow',activebackground='black',state=ACTIVE,command=click)
# b.pack()
# first.mainloop()


# def submit():
#     user=en.get()
#     print(f'hello {user}')

# def delete():
#     en.delete(0,END)

# def back():
#     en.delete(len(en.get())-1,END)

# window=Tk()
# window.geometry('900x340+500+250')
# en=Entry(window,font=('Arial',30,'bold'),fg='yellow',bg='black')
# en.insert(0,'enter here')
# en.config(show='*')
# en.place(x=20,y=140)
# submit=Button(window,text='submit',font=('Time New Roman',9,'bold'),padx=20,pady=13,bg='black',fg='yellow',activebackground='red',activeforeground='white',command=submit)
# submit.place(x=470,y=140)
# delete=Button(window,text='delete',font=('Time New Roman',9,'bold'),padx=20,pady=13,bg='black',fg='yellow',activebackground='red',activeforeground='white',command=delete)
# delete.place(x=565,y=140)
# back=Button(window,text='backspace',font=('Time New Roman',9,'bold'),padx=20,pady=13,bg='black',fg='yellow',activebackground='red',activeforeground='white',command=back)
# back.place(x=657,y=140)
# window.mainloop()

# def c():
#     if (x.get()=='yes'):
#         print('agreed')
#     else:
#         print('disagreed')

# w=Tk()
# w.geometry('480x480+650+250')
# x=StringVar()
# w.config(background='grey')
# pp=ImageTk.PhotoImage(Image.open('G:\\projects\\images\\—Pngtree—red glossy button_4182376.png'))
# check=Checkbutton(w,text='are you sure ?',variable=x,bg='black',fg='yellow',activebackground='black',activeforeground='yellow',command=c,font=('Time New Roman',20,'bold'),padx=20,pady=10,image=pp,compound=LEFT,onvalue='yes',offvalue='no')
# check.pack(side=TOP)
# w.mainloop()

# def order():
#     if x.get()==0:
#         print(f'clicked on {food[0]}')
#     elif x.get()==1:
#         print(f'clicked on {food[1]}')
#     elif x.get()==2:
#         print(f'clicked on {food[2]}')
# food=['Pizza','Hamber','Hotdog']
# w2=Tk()
# w2.geometry('480x480+650+250')
# x=IntVar()
# for index in range(len(food)):
#     rb=Radiobutton(w2,text=food[index],variable=x,value=index,fg='black',activeforeground='black',pady=10,font=('Impact',20,'bold'),indicatoron=0,width=10,command=order)
#     rb.pack(anchor=W)
# w2.mainloop()

# def oo():
#     print(f'on {s.get()}')
# w3=Tk()
# w3.geometry('900x80+650+250')
# ppp=PhotoImage(file='G:\\projects\\images\\—Pngtree—red glossy button_4182376.png')
# l2=Label(image=ppp)
# l2.place(x=210,y=0)
# s=Scale(w3,from_=100,to=0,length=350,orient=HORIZONTAL,font=('Consolas',10,'bold'),tickinterval=10,showvalue=0,troughcolor='yellow',fg='red',bg='black')
# s.pack()
# b2=Button(w3,text='submit',bg='black',foreground='red',command=oo)
# b2.pack()
# pppp=PhotoImage(file='G:\\projects\\images\\blue-button-1428506_1280.png')
# l3=Label(image=pppp)
# l3.place(x=630)
# w3.mainloop()

# w4=Tk()
# w4.geometry('480x300+650+250')
# box=Listbox(w4,bg='black',foreground='yellow',width=28,height=5,font=('Constantia',20,'bold'),selectmode=MULTIPLE)
# box.insert(1,'Pizza')
# box.insert(2,'Hamber')
# box.insert(3,'Hotdog').
# box.insert(4,'Salad')
# box.insert(5,'Soup')
# box.pack()
# entry1=Entry(w4,font=('Arial',10,'bold'),borderwidth=5,border=5,bg='grey')
# entry1.pack()
# f=Frame(w4)
# f.pack()

# def sub():
#     food=[]
#     for i in box.curselection():
#         food.append(box.get(i))
#     print(' and '.join(food))

# def dell():
#     for i in reversed(box.curselection()):
#         box.delete(i)
#     box.config(height=box.size())

# def add():
#     box.insert(box.size(),entry1.get())
#     box.config(height=box.size())

# b1=Button(f,text='submit',command=sub)
# b1.pack(side=LEFT)
# b2=Button(f,text='add',command=add)
# b2.pack(side=LEFT)
# b3=Button(f,text='delete',command=dell)
# b3.pack(side=LEFT)
# w4.mainloop()

# def ff():
#     # messagebox.showinfo(title='info !',message='what up dude')
#     # messagebox.showwarning(title='warning',message='get out NOW!')
#     # messagebox.showerror(title='error !', message='something went wronge !!')
#     # a=messagebox.askokcancel(title='choose!',message='are you sure??')
#     # print(a)
#     # a1=messagebox.askretrycancel(title='question',message='asking')
#     # print(a1)
#     # a2=messagebox.askquestion(title='question',message='are you ok?')
#     # print(a2)
#     # a3=messagebox.askyesnocancel(title='3',message='yes or no or cancel')
#     # print(a3)
#     pass

# w5=Tk()
# w5.geometry('600x600+650+150')
# but=Button(w5,text='click here!',font=('Times New Roman',20,'bold'),fg='yellow',bg='black',activebackground='red',activeforeground='yellow',bd=10,borderwidth=5,command=ff)
# but.pack()
# w5.mainloop()

# def vv():
#     global b
#     b=colorchooser.askcolor()
#     print(b)

# w5=Tk()
# w5.geometry('600x600+650+150')
# but2=Button(w5,text='click here!',font=('Times New Roman',20,'bold'),fg='yellow',bg='black',activebackground='red',activeforeground='yellow',bd=10,borderwidth=5,command=vv)
# but2.pack() 
# w5.mainloop()

# def qq():
#     print(f"{te.get('1.0',END)}")

# w6=Tk()
# w6.geometry('600x600+650+150')
# te=Text(w6,height=8,width=20,background='black',fg='yellow',font=('Ink Free',10,'bold'))
# te.pack()
# but3=Button(w6,text='click here!',font=('Times New Roman',20,'bold'),fg='yellow',bg='black',activebackground='red',activeforeground='yellow',bd=10,borderwidth=5,command=qq)
# but3.pack()
# w6.mainloop()

# def ww():
#     A=filedialog.askopenfilename(title='entr',initialdir='C:\\Users\\kian rayaneh',filetypes=(('text files','*.txt'),('all files','*.*')))
#     B=open(A,'r')
#     print(B.read())
#     B.close()

# w7=Tk()
# w7.geometry('+650+150')
# but4=Button(w7,text='click here!',font=('Times New Roman',20,'bold'),fg='yellow',bg='black',activebackground='red',activeforeground='yellow',bd=10,borderwidth=5,command=ww)
# but4.pack()
# w7.mainloop()

# def ll():
    
#     A=filedialog.asksaveasfile(initialdir='C:\\Users\\kian rayaneh',filetypes=(('text files','.txt'),('all files','.*'),('html files','.html')),defaultextension='.txt')
#     if A is None:
#         return
#     B=str(te2.get('1.0',END))
#     A.write(B)
#     A.close()

# w8=Tk()
# w8.geometry('+650+150')
# but5=Button(w8,text='click here!',font=('Times New Roman',20,'bold'),fg='yellow',bg='black',activebackground='red',activeforeground='yellow',bd=10,borderwidth=5,command=ll)
# but5.pack()
# te2=Text(w8,font=('Constantia',10,'bold'))
# te2.pack()
# w8.mainloop()

# def opp():
#     A=filedialog.askopenfilename(initialdir='C:\\Users\\kian rayaneh',filetypes=(('text files','*.txt'),('all files','*.*')))
#     B=open(A,'r')
#     print(B.read())
#     B.close()

# def ssp():
#     A=filedialog.asksaveasfile(initialdir='C:\\Users\\kian rayaneh',filetypes=(('text files','.txt'),('all files','.*')),defaultextension='.txt')

# def rere():
#     print('hi')

# w9=Tk()
# w9.geometry('+650+150')
# me=Menu(w9)
# w9.config(menu=me)
# filem=Menu(me,tearoff=0)
# me.add_cascade(label='File',menu=filem)
# filem.add_command(label='open',command=opp)
# filem.add_separator()
# filem.add_command(label='save',command=ssp)
# viewm=Menu(me)
# me.add_cascade(label='view',menu=viewm)
# viewm.add_command(label='minimize',command=rere)#, image=pow,compound=LEFT)
# w9.mainloop()

# w10=Tk()
# w10.geometry('+650+150')
# f2=Frame(w10,background='pink',relief=SUNKEN,border=5)
# f2.pack()
# Button(f2,text='W',font=('Times New Roman',20,'bold'),fg='yellow',bg='black',activebackground='red',activeforeground='yellow',width=3).pack(side=TOP)
# Button(f2,text='A',font=('Times New Roman',20,'bold'),fg='yellow',bg='black',activebackground='red',activeforeground='yellow',width=3).pack(side=LEFT)
# Button(f2,text='S',font=('Times New Roman',20,'bold'),fg='yellow',bg='black',activebackground='red',activeforeground='yellow',width=3).pack(side=LEFT)
# Button(f2,text='D',font=('Times New Roman',20,'bold'),fg='yellow',bg='black',activebackground='red',activeforeground='yellow',width=3).pack(side=LEFT)
# w10.mainloop()

# def cw():
#     new=Toplevel()
#     new=Tk()
#     w11.destroy()
# w11=Tk()
# w11.geometry('+650+150')
# Button(w11,text='click here!',font=('Times New Roman',20,'bold'),fg='yellow',bg='black',activebackground='red',activeforeground='yellow',command=cw).pack()
# w11.mainloop()

# w12=Tk()
# w12.geometry('420x420+650+150')
# note=ttk.Notebook(w12)
# tab1=Frame(note)
# tab2=Frame(note)
# note.add(tab1,text='tab1')
# note.add(tab2,text='tab2')
# note.pack(expand=True)
# Label(tab1,text='this is one',width=50,height=20,bg='pink').pack()
# Label(tab2,text='this is two',width=50,height=20,bg='black',fg='white').pack()
# w12.mainloop()

# w13=Tk()
# w13.geometry('+650+150')
# titleinfo=Label(w13,text='enter your info',font=('Times New Roman',20,'bold')).grid(row=0,column=0,columnspan=2)
# name=Label(w13,text='first name :',font=('Arial',10,'bold'),background='red',width=15).grid(row=1,column=0)
# last=Label(w13,text='last name :',font=('Arial',10,'bold'),background='green',width=11).grid(row=2,column=0)
# email=Label(w13,text='email :',font=('Arial',10,'bold'),background='pink').grid(row=3,column=0)
# ent1=Entry(w13).grid(row=1,column=1)
# ent2=Entry(w13).grid(row=2,column=1)
# ent3=Entry(w13).grid(row=3,column=1)
# but4=Button(w13,text='submit').grid(row=4,column=0,columnspan=2)
# w13.mainloop()

# def start():
#     br['value']=0
#     gb=100
#     downlaod=0
#     speed=1
#     while downlaod<gb:
#         time.sleep(0.05)
#         br['value']+=(speed/gb)*100
#         downlaod+=speed
#         percent.set(str(int((downlaod/gb)*100))+'%')
#         tete.set(str(downlaod)+'/'+str(gb)+' GB completed')
#         w14.update_idletasks()

# w14=Tk()
# w14.geometry('420x120+650+150')
# percent=StringVar()
# tete=StringVar()
# br=Progressbar(w14,orient=HORIZONTAL,length=300)
# br.pack(pady=10)
# pl=Label(w14,textvariable=percent)
# pl.pack()
# tl2=Label(w14,textvariable=tete)
# tl2.pack()
# bl=Button(w14,text='click here!',command=start)
# bl.pack()
# w14.mainloop()

# w15=Tk()
# w15.geometry('420x420+650+150')
# c=Canvas(w15,height=400,width=400,background='black')
# c.create_line(0,0,250,250,fill='yellow',width=5)
# c.create_line(0,250,250,0,fill='red',width=5)
# c.create_rectangle(50,50,150,150,fill='yellow')
# points=[125,10,10,230,230,230]
# c.create_polygon(points,fill='yellow',outline='red',width=5)
# c.create_arc(0,0,250,250,fill='yellow',extent=100)
# c.create_oval(200,200,350,350,fill='yellow',outline='white',width=5)
# c.pack()
# w15.mainloop()

# def dst(event):
#     print(f'you pressed {event.keysym}')

# w16=Tk()
# w16.geometry('420x420+650+150')
# w16.bind('<w>',dst)
# w16.bind('<Up>',dst)
# w16.bind('<Key>',dst)
# w16.mainloop()

# def do(event):
#     print(f'you pressed {event.keysym}')
#     print(f'Mouse Coordinates: {event.x}, {event.y}')

# w17=Tk()
# w17.geometry('420x420+650+150')
# w17.bind('<Button-1>',do)
# w17.bind('<Button-2>',do)
# w17.bind('<Button-3>',do) 
# w17.bind('<ButtonRelease>',do)
# w17.bind('<Enter>',do)
# w17.bind('<Leave>',do)
# w17.bind('<Motion>',do)
# w17.mainloop()

# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y

# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x = x, y = y)


# w18 = Tk()
# w18.geometry("+1500+300")

# label1 = Label(w18, bg='red', width=10, height=5)
# label1.place(x=0, y=0)

# label2 = Label(w18, bg='blue', width=10, height=5)
# label2.place(x=100, y=100)

# label1.bind("<Button-1>", drag_start)
# label1.bind("<B1-Motion>", drag_motion)

# label2.bind("<Button-1>", drag_start)
# label2.bind("<B1-Motion>", drag_motion)

# w18.mainloop()

# def move_up(event):
#     car.place(x=car.winfo_x(),y=car.winfo_y()-10)
# def move_left(event):
#     car.place(x=car.winfo_x()-10,y=car.winfo_y())
# def move_down(event):
#     car.place(x=car.winfo_x(),y=car.winfo_y()+10)
# def move_right(event):
#     car.place(x=car.winfo_x()+10,y=car.winfo_y())

# def move_upc(event):
#     can.move(my_ph,0,-10)
# def move_leftc(event):
#     can.move(my_ph,-10,0)
# def move_downc(event):
#     can.move(my_ph,0,+10)
# def move_rightc(event):
#     can.move(my_ph,+10,0)

# w19=Tk()
# w19.geometry('420x420+650+150')

# w19.bind('<w>',move_up)
# w19.bind('<a>',move_left)
# w19.bind('<s>',move_down)
# w19.bind('<d>',move_right)
# w19.bind('<Up>',move_up)
# w19.bind('<Left>',move_left)
# w19.bind('<Down>',move_down)
# w19.bind('<Right>',move_right)

# car=Label(w19,bg='red',width=10)
# car.place(x=10,y=10)

# w19.bind('<w>',move_upc)
# w19.bind('<a>',move_leftc)
# w19.bind('<s>',move_downc)
# w19.bind('<d>',move_rightc)
# w19.bind('<Up>',move_upc)
# w19.bind('<Left>',move_leftc)
# w19.bind('<Down>',move_downc)
# w19.bind('<Right>',move_rightc)
# can=Canvas(w19,width=370,height=400,bg='light grey')
# can.pack()
# photo=PhotoImage(file='G:\\projects\\images\\—Pngtree—red glossy button_4182376.png')
# my_ph=can.create_image(0,0,image=photo,anchor=NW)
# w19.mainloop()

# w20=Tk()
# w20.geometry('+650+150')

# wi=350
# he=200

# speedx=1
# speedy=1

# space=PhotoImage(file='G:\\projects\\images\\space.png')
# ufo=PhotoImage(file='G:\\projects\\images\\ufo.png')

# ca=Canvas(w20,width=wi,height=he)
# ca.pack()

# back=ca.create_image(0,0,image=space)
# popo=ca.create_image(30,30,image=ufo)

# im_w=ufo.width()
# im_h=ufo.height()

# while True:
#     coord= ca.coords(popo)
#     if coord[0]>=(wi-im_w) or coord[0]<0 :
#         speedx= -speedx
#     if coord[1]>=(he-im_h)  or coord[1]<0:
#         speedy= -speedy
    
#     ca.move(popo,speedx,speedy)
#     w20.update()
#     time.sleep(0.01)

# w20.mainloop()

# w21=Tk()
# w21.geometry('420x420+650+150')
# wid=420
# hei=420
# speedx=1
# speedy=1
# speed2x=1
# speed2y=1
# speed3x=1
# speed3y=1
# speed4x=1
# speed4y=1
# canv=Canvas(w21,width=wid,height=hei,background='grey')
# canv.pack()
# cir1=canv.create_oval(210,420,110,320,fill='yellow',outline='black',width=3)
# cir2=canv.create_oval(300,280,400,180,fill='purple',outline='red',width=1)
# cir3=canv.create_oval(400,400,300,300,fill='red',outline='blue',width=3)
# cir4=canv.create_oval(420,150,320,50,fill='orange',outline='black',width=3)
# while True:
#     coco1=canv.coords(cir1)
#     coco2=canv.coords(cir2)
#     coco3=canv.coords(cir3)
#     coco4=canv.coords(cir4)
#     if coco1[0]>=wid-100 or coco1[0]<0:
#         speedx=-speedx
#     if coco1[1]>=hei-100 or coco1[1]<0:
#         speedy=-speedy   
#     if coco2[0]>=wid-100 or coco2[0]<0:
#         speed2x=-speed2x
#     if coco2[1]>=hei-100 or coco2[1]<0:
#         speed2y=-speed2y      
#     if coco3[0]>=wid-100 or coco3[0]<0:
#         speed3x=-speed3x
#     if coco3[1]>=hei-100 or coco3[1]<0:
#         speed3y=-speed3y      
#     if coco4[0]>=wid-100 or coco4[0]<0:
#         speed4x=-speed4x
#     if coco4[1]>=hei-100 or coco4[1]<0:
#         speed4y=-speed4y      
#     canv.move(cir1,speedx,speedy)
#     canv.move(cir2,speed2x,speed2y)
#     canv.move(cir3,speed3x,speed3y)
#     canv.move(cir4,speed4x,speed4y)
#     canv.update()
#     time.sleep(0.012)
# w21.mainloop()

# class circle:
#     def __init__(self,cana,fil,out,x,y,*args):
#         self.speedx=x
#         self.speedy=y
#         self.points=args
#         self.cana=cana
#         self.cana_cr=cana.create_oval(self.points[0],self.points[1],self.points[2],self.points[3],fill=fil,outline=out,width=3)
#     def move(self):
#         coco = self.cana.coords(self.cana_cr)
#         if coco[2]>=self.cana.winfo_width() or coco[0]<0:
#             self.speedx=-self.speedx
#         if coco[3]>=self.cana.winfo_height() or coco[1]<0:
#             self.speedy=-self.speedy
#         self.cana.move(self.cana_cr,self.speedx,self.speedy)
# w22=Tk()
# w22.geometry('420x420+650+150')
# canva=Canvas(w22,width=420,height=420,background='grey')
# canva.pack()
# cir1=circle(canva,'yellow','black',1,1,210,420,110,320)
# cir2=circle(canva,'purple','red',1,1,300,280,400,180)
# cir3=circle(canva,'red','blue',1,1,400,400,300,300)
# cir4=circle(canva,'orange','black',1,1,420,150,320,50)
# while True:
#     cir1.move()
#     cir2.move()
#     cir3.move()
#     cir4.move()
#     w22.update()
#     time.sleep(0.012)
    
# w22.mainloop()