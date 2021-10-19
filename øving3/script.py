import turtle
import math

lengde = 60
space = 30

diamanter = int(input("Hvor mange diamanter ønsker du? "))

turtle.right(45)
for d in range(diamanter):
  turtle.pendown()

  for i in range(4):
    turtle.left(90)
    turtle.forward(lengde)
  
  if d != diamanter-1:
    turtle.penup()
    turtle.right(45)
    dst = math.sqrt(2*space**2)
    turtle.forward(dst)
    turtle.left(45)
    lengde += space*2



input("lol")

   
