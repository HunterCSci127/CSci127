#CSci 127 Teaching Staff
#October 2017
#A program that uses functions to print out months.
#Modified by:  ADD YOUR NAME HERE

def monthString(monthNum):
     """
     Takes as input a number, monthNum, and
     returns the corresponding month name as a string.
     Example: monthString(1) returns "January".
     Assumes that input is an integer ranging from 1 to 12
     """
     
     monthString = ""

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### this is the only section    ###
     ### you change in this program. ###
     ###################################

     return(monthString)



def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
