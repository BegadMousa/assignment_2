'''
This File is Part of the Python Turtle assignment 2 for the course: GCIS 123 section 600
this file is drawings.py which is the second requirment for the assignment
To use this file you must have the turtle module installed
to use this file you must input the file name you want to draw and the file must be in the same directory as this file
the file must be a text file and must be 20x20 or 25x25(drawing02)
the code will draw the art based on the file totaly automaticly without havig to input the colors manually as strings
'''

import turtle

# constants
PIXEL_SIZE = 30
ROW=20
COLUMNS=20
Start_CORD_x = -300
Start_CORD_y = 250

# Colors dictionary
colors = {'0':"black",'1':"white",'2':"red", '3':"yellow", '4':"orange", '5':"green", '6':"yellowgreen", '7':"sienna", '8':"tan", '9':"gray", 'A':"darkgray"}

# Config
def init():
    turtle.speed(0)
    turtle.up()
    turtle.goto(Start_CORD_x,Start_CORD_y)
    turtle.pencolor("black")
    turtle.pensize(1)

# Draw Pixel
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

# draws a row of pixels based on the input string
def Draw_row(row,col,num_pixels,color_string):
    # MOVe to start of row
    xcor = Start_CORD_x
    ycor = Start_CORD_y

    # move to wanted row/col
    xcor += PIXEL_SIZE*col
    ycor -= PIXEL_SIZE*row

    turtle.goto(xcor,ycor)
    
    i=0
    # draw row of pixels
    while i < (num_pixels):
        # print(colors[color_string[i]])
        Draw_pixel(colors[color_string[i]])
        i += 1

# Draws the art based on the input file and the Draw_row function
def Draw_art():
    i=0
    num_pixels = 20

    # input file
    filename = input("please enter to file name to draw: ")

    # if no file set defualt to "drawing01.txt"
    if filename == "":
        filename = "drawing01.txt"

    # draw art from file
    with open(filename) as f:
        for line in f:
            # screen size is 25x25
            if len(line) >= 25:
                num_pixels = 25
                
            Draw_row(i,0,num_pixels,line)
            i += 1

def main():
    init()
    Draw_art()
    turtle.done()

if __name__ == "__main__":
    main()
