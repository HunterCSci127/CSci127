#CSci 127 Teaching Staff
#FALL 2021
#A template for a program that returns olympic world records
#Modified by:  ADD YOUR NAME HERE

def worldRecord(gender, event):
     """
     Write a function worldRecord(), that takes two parameters: gender (string) and the event type (int). 
     The function should return a float for the Olympic world record for the event. 

     Gender can be: Men's Standard = "men", Women's Standard = "women"

     If Men's Standard and event type is 100 meters, the record is 9.63 seconds.
     If Men's Standard and event type is 200 meters, the record is 19.30 seconds.
     If Men's Standard and event type is 400 meters, the record is 43.03 seconds.
     If Women's Standard and event type is 100 meters, the record is 10.62 seconds.
     If Women's Standard and event type is 200 meters, the record is 21.34 seconds.
     If Women's Standard and event type is 400 meters, the record is 48.25 seconds.
     else return -1 since wordlRecord() function can't handle event type greater than 400 meters
     """
     
     time = 0.0
     
     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### this is the only section    ###
     ### you change in this program. ###
     ###################################

     return(time)

def main():
     z = input('Enter the gender: ').lower()
     t = int(input('Enter the event distance: '))
     record = worldRecord(z,t)
     print("The record for "+z+" 's "+ str(t) + " meters is", record)

#Allow script to be run directly:
if __name__ == "__main__":
     main()