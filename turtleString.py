#Modified by: Lilah Au Yeung
#Email: lilah.auyeung11@myhunter.cuny.edu
#A program that uses command strings to control turtle drawing


import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     #The graphics window
commands = input("Please enter a command string: ")

for ch in commands:
    #perform action indicated by the character
    if ch == 'F':            #move forward
        tess.forward(50)
    elif ch == 'L':          #turn left
        tess.left(90)
    elif ch == 'R':          #turn right
        tess.right(90)
    elif ch == '^':          #lift pen
        tess.penup()
    elif ch == 'v':          #lower pen
        tess.pendown()
    elif ch == 'r':          #turn red
        tess.color("red")
    elif ch == 'g':          #turn green
        tess.color("green")
    elif ch == 'b':          #turn blue
        tess.color("blue")
    elif ch == 'S':          #stamps
        tess.stamp()
    elif ch == 'D':          #dots
        tess.dot()
    elif ch == 'B':          #moves backwards 50
        tess.backward(50)
    elif ch == 'p':          #turn purple
        tess.color("purple")
    else:                    #for any other character, print an error message
        print("Error: do not know the command:", ch)

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked
