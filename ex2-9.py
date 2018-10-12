import turtle as t
week = ['black','grey','darkgreen','gold','violet','purple','green','red']
t.setup(1000,400,200,200)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.seth(-40)
ls=["grey","green","pink","yellow"]
for i in range(2):
    for i in ls:
       t.pencolor(i)
       t.circle(30,80)
       t.circle(-30,80)
t.pencolor("gold")
t.circle(30,80/2)
t.pencolor("violet")
t.fd(40)
t.pencolor("purple")
t.circle(16,180)
t.pencolor("red")
t.fd(40*2/3)
