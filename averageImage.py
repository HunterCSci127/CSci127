#CSci 127 Teaching Staff
#October 2017
#A program that summarizes images, like koalastothemax
#Modified by:  ADD YOUR NAME HERE

import numpy as np
import matplotlib.pyplot as plt

def average(region):
     """
     Takes a region of an image and
     Returns the average red, green, and blue values across the region.
     """

     red, green, blue = 0,0,0  #<-- placeholder, can remove once defined.

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### this is the only section    ###
     ### you change in this program. ###
     ###################################


     return(red,green,blue)

def setRegion(region, r,g,b):
     """
     Takes a region of an image and red, green, and blue values, r, g, b.
     Sets the region so that all points have
     red values of r, green values of g, and blue values of b.
     """

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### this is the only section    ###
     ### you change in this program. ###
     ###################################





######################################################################
### DO NOT CHANGE ANYTHING BELOW AND INCLUDING THIS LINE           ###
######################################################################


def quarter(img2, levels):
     """
     Takes an image and the number of splits to make.
     Splits the image into regions (2**levels x 2**levels pieces)
     and averages each of these regions separately.
     Calls average() and setRegion() to average and set colors for the
     regions.
     """
     h = img2.shape[0]
     w = img2.shape[1]
     hReg = h//2**levels
     wReg = w//2**levels
     for i in range(2**levels):
          for j in range(2**levels):
               #Average the region:
               r,g,b = average(img2[i*hReg:(i+1)*hReg,j*wReg:(j+1)*wReg])
               setRegion(img2[i*hReg:(i+1)*hReg,j*wReg:(j+1)*wReg],r,g,b)


def main():
     inFile = input('Enter image file name: ')
     img = plt.imread(inFile)

     #Divides the image in 1/2, 1/4, 1/8, ... 1/2^8, and displays each:
     for i in range(8):
          img2 = img.copy()   #Make a copy to average
          quarter(img2,i)     #Split in half i times, and average regions

          plt.imshow(img2)    #Load our new image into pyplot
          plt.show()          #Show the image (waits until closed to continue)

     #Shows the original image:
     plt.imshow(img)	      #Load image into pyplot
     plt.show()               #Show the image (waits until closed to continue)


#Allow script to be run directly:
if __name__ == "__main__":
     main()
