import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="13579",database="College")
mc=db.cursor()
#mc.execute("Create table Student(Name varchar(255), Regno int(10), Grade varchar(2))")
#mc.execute("ALTER TABLE Student ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#mc.execute("INSERT INTO Student(Name,Regno) VALUES(\"Shannu\",2),(\"Nishan\",3)")
#mc.execute("INSERT INTO Student(Name,Regno) VALUES(\"Nisha\",4)")

#db.commit()
#print(mc.rowcount,"inserted")
#mc.execute("SELECT * FROM Student where name='Dhara'")
mc.execute("SELECT * FROM Student order by Name")
result=mc.fetchone()

for x in result:
    print(result)
