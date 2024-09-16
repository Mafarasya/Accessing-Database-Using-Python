# STAFF Database Project

## Project Overview
This project demonstrates how to create a database named **STAFF**, load data from CSV files into tables, and run basic SQL queries using Python. The project involves managing employee and department records in a structured way.

## Objectives
- Create a database using Python.
- Load data from a CSV file into a database table.
- Run basic queries on the database to retrieve and manipulate data.

## Steps Involved

### 1. Database Creation
- Created the **STAFF** database using Python and SQLite.

### 2. Loading Data from CSV
- Loaded employee data from a CSV file into a table named **INSTRUCTORS**.
- The CSV file contains the following headers:
  - `ID`: Employee ID
  - `FNAME`: First Name
  - `LNAME`: Last Name
  - `CITY`: City of residence
  - `CCODE`: Country code (2 letters)

### 3. Departments Table
- Created another table named **Departments** with the following attributes:
  - `DEPT_ID`: Department ID
  - `DEP_NAME`: Department Name
  - `MANAGER_ID`: Manager ID
  - `LOC_ID`: Location ID
- Populated the **Departments** table with data from a CSV file.

### 4. Appending Data
- Appended the **Departments** table with the following new record:
  - `DEPT_ID`: 9
  - `DEP_NAME`: Quality Assurance
  - `MANAGER_ID`: 30010
  - `LOC_ID`: L0010

### 5. Running Queries on the Departments Table
- Executed the following SQL queries:
  1. View all entries: `SELECT * FROM Departments;`
  2. View only department names: `SELECT DEP_NAME FROM Departments;`
  3. Count the total number of entries: `SELECT COUNT(*) FROM Departments;`

## Technologies Used
- Python
- SQLite
- CSV (Comma-Separated Values)

## How to Run the Project
1. Clone the repository.
2. Ensure Python and SQLite are installed.
3. Run the Python script to create the database and tables, load the data, and execute the SQL queries.

## Author
This project was completed as part of learning how to create and manage databases using Python.
