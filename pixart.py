from turtle import Screen, Turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

def initialization(turta):
    '''Function which sets the speed, pencolor and the starting point of the turtle to start drawing'''
    turta.speed(0)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2) # initial coordinate of the turtle to begin drawing
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)

def get_color(char):
    """Takes a character and returns the corresponding color string or None if the character is invalid."""
    
    # creating a dictionary to map color codes to color names
    color_map = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray'
    }
    return color_map.get(char, None)

def draw_color_pixel(color_string, turta):
    """Draws a pixel with the given color using the turtle object."""

    turta.fillcolor(color_string)
    turta.begin_fill()

    # repeat 4 times to draw a square
    for _ in range(4):
        turta.forward(PIXEL_SIZE)
        turta.right(90)
    
    turta.end_fill()
    turta.forward(PIXEL_SIZE)

def draw_pixel(char, turta):
    """Draws a pixel with the given color code using the turtle object."""
    color_string = get_color(char)

    if color_string:
        draw_color_pixel(color_string, turta) # calling the function to draw the pixel
    else:
        print(f"Invalid color code: {char}")

def draw_line_from_string(color_string, turta):
    """Draws a line of pixels based on the color string using the turtle object."""
    start_x = turta.xcor()

    turta.penup()
    turta.setx(start_x)
    turta.pendown()

    # drawing the pixels based on the color string
    for char in color_string:
        color = get_color(char)
        if color is None:
            print(f"Invalid color code encountered: {char}")
            return False
        draw_pixel(char, turta) # calling the function to draw the pixel

    turta.penup()
    turta.setx(start_x) # moving the turtle to the start of the next row
    turta.sety(turta.ycor() - PIXEL_SIZE) # moving the turtle to the next row
    turta.pendown()

    return True

def draw_shape_from_string(turta):
    """Prompts the user to enter color strings and draws corresponding pixels."""

    while True:
        # asking the user to enter the color string
        color_string = input("Enter a color string (or press Enter to quit): ")

        # if the user presses Enter (i.e., enters an empty str), the loop will break
        if not color_string:
            print("Ending...")
            break

        # calling the function to draw the line of pixels
        if not draw_line_from_string(color_string, turta):
            print("Invalid color string entered, stopping.")
            break

def draw_grid(turta):
    """Draws a 20x20 checkerboard grid using the turtle object."""

    # asking the user to enter the color codes for the two colors
    color1 = input("Enter the code of the first color: ")
    color2 = input("Enter the code of the second color: ")

    for row in range(20):
        # using divisibility by 2 to alternate colors for checkerboard pattern
        if row % 2 == 0:
            color_string = (color1 + color2) * 10
        else: 
            color_string = (color2 + color1) * 10

        draw_line_from_string(color_string, turta) # calling the function to draw the line of pixels

def draw_shape_from_file(turta):
    """Reads color strings from a file and draws the corresponding shape."""

    # asking the user to enter the path of the file
    file_path = input("Enter the path of the file to read: ")

    # reading the file and drawing the shape based on the color strings
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not draw_line_from_string(line, turta): # calling the function to draw the line of pixels
                    print("Invalid color string in file, stopping.")
                    break

    except FileNotFoundError:
        print(f"File {file_path} not found.")