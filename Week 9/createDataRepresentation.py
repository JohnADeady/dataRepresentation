# Import mysql connector
import mysql.connector 
 
# credentials for account
mydb = mysql.connector.connect(   
	host="127.0.0.1",   
	user="root",   
	password="Bruree06",
	auth_plugin='mysql_native_password',
	database="datarepresentation")
 
 
mycursor = mydb.cursor() 

# create student table
sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)" 
# execute to mysql
mycursor.execute(sql) 