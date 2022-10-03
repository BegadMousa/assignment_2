'''
This File is the test file for Checkers.py
This File is Part of the Python Turtle assignment 2 for the course: GCIS 123 section 600
this file is checkers_test.py which is the first requirment for the assignment
'''

import turtle

# constants
PIXEL_SIZE = 30
ROW_AND_COL = 20 # number of rows and columns, this is to be used in the Draw_checkers function becouse its is a 20x20 checker board
ROW= 20
COLUMNS= 20
Start_CORD_x = -300
Start_CORD_y = 250

# Config
def init():
    turtle.speed(0)
    turtle.up()
    turtle.goto(-200,200) 
    turtle.pencolor("black")
    turtle.pensize(1)

def test_heading_init():
    assert turtle.heading() == 0

def test_pencolor():
    assert turtle.pencolor() == "black"

def test_start_cord_x():
    assert Start_CORD_x == -300

def test_start_cord_y():
    assert Start_CORD_y == 250

def Draw_pixel(color):
    i=0

    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.down()

    # draw Pixel
    while i<4:
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
        i += 1

    turtle.up()
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)

    

def test_draw_pixel():
    assert turtle.isdown() == True
    assert turtle.heading() == 0

def Draw_alt_row(row,col,num_pixels,color="red",alt_color="black"):
    # MOVe to start of row
    xcor = Start_CORD_x
    ycor = Start_CORD_y

    # move to wanted row/col
    xcor += PIXEL_SIZE*col
    ycor -= PIXEL_SIZE*row

    turtle.goto(xcor,ycor)
    turtle.fillcolor(color)
    
    i=0
    # draw row of pixels
    for i in range(num_pixels):
        if i%2==0: # alternate colors based iteration
            Draw_pixel(color)
        else:
            Draw_pixel(alt_color)

def Draw_checkers(num_pixels,color="red",alt_color="black"):  
    i=0
    j=0
 
    while j < num_pixels:
        if j%2==0:
            Draw_alt_row(j,0,num_pixels,color,alt_color)
        else:
            Draw_alt_row(j,0,num_pixels,alt_color,color)
        j += 1

def main():
    turtle.speed(0)
    init()
    Draw_checkers(ROW_AND_COL) # num_pixels, color, alt_color 
    turtle.done()


if __name__ == "__main__":
    main()