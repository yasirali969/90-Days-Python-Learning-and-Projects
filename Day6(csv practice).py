import pandas as pd
df=pd.read_csv("stud.csv")


def view_Student():
    print(df) 

def Add_Student():
    sid=int(input("Enter Student ID: "))
    name=input("Enter Name: ")
    clas=input("Enter Class: ")
    marks=int(input("Enter Marks: "))
    df.loc[len(df)]=[sid,name,clas,marks]
    df.to_csv("stud.csv", index=False)
    print("Student Added Successfully")
    print(df)
    
def Update_Student():
    n=int(input("Enter StudentID"))
    SName=input("Enter Student Name")
    
    df.loc[df["StudentID"]==n,"Name"]=SName
    df.to_csv("stud.csv", index=False)
    print("Data Updated Successfully")
    print(df)
        
def Delete_Student():
    global df
    
    n=int(input("Enter StudentID to delete :"))
    df=df.loc[df["StudentID"]!=n]
    df.to_csv("stud.csv", index=False)
    print("Student Deleted Succesfully")
    print(df)
    
def Total_marks():
    Total=df["SubjectMarks"].sum()
    print("Total Marks =",Total)
    
def Average_Marks():
    AVG=df["SubjectMarks"].mean()
    print("Average Marks =",round(AVG,2))

def Percentage():
    df["Percentage"] = (df["SubjectMarks"] / 100) * 100
    df.to_csv("stud.csv", index=False)
    print(df[["StudentID", "Name", "Percentage"]])



def Grade():
    df["Percentage"] = (df["SubjectMarks"] / 100) * 100
    def get_grade(Total):
        if Total>=90:
            return " Grade:A"
        elif Total>=70:
            return " Grade:B"
        elif Total>=50 :
            return " Grade:C"
        else:
         return " Grade:F"
            
    df["Grade"] = df["Percentage"].apply(get_grade)

    df.to_csv("stud.csv", index=False)

    print(df[["StudentID", "Name", "Percentage", "Grade"]])


    


        
    

while True:
    print("==================")
    print("1.View Students")
    print("2.Add Students")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Sum")
    print("6.Average")
    print("7.Percentage")
    print("8.Grade")
    print("9.Exit")
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
            Total_marks()
        case 6:
            Average_Marks()
        case 7:
            Percentage()
        case 8:
            Grade()
        case 9:
            print("Program Terminated!")
            break
        