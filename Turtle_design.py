import turtle
t=turtle.Turtle()
t.speed(3)
t.fillcolor('red')
t.begin_fill()
for i in range(12):
    t.left(50)
    t.circle(50)
t.pendown()
for _ in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()    
