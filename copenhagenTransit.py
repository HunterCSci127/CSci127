#CSci 127 Teaching Staff
#October 2017
#A template for a program that computes Copenhagen transit fares.
#Modified by:  ADD YOUR NAME HERE

def computeFare(zone, ticketType):
     """
     Takes as two parameters: the zone and the ticket type.
     Returns the Copenhagen Transit fare, as follows:

     If the zone is 2 or smaller and the ticket type is "adult", the fare is 23.
     If the zone is 2 or smaller and the ticket type is "child", the fare is 11.5.
     If the zone is 3 and the ticket type is "adult", the fare is 34.5.
     If the zone is 3 or 4 and the ticket type is "child", the fare is 23.
     If the zone is 4 and the ticket type is "adult", the fare is 46.
     If the zone is greater than 4, return a negative number (since your calculator does not handle inputs that high).
     """
     
     fare = 0
     
     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### this is the only section    ###
     ### you change in this program. ###
     ###################################

     return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (adult/child): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
