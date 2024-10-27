import mysql.connector
from mysql.connector import Error
from io import BytesIO
from PIL import Image
try:
    
    cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='python')
    if cnx:
        print('connect')
        print(type(cnx))
    else:
        print('not connect')

    db_Info = cnx.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = cnx.cursor() #create cursor object
    record=cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)


    #cmd="create table class(no int(10) PRIMARY KEY,name varchar(20) NOT NULL,age int(10))"
    #res=cursor.execute(cmd)
    #print(res.rowcount)

    #cursor.execute("insert into class values(117,'anand',21)")
    #print(cursor.rowcount)
    #cnx.commit()
    cursor.execute("select * from class")
    res=cursor.fetchall()
    for r in res:
        print(r[0],r[1],r[2],r[3])
    print()
    '''with open('frame_0011.jpg', 'rb') as file:
            image_data = file.read()
            cursor.execute("INSERT INTO class values(110,'velu',21,%s)",(image_data, ))
            cnx.commit()'''
    
    # Retrieve the image from the database
    cursor.execute("SELECT pic FROM class WHERE no = 110")
    data = cursor.fetchone()[0]
    print(data)
    # Display the image
    image = Image.open(BytesIO(data))
    image.show()
except mysql.connector.Error as e:
    print('error: ',e)
