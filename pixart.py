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
