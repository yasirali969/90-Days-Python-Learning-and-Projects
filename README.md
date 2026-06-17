# Day 1 - Python Basics(Lists)

Today I learned the fundamentals of Python programming. I practiced working with variables, lists, functions, and the random module.

## Topics Covered

* Variables and data storage

* Lists and list operations

* Accessing elements using indexes

* Searching for elements in a list

* Adding and removing list items

* Sorting and reversing lists

* Finding maximum and minimum values

* Creating and calling functions

* Using the random module

## Practice Tasks

* Selected a random name from a list

* Retrieved values using indexes

* Checked whether an item exists in a list

* Added and removed elements from a list

* Updated list values

* Counted occurrences of elements

* Sorted and reversed a list

* Created a simple function that returns a string

## Key Learning

I learned how to store multiple values in a list and manipulate them using built-in Python methods. I also learned how functions help organize code and make it reusable.

# Day 2 - Python Dictionaries

Today I learned about Python dictionaries, a powerful data structure used to store information in key-value pairs. Dictionaries make it easy to organize, access, update, and manage data efficiently.

## Topics Covered

* Creating dictionaries


* Accessing values using keys

* Using the `get()` method

* Adding new key-value pairs

* Updating existing values

* Removing items with `pop()`

* Checking if a key exists

* Looping through dictionaries

* Using `keys()`, `values()`, and `items()`

* Finding the length of a dictionary

* Working with nested dictionaries

## Practice Tasks

* Created a student information dictionary

* Retrieved values using keys

* Added and updated student details

* Removed dictionary entries

* Checked for the existence of keys

* Displayed dictionary contents using loops

* Worked with nested dictionaries to store multiple students


## Key Learning

I learned how dictionaries store data using key-value pairs and how they are more suitable than lists when information needs to be accessed using meaningful names instead of numeric indexes. Dictionaries are commonly used in real-world applications to represent structured data such as user profiles, product details, and database records.


# Day 3 Practice(Lists,Dictionary,loops,Conditions)

# Quiz Game (Python)

This is a simple **console-based Quiz Game** built using Python. The game tests the user's general knowledge and keeps track of the score.

## Features

* Multiple-choice questions

* Score tracking system

* Instant feedback (Correct / Incorrect)

* Final score summary

* User-friendly console interface

## Concepts Used

* Lists of dictionaries

* Loops (`for`)

* Conditional statements (`if-else`)

* User input

* Score calculation

## How It Works

The quiz contains a list of questions. Each question has:

* Question text

* Multiple options

* Correct answer

The program:

1. Displays each question

2. Takes user input

3. Checks the answer

4. Updates the score

At the end, it shows:

* Player name

* Final score

## Learning Outcome

This project improved my understanding of loops, condition checking, and how to structure small interactive applications in Python.


# Student Management System (Python)

This project is a simple **console-based Student Management System** built using Python. It helps manage student records using lists and dictionaries.

## Features

* Add new student

* View all students

* Search student by name

* Menu-driven system using loops

* Uses functions for better code organization

## Concepts Used

* Lists

* Dictionaries

* Functions

* Loops (`while`, `for`)

* Conditional statements (`match-case`)

* User input handling

## How It Works

The program stores student data in a list of dictionaries. Each student has:

* Name

* Age

* Class

Users can interact with the system through a menu:

1. Add Student → Adds a new student to the list

2. View Students → Displays all student records

3. Search Student → Finds a student by name

4. Exit → Stops the program

## Learning Outcome

This project helped me understand how real-world applications manage data using basic Python structures like lists and dictionaries, and how menu-driven programs work.


# Day 4 - Sets and Tuples in Python

Today I learned about Sets and Tuples, two important data structures in Python used to store collections of data.

## Topics Covered

## Sets

*Creating sets

* Adding elements with add()

* Removing elements with remove()

* Checking membership using in

* Removing duplicate values

* Union, Intersection, and Difference operations

* Iterating through sets

### Tuples

* Creating tuples

* Accessing tuple elements

* Tuple slicing

* Iterating through tuples

* Using `count()` and `index()`

* Understanding tuple immutability

* Converting tuples to lists and vice versa


## Key Learning

I learned the difference between mutable and immutable data structures. I learned that sets are useful for storing unique values and performing mathematical set operations, while tuples provide an immutable way to store data that should not be modified.




# Day 5 - CSV Files and Pandas

Today I learned how to work with CSV files using the Pandas library in Python. I practiced reading data from CSV files, modifying records, adding new rows, and saving updated data back to CSV files.

## Topics Covered

### CSV Files

* Reading CSV files
* Writing data to CSV files
* Updating existing records
* Saving modified data

### Pandas DataFrame

* Creating and loading DataFrames
* Using `read_csv()`
* Using `to_csv()`
* Adding rows with `loc`
* Viewing data with `head()`
* Understanding `index_col`
* Selecting specific columns with `usecols`
* Using custom converters
* Viewing dataset information with `info()`

## Practice Tasks

* Loaded student records from CSV files
* Added multiple student records to a DataFrame
* Saved updated records to a new CSV file
* Removed the default index column
* Displayed selected columns from a dataset
* Used converters to modify column values during import
* Examined data types using `info()`

## Key Learning

I learned how Pandas simplifies working with tabular data. CSV files can be used to store and manage structured information such as student records, and Pandas provides powerful tools for reading, updating, filtering, and analyzing this data efficiently.

## Technologies Used

* Python
* Pandas
* CSV Files

## Skills Gained

* Data Manipulation
* File Handling
* Working with DataFrames
* Data Import and Export
* Basic Data Analysis

# Day 6: 📚 Student Management System (Python + Pandas)

## 📌 Overview

The Student Management System is a Python-based console application that uses the Pandas library to manage student records stored in a CSV file. It allows users to perform various operations such as adding, updating, deleting, and viewing student information, as well as calculating marks, percentages, and grades.

---

## 🚀 Features

* 👨‍🎓 View all student records
* ➕ Add a new student
* ✏️ Update existing student information
* ❌ Delete a student record
* 📊 Calculate total marks
* 📈 Calculate average marks
* 📝 Generate percentage for each student
* 🏆 Assign grades automatically
* 💾 Store and update data in a CSV file

---

## 🛠️ Technologies Used

* Python 3
* Pandas Library
* CSV File Handling

---

## 📂 Project Structure

```text
Student-Management-System/
│
├── stud.csv          # Student data file
├── main.py           # Main application code
└── README.md         # Project documentation
```

---

## 📋 CSV File Format

The `stud.csv` file should contain the following columns:

| StudentID | Name  | Class | SubjectMarks |
| --------- | ----- | ----- | ------------ |
| 101       | Ali   | BSCS  | 85           |
| 102       | Ahmed | BSIT  | 78           |

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/student-management-system.git
```

2. Navigate to the project folder:

```bash
cd student-management-system
```

3. Install Pandas:

```bash
pip install pandas
```

4. Run the program:

```bash
python main.py
```

---

## 🎯 Menu Options

```text
1. View Students
2. Add Students
3. Update Student
4. Delete Student
5. Sum
6. Average
7. Percentage
8. Grade
9. Exit
```

---

## 📊 Grade Criteria

| Percentage    | Grade |
| ------------- | ----- |
| 90% and Above | A     |
| 70% - 89%     | B     |
| 50% - 69%     | C     |
| Below 50%     | F     |

---

## 📸 Sample Output

```text
==================
1.View Students
2.Add Students
3.Update Student
4.Delete Student
5.Sum
6.Average
7.Percentage
8.Grade
9.Exit
==================

Enter the choice : 1
```

---

## 🔮 Future Improvements

* Search Student by ID
* Multiple Subject Support
* GUI Version using Tkinter
* Database Integration (MySQL)
* Student Ranking System
* Export Reports to Excel

---

## 👨‍💻 Author

**Yasir Ali Sajjad Ahmad**

Feel free to contribute, fork, and improve this project.



# Day 7 : FUll Project- Student Management System (Python + Pandas)

## 📌 Overview

The Student Management System is a console-based Python application developed using the Pandas library for managing student records efficiently. It allows users to perform CRUD operations, calculate academic performance, generate reports, and analyze student data stored in a CSV file.

## 🚀 Features

### Student Management

* View all student records
* Add new students
* Update existing student information
* Delete student records
* Search students by name

### Academic Analysis

* Calculate Total Marks
* Calculate Average Marks
* Calculate Percentage
* Generate Grades (A, B, C, D, F)
* Display Top 3 Toppers
* Display Bottom 3 Weak Students

### Reports & Statistics

* Subject-wise Average Analysis
* Class-wise Performance Comparison
* Final Academic Report

  * Total Students
  * Average Percentage
  * Highest Percentage
  * Lowest Percentage

## 🛠 Technologies Used

* Python
* Pandas
* CSV File Handling

## 📂 Project Structure

StudentManagementSystem/
│
├── Students.csv
├── student_management.py
└── README.md

## 📊 Student Data Fields

| Field       | Description                       |
| ----------- | --------------------------------- |
| StudentID   | Unique Student ID                 |
| Name        | Student Name                      |
| Class       | Student Class                     |
| Programming | Programming Subject Marks         |
| Database    | Database Subject Marks            |
| OOP         | Object-Oriented Programming Marks |

## 📈 Grade Criteria

| Percentage | Grade |
| ---------- | ----- |
| 90 - 100   | A     |
| 80 - 89    | B     |
| 70 - 79    | C     |
| 60 - 69    | D     |
| Below 60   | F     |

## ▶️ How to Run

1. Install Pandas:

```bash
pip install pandas
```

2. Place `Students.csv` in the project folder.

3. Run the program:

```bash
python student_management.py
```

## 🎯 Learning Outcomes

This project demonstrates:

* Python Functions
* Pandas DataFrame Operations
* CSV File Handling
* Data Analysis
* CRUD Operations
* Conditional Statements
* Sorting & Filtering
* GroupBy Operations
* Academic Report Generation

## 👨‍💻 Author

**Yasir Ali Sajjad Ahmad**

Aspiring Software Engineer | Python Developer | Data Analysis Enthusiast

## ⭐ Future Enhancements

* GUI using Tkinter
* Student Login System
* Attendance Management
* Database Integration (MySQL)
* Data Visualization using Matplotlib
* Export Reports to Excel/PDF

# Day 8: 🧮 Tkinter Calculator

A simple yet functional GUI Calculator built using Python’s Tkinter library.
It performs basic arithmetic operations with an easy-to-use graphical interface.

## ✨ Features
➕ Addition

➖ Subtraction

✖️ Multiplication

➗ Division

🧹 Clear screen (C button)

🖥️ Clean and responsive GUI

⚡ Lightweight and fast execution

🛠️ Tech Stack

## Tools :

Python 🐍
Tkinter (Python GUI Library)

## 👨‍💻 Author
Yasir Ali Sajjad Ahmad
Python & GUI Developer 


# Day 9 - Login Form Using Tkinter
## 📌 Project Overview

A simple Login Form built using Python Tkinter GUI. This project demonstrates the fundamentals of creating graphical user interfaces, handling user input, and validating login credentials.

## 🚀 Features
User-friendly graphical interface

Username and Password input fields

Login button functionality

Basic credential validation

Error and success message display

Clean and responsive Tkinter layout
## 🛠️ Technologies Used
Python

Tkinter

## 📂 Learning Outcomes

Through this project, I learned:

Creating GUI applications with Tkinter

Using Labels, Entry Widgets, and Buttons

Managing widget placement with Geometry Managers

Handling user events and button clicks

Implementing basic login validation logic
