        # Student Managment System


def AddStudent():
    student={"Name":"Hassan","Age":32,"Class":6}
    List.append(student)
    print("Student Added")

def ViewStudent(List):
   for student in List:
    print(student)
    print("\n")

def SearchStudent(Name,List):
  for student in List:
    if student['Name'] in Name:
        print("Found")
        print(student)
    
print("Not Found")



List=[{"Name":"Yasir","Age":31,"Class":5}, 
    {"Name": "Fahad", "Age": 20, "Class": 12},
    {"Name": "Asad", "Age": 19, "Class": 11},
    {"Name": "Umer", "Age": 21, "Class": 13},
    {"Name": "Ali", "Age": 18, "Class": 10},
    {"Name": "Ahmed", "Age": 22, "Class": 14}]



while True:
    print("==========Menu=========")
    print("1.Add Student")
    print("2.View Student")
    print("3.Search Students")
    print("4.Exit")
    print("=======================")

    
    choice=int(input("Enter the choice"))

    match choice:

      case 1:
        AddStudent()
      case 2:
        ViewStudent(List)
      case 3:
        name=input("Enter the name of Student")
        SearchStudent(name,List)
      case 4:
        "Thank you for Using S.M.S"



            # Quiz Game

name=input("Enter UserName :")
score=0


Quiz=[{"question":"Q1: What is the Capital of Pakistan",
       "Options":["1)Islamabad","2)Peshawar","3)Quetta","4)Karachi"],
       "answer":"Islamabad"},
      {
    "question": "Q2: Who is known as the father of computers?",
    "Options": ["1)Alan Turing", "2)Charles Babbage", "3)Bill Gates", "4)Steve Jobs"],
    "answer": "Charles Babbage"
    },
   {
    "question": "Q3: How many provinces are there in Pakistan?",
    "Options": ["1)3", "2)4", "3)5", "4)6"],
    "answer": "4"
   }]
    
for q in Quiz:
        print(q["question"])
        for option in q["Options"]:
           print(option)
        
        print("==================")   
        n=input("Enter the Answer :")
        
        if n==q["answer"]:
                print("Correct!")
                score=score+1
        else :
                print("Incorrect!")
        print("===================")
print("========= Game Summary =========")
print("Player Name :",name)
print("Score :",score)
print("================================")        
    
  

      
