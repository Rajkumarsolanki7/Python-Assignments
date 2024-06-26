import turtle

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
pen = turtle.Turtle()

# Function to draw a circle (used for the face, eyes, and nose)
def draw_circle(color, radius):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Draw the face
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)  # Size of the face
pen.end_fill()
# Draw the eyes
pen.penup()
pen.goto(-40, 120)
draw_circle('black', 15)  # Fully black eyes
pen.goto(40, 120)
draw_circle('black', 15)  # Fully black eyes

# Draw the mouth
pen.penup()
pen.goto(-40, 85)
pen.pendown()
pen.right(80)
pen.circle(40, 160)  # Slightly smiling mouth

# Hide the turtle cursor
pen.hideturtle()

# Keep the window open until the user closes it
turtle.done()

