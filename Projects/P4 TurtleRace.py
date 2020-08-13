from turtle import *
from random import randint
import string

for step in range(16):
    speed(0.1)
    write(step,align="left")
    right(90)
    forward(10)
    pendown()    
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
try:
   ada= Turtle("turtle")
   ada.color("red")
   ada.right(360)
   ada.penup()
   ada.goto(-30,-15)
   ada.pendown()

   ama= Turtle("turtle")
   ama.color("blue")
   ada.right(360)
   ama.penup()
   ama.goto(-30,-55)
   ama.pendown()

   aca= Turtle("turtle")
   aca.color("green")
   aca.right(360)
   aca.penup()
   aca.goto(-30,-95)
   aca.pendown()

   ava= Turtle("turtle")
   ava.color("yellow")
   ava.right(360)
   ava.penup()
   ava.goto(-30,-135)
   ava.pendown()

   for step in range(130):
      ama.forward(randint(1,5))
      ada.forward(randint(1,5))
      aca.forward(randint(1,5))
      ava.forward(randint(1,5))
         

      