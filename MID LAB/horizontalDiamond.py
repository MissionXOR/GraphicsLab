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
for i in range(2):
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(60)
t.end_fill()

# Keep window open until user clicks to close
turtle.done()
