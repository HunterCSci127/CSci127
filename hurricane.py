#YOUR NAME HERE
#YOUR EMAIL HERE
#Inspired by 2018 Nifty Program by Phil Ventura:
#   This program uses his turtle setup but processing
#       of data is with Pandas.


import turtle
import pandas as pd

def setup(windowTitle):
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    screen = turtle.Screen()
    screen.title(windowTitle)

    # this assures that the size of the screen will match the map image:
    screen.setup(800, 404)
    #Set coordinates for latitude and longitude:
    screen.setworldcoordinates(-180,-90,180,90)

    # ... which is the same size as our image
    # now set the background to our space image
    screen.bgpic("mapNASA.gif")

    t = turtle.Turtle()
    t.pensize(1)
    t.color('red')
    t.penup()

    return t,screen

def animate(t,lat,lon,wind):
    """
    Takes as input: a turtle, the location (as latitude and longitude) and
    the wind speed.  The turtle moves to the location, changes color & pensize
    (see below).

    * Red for Category 5 (windspeed > 157 mph)
    * Orange for Category 4  (windspeed in 130-156 mph)
    * Yellow for Category 3   (windspeed in 111-129 mph)
    * Green for Category 2   (windspeed in 96-110 mph)
    * Blue for Category 1   (windspeed in 74-95 mph)
    * White if not hurricane strength

    The thickness of the line should change in proportion to the hurricane category
    (i.e. pensize(5) for Category 5, pensize(4) for Category 4, etc.).

    """

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other thanname/email above, ###
     ### this is the only section    ###
     ### you change in this program. ###
     ###################################
    
    return(t)

def main():
    """Animates the path of hurricane from file:
    """
    hFile = input('Enter file name: ')
    t, wn = setup(hFile)

    df = pd.read_csv(hFile)
    for index,row in df.iterrows():
        lat = int(row["Lat"])
        lon = int(row["Lon"])
        wind = row["Wind"]
        print(lat,lon,wind)
        animate(t,lat,lon,wind)

if __name__ == "__main__":
    main()
