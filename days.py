#CSci 127 Teaching Staff
#A program that uses functions to print out days.
#Modified by:  Nicole Chiguil

def dayString(dayNum):
     """
     Takes as input a number, dayNum, and
     returns the corresponding day name as a string.
     Example: dayString(1) returns "Monday".
     Assumes that input is an integer ranging from 1 to 7
     """
     
     dayString = ""

    def dayString(no):
    if no==1:
        print("Monday")
    elif no==2:
        print("Tuesday")
    elif no==3:
        print("Wednesday")
    elif no==4:
        print("Thrusday")
    elif no==5:
        print("Friday")
    elif no==6:
        print("Saturday")
    elif no==7:
        print("Sunday")

no=int(input("Enter day number:"))

dayString(no)


     return(dayString)



def main():
     n = int(input('Enter the number of the day: '))
     dString = dayString(n)
     print('The day is', dString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
