# import required modules
import mysql.connector

# create connection object
con = mysql.connector.connect(host="localhost", user="root",password="", database="grocery")

# create cursor object
cursor = con.cursor()

# assign data query
query1 = "desc product"

# executing cursor
cursor.execute(query1)

# display all records
table = cursor.fetchall()

# describe table
print('\n Table Description:')
for attr in table:
	print(attr)

# assign data query
query2 = "select * from product"

# executing cursor
cursor.execute(query2)

# display all records
table = cursor.fetchall()

# fetch all columns
print('\n Table Data:')
for row in table:
    print(row[0], end=" ")
    print(row[1], end=" ")
    print(row[2], end=" ")
    print(row[3], end=" ")
    print(row[4], end=" ")
    print(row[5], end=" ")
    print(row[6], end=" ")
    print(row[7], end=" ")
    print(row[8], end=" ")
    print(row[9], end="\n")
	
# closing cursor connection
cursor.close()

# closing connection object
con.close()
