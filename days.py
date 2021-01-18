#CSci 127 Teaching Staff
#A program that uses functions to print out days.
#Modified by:  --YOUR NAME HERE-- , --YOUR EMAIL HERE--

def dayString(dayNum):
     """
     Takes as input a number, dayNum, and
     returns the corresponding day name as a string.
     Example: dayString(1) returns "Monday".
     Assumes that input is an integer ranging from 1 to 7
     """

     dayString = ""

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### this is the only section    ###
     ### you change in this program. ###
     ###################################

     return(dayString)



def main():
     n = int(input('Enter the number of the day: '))
     dString = dayString(n)
     print('The day is', dString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
