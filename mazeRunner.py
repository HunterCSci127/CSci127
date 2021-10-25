# Name: Yash Mahtani
# Email: Yash.Mahtani82@myhunter.cuny.edu

## This function determines whether or not a given move is legal
def isPositionAvailable(row, col, maze): ## row and col of the place the User wishies to move to
    if row < 0 or col < 0: ## Checks if User is attempting to go out of bounds
        return False
    if maze[row][col] == '1': ## Checks if User is attempting to go thru walls
        return False
    elif maze[row][col] == '0': ## Checks if User is attempting to make legal move
        return True
    else:
        return True

## Given a string representing a maze, this function will place it in a 2d array
def generateMaze(textMaze):
    textMaze = textMaze.split('\n')

    maze = []

    for row in textMaze:
        rowOfMaze = row.split(' ')
        maze.append(rowOfMaze)

    return maze

## Prints out a visual representation of the maze, and where the current user is located
def printMaze(maze, currRow, currCol): ## currRow and currCol represent the Users current location
    rowCount = -1

    for row in maze:
        rowCount += 1
        for stuff in range(3):
            colCount = -1
            for column in row:
                colCount += 1

                ## Location of User
                if rowCount == currRow and colCount == currCol:
                    for i in range(3):
                        print('v', end = '')
                ## Location of wall
                elif column == '1':
                    for i in range(3):
                        print('*', end = '')
                ## Location of hall
                elif column == '0':
                    for i in range(3):
                        print(' ', end = '')
                ## Location of start
                elif column == 'S':
                    for i in range(3):
                        print('S', end = '')
                ## Location of end
                elif column == 'X':
                    for i in range(3):
                        print('X', end = '')
            print()


## This function asks for a string of commands and executes them
def playGame(maze, row, col): ## row and col given here is the starting position
    commands = input("Enter a string of commands: ")
    
    ## Loops through the given set of commands
    invalidMoveFound = False
    
    for command in commands:
        # If valid move, continue looping through string doing stuff, if not, 
        # put a hault on doing things the rest of the run
        if not invalidMoveFound:
            
            #### ENTER YOUR CODE HERE ####

                    # WITHIN HERE #

            ##############################

    ## If after all the commands have been executed, the game has not finished
    ## return false indicating that they did not reach the end, and return the row
    ## and col position so that the outputed maze can be updated.
    return False, row, col

def main():
    print("Hello Everyone! Welcome to Maze Runner!\n\
To succeed in this Computer Science class, you must go through some trials and tribulations...\n\
So tonight, you must pass through our maze!\n\
The game is not over until you have found your path...\n\
And if you try and fail, you must restart from the beginning and try again!\n\
Good luck!")

    ## Reads in a text file containing a maze
    textMazeFile = input("Enter name of text file containing a maze: ")
    textMaze = open(textMazeFile, "r")
    maze = generateMaze(textMaze.read())

    ## The game continues until the User is victorious
    result, row, col = False, 1, 0
    while not result:
        print("\nHere is a picture of the maze, provided by some random person down the street ->")
        printMaze(maze, row, col)
        result, row, col = playGame(maze, row, col)

    print("Congrats on escaping the maze! Please do join us again :)")

if __name__ == '__main__':
    main()
