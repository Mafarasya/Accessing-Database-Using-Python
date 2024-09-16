import pandas as pd
import sqlite3
 
# create and connect our process to a new database STAFF
conn = sqlite3.connect('STAFF.db')

# Define Table Name
table_name = 'INSTRUCTOR'
dep_table_name = 'Departments'

# Define Attribute list
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']
dep_attribute_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

# Define file path
file_path = './INSTRUCTOR.csv'
dept_file_path = './Departments.csv'

df = pd.read_csv(file_path, names=attribute_list)
df_dept = pd.read_csv(dept_file_path, names=dep_attribute_list)

df.to_sql(table_name, conn, if_exists='replace', index=False)
df_dept.to_sql(dep_table_name, conn, if_exists='replace', index=False)

print("Table is ready")

# Viewing the data in the table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing FNAME
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing total numbers of entries in the table
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Departments - Viewing all data
query_statement = f"SELECT * FROM {dep_table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


# Appending some data into table
# INSTRUCTOR
data_dict = {'ID': [100], 'FNAME': ['John'], 'LNAME': ['Doe'], 'CITY': ['Paris'],
             'CCODE': ['FR']}
data_append = pd.DataFrame(data_dict)

# Departments
dep_data_dict = {'DEPT_ID': [9], 'DEP_NAME': ['Quality Assurance'], 'MANAGER_ID': [9], 'LOC_ID': ['L0010']}
dep_data_append = pd.DataFrame(dep_data_dict)

# append to db
# INSTRUCTOR
data_append.to_sql(table_name, conn, if_exists='append', index=False)
print("Data appended successfully")

# Departments
dep_data_append.to_sql(dep_table_name, conn, if_exists='append', index=False)
print("Departments Data Appended Successfuly")


