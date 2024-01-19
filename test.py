from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
turtle.penup()

turtle.write("Home = ", False, align="center")
turtle.write((0, 0), False)
screen.exitonclick()
