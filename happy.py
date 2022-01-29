from turtle import *


timmy = Turtle()
timmy.shape('turtle')
timmy.color()

colors = ['null', 'null', 'red','blue','yellow', 'green', 'black', 'dodger blue', 'orange', 'pink', 'purple', 'gold']


for i in range(3, 11):
    for n in range(i):
        timmy.color(colors[i])
        timmy.forward(15)
        timmy.rt(float(360 / i))
        timmy.forward(15)



screen = Screen()
screen.exitonclick()
