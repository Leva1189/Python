# Function
# def print_numbers(limit):
#     for i in range(limit):
#         print(i)

# print_numbers(5)   

# малює трикутник за допомогою бібліотеки turtle
import turtle
import random

def draw_triangle(color: str, width: int):
  turtle.color(color)
  turtle.width(width)
  turtle.speed(3)
  for _ in range(3):
      turtle.forward(100)
      turtle.left(120)
list_colors = ['red', 'blue', 'green', 'yellow', 'purple']

for i in range(5):
  draw_triangle(list_colors[i], random.randint(1, 10))
  turtle.penup()
  turtle.forward(20)
  turtle.pendown()

turtle.exitonclick()