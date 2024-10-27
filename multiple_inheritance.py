#program for multiple Inheritance and  polymorphic functions 
class Shapes: #base Class
   def define(self):
       print('...Program to fine Area of Rectangle,Square,Triangle...')
class Rectangle(Shapes): #Derived Class
    def calculate_area(self,length,width):
        print('Area of the Rectangle: ',length * width)

class Square(Shapes):#Derived Class

    def calculate_area(self,side):#method Overriding 
        print('Area of the Square:',side * side)

class Triangle(Shapes):#Derived Class
    def calculate_area(self,base,height):
        print('Area of the Triangle:',0.5 * base * height)

# Object Creation:
r= Rectangle()
s = Square()
t = Triangle()
#function Calling
r.define()
r.calculate_area(5,4)
s.calculate_area(6)
t.calculate_area(10,15)


