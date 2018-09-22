#e2.1Drawpython.py
import turtle
turtle.setup(400,250,250,200)
turtle.penup()
turtle.fd(-500)
turtle.pendown()
turtle.pensize(30)
turtle.pencolor("pink")
turtle.seth(-20)
for i in range(5):
    turtle.circle(60,90)
    turtle.circle(-60,90)
turtle.circle(100,70/2)
turtle.fd(80)
turtle.circle(-150,200)
turtle.fd(70*2/3)
