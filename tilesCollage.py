#CSci 127 Teaching Staff
#January 2021
#A program that creates a tile collage from input image
#Modified by:  ADD YOUR NAME HERE , ADD YOUR EMAIL HERE


import numpy as np
import matplotlib.pyplot as plt


def mirror(img, axis):
    '''
    Creates and returns a mirrored copy of img along axis
    Expected values for axis are 'x', 'y', 'xy' (mirrored along both x and y axes)
    If the value of axis is not one of the expected, it prints: Invalid axis
    '''

    ###################################
    ### FILL IN YOUR CODE HERE      ###
    ### Other than your name above, ###
    ### this is the only section    ###
    ### you change in this program. ###
    ###################################








def remove_hue(img, hue):
    '''
    Removes hue from img by turning off the corresponding color channel
    Expected values for hue are 'red', 'green', 'blue'
    If the value of hue is not one of the expected, it prints: No such hue.
    '''
    ###################################
    ### FILL IN YOUR CODE HERE      ###
    ### Other than your name above, ###
    ### this is the only section    ###
    ### you change in this program. ###
    ###################################






def fourfold_tile(img):
    '''
    Creates and returns a new image consisting of 4 copies of img
    in a tile layout, with 2 copies at the top and 2 copies at the bottom
    '''

    ###################################
    ### FILL IN YOUR CODE HERE      ###
    ### Other than your name above, ###
    ### this is the only section    ###
    ### you change in this program. ###
    ###################################






######################################################################
### DO NOT CHANGE ANYTHING BELOW  AND INCLUDING THIS LINE          ###
######################################################################


def main():
    '''
    Creates a tile collage from input image
    '''

    infile = input('Enter input file name: ')
    outFile = input('Enter output file name: ')
    img = plt.imread(infile)

    #new_img consits of four copies of img, two on top and two ont the bottom
    new_img = fourfold_tile(img)

    #Remove blue from top-right quarter
    remove_hue(new_img[:img.shape[0],img.shape[1]:],'blue')
    #Remove green from bottom-left quarter
    remove_hue(new_img[img.shape[0]:,:img.shape[1]],'green')
    #Remove blue from bottom-right quarter
    remove_hue(new_img[img.shape[0]:,img.shape[1]:],'red')


    #Mirror top-right quarter along the y-axis
    new_img[:img.shape[0],img.shape[1]:] = mirror(new_img[:img.shape[0],img.shape[1]:],"y")
    #Mirror bottom-left quarter along the x-axis
    new_img[img.shape[0]:,:img.shape[1]] = mirror(new_img[img.shape[0]:,:img.shape[1]],"x")
    #Mirror bottom-right quarter along both x and y axis
    new_img[img.shape[0]:,img.shape[1]:] = mirror(new_img[img.shape[0]:,img.shape[1]:],"xy")


    #Save the tile collage to a file
    plt.imsave(outFile, new_img)


#Allow script to be run directly:
if __name__ == '__main__':
    main()
