import turtle
from turtle import *
from turtle import Screen
from freegames import vector
    
def emptySquare():
    pass  # TODO
    
def filledSquare():
  pass  # TODO
  
while True:
    screen = Screen()
    answer = screen.textinput("Next Game","1 - Square:")
    if (answer is None):
        break
    elif (answer == '1'):
        emptySquare()
    elif (answer == '2'):
        filledSquare()
 
def emptySquare():
    t = turtle.Turtle()

    for i in range(4):
        t.forward(50)
        t.right(90)     # Rotate clockwise by 90 degrees

def emptyCircle():
    t = turtle.Turtle()
    t.circle(100)
