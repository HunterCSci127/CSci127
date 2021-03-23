#CSci 127 Teaching Staff
#September 2020
#A template for a program that draws nested squares
#Modified by:  ADD YOUR NAME HERE
#Email: ADD YOUR EMAIL HERE

import turtle
def setUp(t, dist, col):
    """
    Takes three parameters, a turtle, t, the distance, dist,
    to move the turtle and a color, col, to set the turtle's color.
    """
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)


def nested_squares(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 4 times:  moves forward that length, turns 90 degrees,
    and calls nested_squares(t, length/2).
    """

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### these are the only sections ###
     ### you change in this program. ###
     ###################################


def fractal_squares(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 4 times:  moves forward that length, turns 90 degrees,
    and calls fractal_squares(t, length/2).
    """

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### these are the only sections ###
     ### you change in this program. ###
     ###################################


def main():
    n = int(input('Enter length: '))

    tom = turtle.Turtle()
    setUp(tom, -100, "darkgreen")
    nested_squares(tom, n)

    tess = turtle.Turtle()
    setUp(tess, 100, "steelblue")
    fractal_squares(tess, n)

if __name__ == "__main__":
     main()

          
