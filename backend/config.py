# import os

# # Path to the data directory
# DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")

# # Mapping of database keys to their actual SQLite file paths
# DATABASES = {
#     "students": os.path.join(DATA_DIR, "students.db"),
#     "teachers": os.path.join(DATA_DIR, "teachers.db"),
#     "grades": os.path.join(DATA_DIR, "grades.db"),
#     "attendance": os.path.join(DATA_DIR, "attendance.db"),
# }

# # Optional: You can still keep table schemas for UI/documentation
# TABLE_SCHEMAS = {
#     "students": {
#         "columns": ["student_id", "name", "department", "year", "email"],
#         "types": ["int", "str", "str", "int", "str"],
#         "example_row": [101, "Alice", "ISE", 3, "alice@nmit.ac.in"],
#         "description": "List of students with department, year, and contact email."
#     },
#     "teachers": {
#         "columns": ["teacher_id", "name", "subject", "email"],
#         "types": ["int", "str", "str", "str"],
#         "example_row": [201, "Dr. Smith", "Machine Learning", "smith@nmit.ac.in"],
#         "description": "List of teachers along with subject taught and email."
#     },
#     "grades": {
#         "columns": ["student_id", "subject", "score"],
#         "types": ["int", "str", "float"],
#         "example_row": [101, "DBMS", 89.5],
#         "description": "Marks/grades scored by students in various subjects."
#     },
#     "attendance": {
#         "columns": ["student_id", "date", "status"],
#         "types": ["int", "str", "str"],
#         "example_row": [101, "2025-08-01", "Present"],
#         "description": "Student attendance records by date."
#     }
# }

import os

# MySQL connection details
MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "MySQL2025!",
    "database": "classicmodels"
}

# Table schemas for UI/documentation (unchanged)
# TABLE_SCHEMAS = {
#     "students": {
#         "columns": ["student_id", "name", "department", "year", "email"],
#         "types": ["int", "str", "str", "int", "str"],
#         "example_row": [101, "Alice", "ISE", 3, "alice@nmit.ac.in"],
#         "description": "List of students with department, year, and contact email."
#     },
#     "teachers": {
#         "columns": ["teacher_id", "name", "subject", "email"],
#         "types": ["int", "str", "str", "str"],
#         "example_row": [201, "Dr. Smith", "Machine Learning", "smith@nmit.ac.in"],
#         "description": "List of teachers along with subject taught and email."
#     },
#     "grades": {
#         "columns": ["student_id", "subject", "score"],
#         "types": ["int", "str", "float"],
#         "example_row": [101, "DBMS", 89.5],
#         "description": "Marks/grades scored by students in various subjects."
#     },
#     "attendance": {
#         "columns": ["student_id", "date", "status"],
#         "types": ["int", "str", "str"],
#         "example_row": [101, "2025-08-01", "Present"],
#         "description": "Student attendance records by date."
#     }
# }