# NAME: 
# EMAIL: 
# Starter code Program #40: Checkers

""" FILL IN MISSING LINES OF CODE BELOW: import necessary libraries """


# drawBoard(size) uses numpy and matplotlib to create a checkerboard and save it as an image
def drawBoard(size):
   """ FILL IN MISSING LINE OF CODE BELOW: Create numpy size x size array of ones with 3 color channels called board"""
   
   
   # Fill in tiles of even indexed rows
   for i in range(0, size, size//4):
      for j in range(0, size, size//4):
         board[i:i+size//8, j:j + size//8, :] = 0
         
   # Fill in tiles of odd indexed rows      
   for i in range(size//8, size, size//4):
      for j in range(size//8, size, size//4):
         board[i:i+size//8, j:j + size//8, :] = 0
         
   """ FILL IN MISSING LINE OF CODE BELOW: Save board as 'board.png' """
   
   
   
# setupScreen(size) creates a turtle screen of size + 100 x size + 100 with the background picture as the checkerboard created   
def setupScreen(size):
   """ 
   FILL IN MISSING LINES OF CODE BELOW: 
      Create a turtle screen
      Setup turtle screen with width of size + 100 and height of size + 100
      Set background pic of turtle screen to 'board.png'
   """
   # placeholder line: Remove me!
   placeholder = ""


# createPiece(color) creates a circle turtle with the specified color that will act as our checker piece
def createPiece(pieceColor):
   """
   FILL IN MISSING LINES OF CODE BELOW:
      create turtle object
      set turtle color to pieceColor
      set shape to circle
      pick the pen up
      return created turtle object
   """
   # placeholder line: Remove me!
   placeholder = ""



# movePiece(piece, x, y) moves the piece to the respective tile on the board
def movePiece(size, piece, row, col):
   # calculating x coordinate and y coordinate based on board size, row, and col provided
   coordX = size//-2 + size//16 + ((col - 1) * size//8)
   coordY = size//2 - size//16 - ((row - 1) * size//8)
   
   """ FILL IN MISSING LINE OF CODE BELOW: move the piece (a turtle object) to (coordX, coordY) using the goto() function"""
   
     
def main():
   """ 
   FILL IN MISSING LINES OF CODE BELOW: 
      ask user for size of checkboard and save to a variable
      call drawBoard
      call setupScreen
      create a piece with the color red by calling createPiece and save to a variable
      ask user for row to move piece to
      ask user for col to move piece to
      call movePiece with parameters size, piece, row, col
   """

   
   
if __name__ == "__main__":
   main()