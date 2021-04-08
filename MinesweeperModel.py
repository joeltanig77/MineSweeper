from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

class Bomb:
    def __init__(self):
        self.revealedFlag = False
        self.loseFlag = False

    def __repr__(self):
        return str("?")

    def flag(self):
        pass

    def revealed(self):
        return self.revealedFlag

    def clearSpace(self):
        self.revealedFlag = True
        self.loseFlag = True

    def getLoseFlag(self):
        return self.loseFlag

class Move:
    def __init__(self):
        self.revealedFlag = False
        self.numberOfBombsAroundIt = 0

    def __repr__(self):
        return str(self.getBombsAroundMe())

    def clearSpace(self):
        self.revealedFlag = True


    def incrementNumberOfBombsAroundIt(self):
        self.numberOfBombsAroundIt += 1

    def flag(self):
        pass

    def getBombsAroundMe(self):
        return self.numberOfBombsAroundIt

    def revealed(self):
        return self.revealedFlag

class MinesweeperModel:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.moveCount = 0
        # -1 = in progress, 0 = lose, 1 = win
        self.gameState = -1
        self.move = Move()
        self.bomb = Bomb()
        self.grid = []
    def newGame(self):
        # Creates a new board
        self.grid = [[0] * (self.rows) for i in range(self.cols)]
        self.moveCount = 0
        self.gameState = -1
        count = self.rows*self.cols
        bombCount = 10
        listOfBoardPieces = []
        while count != 0:
            if count % 2 == 0 and bombCount != 0:
                listOfBoardPieces.append(Bomb())
                print(bombCount)
                bombCount -= 1
                count -= 1
            else:
                listOfBoardPieces.append(Move())
                count -= 1
        i = 0
        count = 100
        while count != 0:
            randomIntRows = random.randint(0,self.rows-1)
            randomIntCols = random.randint(0,self.cols-1)
            if self.grid[randomIntRows][randomIntCols] == 0:
                self.grid[randomIntRows][randomIntCols] = listOfBoardPieces[i]
                i+=1
                count -= 1

        print(self.grid)
        #grid[self.rows-1][self.cols-1] = Bomb()
        # Need to now figure out the bombs next to each move class
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if isinstance(self.grid[i][j],Bomb):
                    # Top left corner
                    if i == 0 and j == 0:
                        print("Top left corner bomb")
                        print(self.grid[0][0])
                        if isinstance(self.grid[i][j+1],Move):
                            grab = self.grid[i][j+1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())
                        if isinstance(self.grid[i + 1][j - 1], Move):
                            grab = self.grid[i+1][j-1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())
                        if isinstance(self.grid[i-1][j],Move):
                            grab = self.grid[i-1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())
                    # Bottom left corner
                    elif i == self.rows-1 and j == 0:
                        print("Bottom left corner bomb")
                        print(self.grid[self.rows-1][0])
                        if isinstance(self.grid[i-1][j],Move):
                            grab = self.grid[i-1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i-1][j+1], Move):
                            grab = self.grid[i-1][j+1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i][j+1], Move):
                            grab = self.grid[i][j+1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                    # Top right corner
                    elif i == 0 and j == self.cols-1:
                        print("Top right corner bomb")
                        print(self.grid[0][self.cols - 1])
                        if isinstance(self.grid[i][j-1],Move):
                            grab = self.grid[i][j-1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i+1][j-1],Move):
                            grab = self.grid[i+1][j-1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i+1][j],Move):
                            grab = self.grid[i+1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                    # Bottom right corner
                    elif i == self.rows-1 and j == self.cols-1:
                        print("Bottom right corner bomb")
                        print(self.grid[self.rows - 1][self.cols - 1])
                        if isinstance(self.grid[i][j - 1], Move):
                            grab = self.grid[i][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i - 1][j - 1], Move):
                            grab = self.grid[i - 1][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i - 1][j], Move):
                            grab = self.grid[i - 1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                    # Top side rectangle
                    elif i == 0:
                        print("Top side rectangle")
                        print(self.grid[i][j])
                        if isinstance(self.grid[i][j - 1], Move):
                            grab = self.grid[i][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i + 1][j - 1], Move):
                            grab = self.grid[i + 1][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i + 1][j], Move):
                            grab = self.grid[i + 1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i + 1][j + 1], Move):
                            grab = self.grid[i + 1][j + 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i][j + 1], Move):
                            grab = self.grid[i][j + 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                    # Left side rectangle
                    elif j == 0:
                        print("Left side rectangle")
                        print(self.grid[i][j])
                        if isinstance(self.grid[i - 1][j], Move):
                            grab = self.grid[i - 1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i - 1][j + 1], Move):
                            grab = self.grid[i - 1][j + 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i][j + 1], Move):
                            grab = self.grid[i][j + 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i + 1][j + 1], Move):
                            grab = self.grid[i + 1][j + 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i + 1][j], Move):
                            grab = self.grid[i + 1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                    # Bottom side of rectangle
                    elif i == self.rows-1:
                        print("Bottom side rectangle")
                        print(self.grid[i][j])
                        if isinstance(self.grid[i][j - 1], Move):
                            grab = self.grid[i][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i - 1][j - 1], Move):
                            grab = self.grid[i - 1][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i - 1][j], Move):
                            grab = self.grid[i - 1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i - 1][j + 1], Move):
                            grab = self.grid[i - 1][j + 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i][j + 1], Move):
                            grab = self.grid[i][j + 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                    # Right side rectangle
                    elif j == self.cols-1:
                        print("Right side rectangle")
                        print(self.grid[i][j])
                        if isinstance(self.grid[i + 1][j], Move):
                            grab = self.grid[i + 1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i - 1][j - 1], Move):
                            grab = self.grid[i - 1][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i][j - 1], Move):
                            grab = self.grid[i][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i + 1][j - 1], Move):
                            grab = self.grid[i + 1][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i - 1][j], Move):
                            grab = self.grid[i - 1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                    # Reg case
                    else:
                        print("Regular case")
                        print(self.grid[i][j])
                        if isinstance(self.grid[i - 1][j], Move):
                            grab = self.grid[i - 1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i - 1][j - 1], Move):
                            grab = self.grid[i - 1][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i][j - 1], Move):
                            grab = self.grid[i][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i + 1][j - 1], Move):
                            grab = self.grid[i + 1][j - 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i + 1][j], Move):
                            grab = self.grid[i + 1][j]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i + 1][j + 1], Move):
                            grab = self.grid[i + 1][j + 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i][j + 1], Move):
                            grab = self.grid[i][j + 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())

                        if isinstance(self.grid[i - 1][j + 1], Move):
                            grab = self.grid[i - 1][j + 1]
                            grab.incrementNumberOfBombsAroundIt()
                            print(grab.getBombsAroundMe())
        print(self.grid)
        for i in self.grid:
            print(i)

    def getMoveCount(self):
        return self.moveCount

    def getGameState(self):
        return self.gameState

    #TODO: Need to have users pick moves next
    def getSquare(self,i,j):
        self.reveal(i,j)
        return self.grid[i][j]

    def reveal(self,i,j):
        grab = self.grid[i][j]
        if grab.revealed() == False:
            grab.clearSpace()
            self.moveCount += 1

        if isinstance(self.grid[i][j],Bomb):
            self.gameState = 0

    def revealAllBombs(self,board,buttons):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if isinstance(self.grid[i][j], Bomb):
                    grab = self.grid[i][j]
                    grab.clearSpace()
                    buttons[i][j] = QLabel("       " + str("b"))
                    board.addWidget(buttons[i][j], i, j)

    def getPuzzle(self):
        return self.grid