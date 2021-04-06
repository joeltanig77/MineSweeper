from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

class Bomb:
    def lose(self):
        pass

    def flag(self):
        pass

class Move:
    def __init__(self):
        self.revealedFlag = False
        self.numberOfBombsAroundIt = 0

    def clearSpace(self):
        self.revealedFlag = True
        pass

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
        self.grid = [[0] * (self.rows) for i in range(self.cols)]
    def newGame(self):
        # Creates a new board
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
        s = [[str(e) for e in row] for row in self.grid]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))

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

    def getMoveCount(self):
        return self.moveCount

    def getGameState(self):
        return self.gameState

    def getSquare(self,i,j):
        pass

