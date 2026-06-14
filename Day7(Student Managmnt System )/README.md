## Full Student Management System (Python + Pandas)

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
