import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="13579",database='new')

#to fetch all database
mycursor=db.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
mycursor.execute("use new")
mycursor.execute("create table info(name varchar(50),age varchar(3), gender char(1),dob date)")
mycursor.execute("Describe info")

'''
#fetch the information from the table
mycursor.execute("select * from ")
for i in mycursor:
    print(i)
    '''
'''
# fetachall function
mycursor.execute("select * from me")
res=mycursor.fetchall()
for i in res:
    print(i)
# fetchone function
mycursor.execute("select * from me")
res=mycursor.fetchone()
for i in res:
    print(i)
'''
#show table
'''
mycursor.execute("show tables")
for i in mycursor:
    print(i)
'''
