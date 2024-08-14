# from tkinter import *
# import sqlite3
# from random import randint
# import pyglet


# pyglet.font.add_file('G:\\projects\\fonts\\Ubuntu-Bold.ttf')
# pyglet.font.add_file('G:\\projects\\fonts\\Shanti-Regular.ttf')

# def load1():
#     clear(window)
#     window.config(background='#5B5B5B')
#     photo=PhotoImage(file='G:\\projects\\images\\RRecipe_logo.png')
#     photo.image= photo
#     la=Label(window,image=photo,bg='#5B5B5B',fg='white')
#     la.pack()
#     la2=Label(window,text='ready for your random recipe?',bg='#5B5B5B',font=('Shanti',15,'bold'),fg='white')
#     la2.pack()
#     bu=Button(text='SHUFFLE',bg='black',fg='white',font=('Ubuntu',25,'bold'),activebackground='#badee2',cursor='hand2',command=load2)
#     bu.pack(pady=15)

# def clear(window):
#     for i in window.winfo_children():
#         i.destroy()

# def load2():
#     clear(window)
#     a=fetch_db()
#     b=prosses(a[0],a[1])
#     window.config(background='#5B5B5B')
#     logo=PhotoImage(file='G:\\projects\\images\\RRecipe_logo_bottom.png')
#     la3=Label(window,image=logo,background='#5B5B5B')
#     la3.pack(pady=15)
#     la3.image=logo
#     la4=Label(window,text=b[0],background='#5B5B5B',font=('Times New Roman',18,'bold'),fg='white')
#     la4.pack()
#     la5=Label(window,text='\n'.join(b[1]),font=('Arial',12),fg='white',bg='black',pady=10,padx=40)
#     la5.pack(pady=15)
#     bu2=Button(text='BACK',bg='black',fg='white',font=('Arial',15,'bold'),activebackground='#badee2',cursor='hand2',command=load1)
#     bu2.pack(pady=10)

# def fetch_db():
#     new=sqlite3.Connection('G:\\projects\\data\\recipes.db')
#     new2=new.cursor()
#     new2.execute("SELECT * FROM sqlite_schema WHERE type='table'")
#     all=new2.fetchall()
#     name=all[randint(0,len(all)-1)][1]
#     new2.execute(f"SELECT * FROM {name};")
#     data=new2.fetchall()
#     return name,data

# def prosses(name,data):
#     title=name[:-6]
#     title=''.join([i if i.islower() else ' '+i for i in title])
#     txt=[]
#     for i in data:
#         nam=i[1]
#         qty=i[2]
#         unit=i[3]
#         txt.append(f'{qty} {unit} of {nam}') 
#     return title,txt

# window=Tk()
# window.geometry('400x550+500+170')
# load1()
# window.mainloop() 