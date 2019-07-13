import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM em_table_users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)