import turtle

# create a turtle object
pen = turtle.Turtle()

# set turtle speed
pen.speed(2)

# first star
for i in range(5):
    pen.forward(100)
    pen.right(144)

# move turtle to start position for second star
pen.penup()
pen.goto(-150, 0)
pen.pendown()

# second star
for i in range(5):
    pen.forward(100)
    pen.left(144)

# hide turtle when finished
pen.hideturtle()

# keep turtle window open until closed manually
turtle.done()
