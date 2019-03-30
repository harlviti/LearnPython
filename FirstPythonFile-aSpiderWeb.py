# -*- coding: utf-8 -*-
import turtle
import random
screen = turtle.Screen()
screen.bgcolor("white")
turtle.speed(10)

turtle.fd(400)
turtle.back(400)
turtle.fd(-400)
turtle.back(-400)
turtle.left(90)
turtle.fd(400)
turtle.back(400)
turtle.fd(-400)
turtle.back(-400)

turtle.left(45)
turtle.fd(350)
turtle.back(350)
turtle.fd(-350)
turtle.back(-350)
turtle.right(90)
turtle.fd(350)
turtle.back(350)
turtle.fd(-350)
turtle.back(-350)

sides = 8
for i in range(120):
   # TODO: write code...
   turtle.forward(i * 3 / sides + i)
   turtle.left(240 / sides + 1)
   turtle.width(i * sides / 200)

turtle.exitonclick()
