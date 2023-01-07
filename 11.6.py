
import turtle
t=turtle.Turtle()
turtle.bgcolor('black')
t.shape('turtle')
List1=["red","red","orange","red","gold"]
for i in range(200):
    t.color(List1[i%5])
    t.pensize(i/10+2)
    t.forward(i)
    t.left(59)
