import mysql.connector  
  
myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = 'kambok1', database = "infotech")  

cur = myconn.cursor()

# create
# cur.execute("create table customers(id int auto_increment primary key, name varchar(20), address varchar(20))")

cur.execute("drop table if exists office")

# read
# cur.execute("show tables")
# for x in cur:
#     print(x)


# create
# sql = "insert into customers(name, address) values(%s, %s)"
# val = [("john", "Garki"), ("sam", "Wuse 2"), ("dan", "Gwagwalada"), ("mark", "Jabi"), ("peter", "Maitama")]
# cur.executemany(sql, val)
# myconn.commit()

# cur.execute("delete from customers where id = 4")
# myconn.commit()



