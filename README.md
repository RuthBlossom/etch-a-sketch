# Turtle Drawing Program

This Python program utilizes the Turtle module to create a simple drawing application where users can control a turtle named 'byron' to draw on a screen.

![Uploading turtle graphics.JPG…]()


## Features

- **Interactive Drawing**: Users can control the turtle to move forwards, backwards, turn left, and turn right using keyboard inputs.
- **Clear Drawing**: Users can clear the drawing canvas by pressing the "c" key.
- **Customizable Turtle**: You can customize the turtle's appearance, pen size, and drawing speed.
- **Keyboard Events**: The program listens for keyboard events and responds to specific key presses to execute corresponding actions.

## How It Works

The program uses the Turtle module to create a turtle object (`byron`) and a drawing screen. Here's how it works:

1. **Turtle Initialization**: The program creates a Turtle object named 'byron' and a drawing screen using the `Turtle()` and `Screen()` functions, respectively.
2. **Movement Functions**: It defines functions to move the turtle forwards, backwards, turn left, and turn right by a fixed amount.
3. **Clear Function**: A function is defined to clear the drawing canvas, lift the pen, return the turtle to its home position, and put the pen down.
4. **Keyboard Event Handling**: The program listens for keyboard events using the `listen()` method and binds specific functions to certain keys using the `onkey()` method.
5. **Main Loop**: The program enters the main loop where it waits for user input. When the user presses a key, the corresponding function is executed to move the turtle or clear the canvas.
6. **Exit Condition**: The program exits the Turtle graphics window when clicked by the user.

## Usage

1. Run the program using a Python interpreter.
2. Use the following keys to control the turtle:
   - "w": Move forwards
   - "s": Move backwards
   - "a": Turn left
   - "d": Turn right
   - "c": Clear the drawing
3. Click on the drawing window to close it when you're done.

## Customization

You can customize the program in the following ways:

- **Turtle Appearance**: Adjust the turtle's appearance, pen size, and drawing speed.
- **Key Bindings**: Change the keys associated with specific actions by modifying the `screen.onkey()` calls.
- **Additional Features**: Add more functions to implement additional drawing capabilities or interactive features.

## Prerequisites

Before running the program, ensure you have Python installed on your system. The Turtle module is included in the standard Python library, so no additional installation is required.

