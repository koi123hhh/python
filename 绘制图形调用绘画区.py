
#绘制图形
import turtle
turtle.setup(1300,400,-250,250)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.color("yellow")
turtle.seth(-40)
for i in range(1):
 turtle.circle(40,80)

turtle.circle(-40,80)

turtle.circle(40,80/2)

turtle.fd(40)

turtle.circle(16,180)

turtle.fd(40 * 2/3)

turtle.done()