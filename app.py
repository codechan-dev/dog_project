# core code for dog project
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()
print("1.create\t2.display\t3.drop table\t4.insert")
op=int(input("enter your oprion :"))

if(op==1):
    mycursor.execute("CREATE TABLE dogs (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), state VARCHAR(255),used VARCHAR(255))")

elif(op==2):

    mycursor.execute("SELECT * FROM dogs")

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)
elif(op==3):
    sql = "DROP TABLE dogs"

    mycursor.execute(sql)
elif(op==4):
    
    a=input("enter dog name:")
    b=input("enter dog state")
    c=input("enter uses")

    sql = "INSERT INTO dogs (name, state,used) VALUES (%s, %s,%s)"
    val = [
      (a, b,c),
    ]

    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")