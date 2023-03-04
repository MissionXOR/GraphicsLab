import turtle

# Prompt user for input
size = int(input("Enter the size of the diamond: "))
fill_color = input("Enter the fill color of the diamond: ")
line_color = input("Enter the line color of the diamond: ")

# Set up turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw diamond
t.fillcolor(fill_color)
t.pencolor(line_color)
t.begin_fill()
t.right(45)
t.forward(size)
t.right(135)
t.forward(size)
t.right(45)
t.forward(size)
t.right(135)
t.forward(size)
t.end_fill()

# Keep window open until user clicks to close
turtle.done()
