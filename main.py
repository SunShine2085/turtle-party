# Turtle Party Project
#by Chris Courville 
6/20/23

# print("Hello, World!")

import turtle
turtle.color("purple")

def back(len):
   turtle.penup()
   turtle.backward(len)
   turtle.pendown()
   
def move(len):
  back(-1 * len)

def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)
    
def square(size):
  for i in range(4):
    turtle.forward(size)
    turtle.left(24)
    
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360/num)
    
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
    
spiral(75,45)
move(150)
turtle.color("blue")
spiral(100,90)

#for n in range(3, 10):
#  move(50)
#  polygon(n, 100/n)
#  back(50)
#  turtle.right(360/7)
