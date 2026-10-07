import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="viru8000@",
    database="smart_routh_map"
)

cursor = connection.cursor()

print("Database connected successfully")