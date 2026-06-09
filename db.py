import sqlite3

con=sqlite3.connect('users.db')
def insertData(name,city,age):
    qrt="insert into users(NAME,CITY,AGE) values(?,?,?);"
    con.execute(qry,(name,city,age))
    con.commit()
    print("user details Added")
    
def updateData(name,city,age,id):
    qrt="update users set NMAE=?,CITY=?,AGE=? where id=?;"
    con.execute(qry,(name,city,age,id))
    con.commit()
    print("user details update")
    
def deleteData(id):
    qrt="delete from user where id=?;"
    con.execute(qry,(id))
    con.commit()
    print("user details deleted")
    
def selectData():
    qry="select * from users"
    result=con.execute(qry)
    for row in result:

print("""
1.INSERT
2.UPDATE
3.DELETE
4.SELECT
""")

ch=1
while ch==1:
    c=int(input("select your choice : "))
    if(c==1):
        print("add new record")
        name=input("Enter a name : ")
        city=input("Enter a city : ")
        age=int(input("Enter a age : "))
    elif(c==2):
        print("edit a record")
        id=int(input("Enter a id :"))
        name=input("Enter a name : ")
        city=input("Enter a city : ")
        age=int(input("Enter a age : "))
        updateData(name,city,age,id)
    elif(c==3):
        print("delete a record")
        id=int(input("Enter a id :"))
        deleteData(id)
    elif(c==4):
        print("print all data")
        selectData()
    else:
        print("invalid selection")
    ch=int(input("Enter 1 to continue : "))
print("Thank you")