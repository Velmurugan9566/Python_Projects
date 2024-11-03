import mysql.connector
from mysql.connector import Error
from io import BytesIO
from PIL import Image
try:
    
    cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='java')
    if cnx:
        print('connect')
        print(type(cnx))
    else:
        print('not connect')

    db_Info = cnx.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = cnx.cursor() #create cursor object
    #record=cursor.execute("select database();")
    #record = cursor.fetchone()
    #print("You're connected to database: ", record)

   
    #cmd="create table class(no int(10) PRIMARY KEY,name varchar(20) NOT NULL,age int(10))"
    #res=cursor.execute(cmd)
    #print(res.rowcount)
    def insert_student():
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        course = input("Enter course: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender (Male/Female): ")
        
        cursor.execute("INSERT INTO student (id, name, course, age, gender) VALUES (%s, %s, %s, %s, %s)",
                       (student_id, name, course, age, gender))
        cnx.commit()
        print("Student inserted successfully")

    def view_students():
        cursor.execute("SELECT * FROM student")
        records = cursor.fetchall()
        for record in records:
            print("ID:", record[0], "| Name:", record[1], "| Course:", record[2], "| Age:", record[3], "| Gender:", record[4])

   
    def update_course():
        student_id = int(input("Enter the student ID to update: "))
        new_course = input("Enter new course: ")
        
        cursor.execute("UPDATE student SET course = %s WHERE id = %s", (new_course, student_id))
        cnx.commit()
        print("Course updated successfully")

   
    def delete_student():
        student_id = int(input("Enter the student ID to delete: "))
        
        cursor.execute("DELETE FROM student WHERE id = %s", (student_id,))
        cnx.commit()
        print("Student deleted successfully")

   
    while True:
        print("\nMenu:")
        print("1. Insert Student")
        print("2. View Students")
        print("3. Update Course")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            insert_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_course()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
    cursor.execute("insert into student values(110,'Velu','MCA',22,'Male')")
    print(cursor.rowcount)
    cnx.commit()
    cursor.execute("select * from student")
    res=cursor.fetchall()
    for r in res:
        print(r[0],r[1],r[2],r[3])
    print()
    '''with open('frame_0011.jpg', 'rb') as file:
            image_data = file.read()
            cursor.execute("INSERT INTO class values(110,'velu',21,%s)",(image_data, ))
            cnx.commit()
    
    # Retrieve the image from the database
    cursor.execute("SELECT pic FROM class WHERE no = 110")
    data = cursor.fetchone()[0]
    print(data)
    # Display the image
    image = Image.open(BytesIO(data))
    image.show()'''
except mysql.connector.Error as e:
    print('error: ',e)
