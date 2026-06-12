import pandas as pd
df=pd.read_csv("student.csv")


new_students = [
    [3, "Hassan", "BSCS", 90, 88, 95],
    [4, "Ayesha", "BSIT", 78, 85, 80],
    [5, "Ali", "BSCS", 60, 70, 75],
    [6, "Sara", "BSIT", 92, 89, 94],
    [7, "Bilal", "BSCS", 55, 65, 60],
    [8, "Zain", "BSIT", 88, 84, 90],
    [9, "Maryam", "BSCS", 73, 79, 77],
    [10, "Usman", "BSIT", 81, 76, 85],
    [11, "Fatima", "BSCS", 95, 93, 97],
    [12, "Hamza", "BSIT", 68, 72, 70]
]

for students in new_students:
    df.loc[len(df)]=students
    
df.to_csv("students.csv", index=False)


df.loc[len(df)]=[13,"Inam","BSAI",70,80,90]

df.to_csv("students.csv",index=False)

# index_col used to remove by default index col
df=pd.read_csv("students.csv",index_col=0)

# use_col row is used to add particular col from file
#df=pd.read_csv("students.csv",usecols=["StudentID","Name","Class"])
#print(df.head(5)) # head use to show specific rowa col



# convertor used to connvert big symbol into small one
'''
def rename(name):
    if name=="BSIT":
        return ("IT")
    else:
        return name
    
rename("BSIT")

df=pd.read_csv("students.csv",converters={ "Class":rename})
print(df)
'''

# info() is used to check the datatypes

'''
df=pd.read_csv("student.csv").info()
print(df)'''



# =========== Example 2 ======================
import pandas as PD
df=PD.read_csv("prac2.csv")
#print(df)

df.loc[len(df)]=["103","Umer","CSAI",67,94,60,3.45]
new_data=[["104","Inam","CSAI",95,32,56,3.5],["105","Amina","BSIT",54,76,86,3.56]]
for Ndata in new_data:
        df.loc[len(df)]=Ndata
print(df)

df=PD.read_csv("prac2.csv")
print(df)