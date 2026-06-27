import sqlite3

# connecting to database("Student.db")
conn=sqlite3.connect("Student.db")

# cursor used to run sqlite command
cursor=conn.cursor()

conn.execute("""
            
    Create table  if not exists std(
       id integer Primary Key,
       name TEXT,
       age Integer 
        
    )
             
             """)

cursor.execute("Insert into std(name,age) values(?,?)",("Ali",20))
cursor.execute("Insert into std(name,age) values(?,?)",("Ahmed",27))

# To save Changes
conn.commit()

cursor.execute("Select * From std")
rows=cursor.fetchall()

# Student records
print("Student Record")
for row in rows:
    print(row)
   
# close Connection 
conn.close()
