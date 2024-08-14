# import sqlite3

# new_c=sqlite3.connect('test.db')
# new2=new_c.cursor()
# new3="SELECT datetime('now','localtime');"
# new2.execute(new3)
# print(new2.fetchone()) 

# with sqlite3.connect('test.db') as new_c:
#     new2=new_c.cursor()
#     print(new2.execute("SELECT datetime('now','localtime');").fetchone()[0])

# new2.execute('DROP TABLE IF EXISTS firstone')
# new2.execute('CREATE TABLE firstone(name TEXT,num INT);') 

# new2.execute("INSERT INTO firstone VALUES('masud', 14)")
# new_c.commit()
# new2.execute("SELECT * FROM firstone;")
# print(new2.fetchone())

# new2.execute("UPDATE firstone set num=10 WHERE name = 'masud'")
# new_c.commit()
# new2.execute("SELECT * FROM firstone;")
# print(new2.fetchone())

# new2.execute("DELETE FROM firstone WHERE name = 'masud'")
# new_c.commit()
# new2.execute("SELECT * FROM firstone;")
# print(new2.fetchone())

# values=(('ronaldo',7),('messi',20),('haaland',9))
# new2.executemany("INSERT INTO firstone VALUES(?, ?)",values)
# new_c.commit()
# new2.execute("SELECT * FROM firstone;")
# print(new2.fetchall())