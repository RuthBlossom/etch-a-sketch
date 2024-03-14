from turtle import Turtle, Screen

# Create a turtle named 'byron' and a screen to draw on
byron = Turtle()
# Creates a drawing screen.
screen = Screen()


# Function to move the turtle forward by 10 units
def move_forwards():
	byron.forward(10)


# Function to move the turtle backward by 10 units
def move_backwards():
	byron.backward(10)


# Function to turn the turtle left by 10 degrees
def move_left():
	new_heading = byron.heading() + 10
	byron.setheading(new_heading)


# Function to turn the turtle right by 10 degrees
def move_right():
	new_heading = byron.heading() - 10
	byron.setheading(new_heading)


# Function to clear the drawing, lift the pen, move to the home position, and put the pen down
def clear():
	byron.clear()
	byron.penup()
	byron.home()
	byron.pendown()


# Listen for keyboard events
screen.listen()

# Bind the functions to specific keys
# Binds a function (func) to a specific key (key). When the key is pressed, the associated function is called.
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_right, "a")
screen.onkey(move_left, "d")
screen.onkey(clear, "c")

# Exit the turtle graphics window when clicked
screen.exitonclick()
