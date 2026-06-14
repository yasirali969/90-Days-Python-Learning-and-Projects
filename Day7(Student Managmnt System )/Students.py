import pandas as Pd
Df=Pd.read_csv("Students.csv")
Df["StudentID"] = Df["StudentID"].astype(int)


def view_Student():
    print(Df)
    
def Add_Student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    clas = input("Enter Class: ")

    prog =int(input("Enter Programming Marks: "))
    db =int(input("Enter Database Marks: "))
    oop =int(input("Enter OOP Marks: "))
    
    if prog<0 or prog>100:
        print("Invalid Programming Marks")
        return

    if db<0 or db>100:
        print("Invalid Database Marks")
        return

    if oop<0 or oop>100:
        print("Invalid OOP Marks")
        return

    Df.loc[len(Df), ["StudentID", "Name", "Class", "Programming", "Database", "OOP"]]  = [sid, name, clas, prog, db, oop]

    Df.to_csv("Students.csv", index=False)

    print("Student Added Successfully")   
    
def Update_Student():
    n=int(input("Enter the StudentID :"))
    name=input("Enter the Updated Name :")
    
    Df.loc[Df["StudentID"]==n,"Name"]=name 
    Df.to_csv("Students.csv",index=False)
    print("Student Updated Successfully")
    print(Df)

def Delete_Student():
    global Df
    
    N=int(input("Enter the studentid to be deleted :"))
    Df=Df.loc[Df["StudentID"]!=N]
    Df.to_csv("Students.csv",index=False)
    print("Student Deleted Successfully!")
    print(Df)
    
def Search_Student():
    name=input("Enter the Stud_Name to Find :")
    
    res=Df[Df["Name"]==name]
    
    if res.empty:
        print("Not Found!")
    else:
        print("Found!")
        print(res)
    
def Total_marks():
    
    Df["Total_Sum"]=Df["Programming"]+Df["Database"]+Df["OOP"]
    Df.to_csv("Students.csv",index=False)
    print(Df)
    
def Average_Marks():
    Df["Total_Sum"]=Df["Programming"]+Df["Database"]+Df["OOP"]
    Df["Average"]=round(Df["Total_Sum"]/3,2)
    Df.to_csv("Students.csv",index=False)
    print(Df)
    

def Percentage():
    Df["Total_Sum"]=Df["Programming"]+Df["Database"]+Df["OOP"]
    Df["Percentage"]=round((Df["Total_Sum"]/300)*100,2)
    Df.to_csv("Students.csv",index=False)
    print(Df)

def Grade():

    def get_grade(p):
        if p >= 90:
            return "A"
        elif p >= 80:
            return "B"
        elif p >= 70:
            return "C"
        elif p >= 60:
            return "D"
        else:
            return "F"

    Df["Grade"] = Df["Percentage"].apply(get_grade)

    Df.to_csv("Students.csv", index=False)

    print(Df)


def Toppers():
    sorted_df=Df.sort_values(by="Percentage", ascending=False)
    print(sorted_df[["StudentID", "Name", "Percentage"]].head(3))

def Weak_Students():
    sorted_df=Df.sort_values(by="Percentage", ascending=True)
    print(sorted_df[["StudentID", "Name", "Percentage"]].head(3))

def SubjectWise_Avg():
    n=input("Enter the Name of Subject:")
    if n=="OOP":
        OOP_Average=Df["OOP"].mean()
        print("OOP_Average =",OOP_Average)
        
    elif n=="Programming":
        Prog_Average=Df["Programming"].mean()
        print("Prog_Average =",Prog_Average)
    elif n=="Database":
        DB_Average=Df["Database"].mean()
        print("DB_Average =",DB_Average)
    else:
        print("Subject Does not Exist!")
        
def ClassWise_Compare():
    result = Df.groupby("Class")["Percentage"].mean()
    print(result)
    

def Report():
    print("Total Students:", len(Df))
    print("Average Percentage:", Df["Percentage"].mean())
    print("Highest Percentage:", Df["Percentage"].max())
    print("Lowest Percentage:", Df["Percentage"].min())

        


while True:
    print("==================")
    print("1.View Students")
    print("2.Add Students")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Search Student")
    print("6.Sum")
    print("7.Average")
    print("8.Percentage")
    print("9.Grade")
    print("10.Toppers")
    print("11.Weak Students")
    print("12.Subject Wise Average")
    print("13.Class_Wise Comparison")
    print("14.Final Report")
    print("15.Exit")
    print("==================")


    choice=int(input("Enter the choice :"))
    match choice:
        case 1:
            view_Student()
        case 2:
            Add_Student()
        case 3:
            Update_Student()
        case 4:
            Delete_Student() 
        case 5:
            Search_Student() 
        case 6:
            Total_marks()
        case 7:
            Average_Marks()
        case 8:
            Percentage()
        case 9:
            Grade()
        case 10:
            Toppers()
        case 11:
            Weak_Students()
        case 12:
            SubjectWise_Avg()
        case 13:
            ClassWise_Compare()
        case 14:
            Report()
        case 15:
            print("Program Terminated!")
            break
      
        