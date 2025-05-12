import mysql.connector  
  
myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = 'kambok1', database = "infotech")  

cur = myconn.cursor()
