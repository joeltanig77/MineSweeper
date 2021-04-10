from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import Qt
from MinesweeperModel import *


# This is the view controller

class MinesweeperWindow(QMainWindow,QWidget):
    def __init__(self):
        super(MinesweeperWindow,self).__init__()
        sound = QSound("WindowsXPExclamation.wav")
        sound.play("WindowsXPExclamation.wav")
        self.mine = MinesweeperModel()
        self.winOrLoseLabel = QLabel("")
        # Add a widget at the center
        widget = QWidget()
        self.setCentralWidget(widget)

        # we'll stack the puzzle above the grid of buttons with this
        self.layout = QVBoxLayout()
        widget.setLayout(self.layout)
        self.timer = QTimer()
        self.buttons = [[0] * (10) for i in range(10)]

        self.mine.newGame()

        self.puzzle = self.mine.getPuzzle()

        #Add grid logic
        self.board = QGridLayout()
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                button = QPushButton("")
                button.clicked.connect(lambda _, row=i,col=j: self.buttonClicked(row,col))
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.buttons[i][j] = (button)
                self.buttons[i][j].setStyleSheet("background-color : #A9A9A9")
                self.board.addWidget(self.buttons[i][j],i,j)
        #QTimer.singleShot(0, lambda: self.print_coordinates(0, 0))
        self.layout.addLayout(self.board)



        # only two menu items, so may as well set them up here
        menu = self.menuBar().addMenu("&Game")
        newAct = QAction("&New", self, shortcut=QKeySequence.New, triggered=self.newGame)
        menu.addAction(newAct)
        menu.addSeparator()
        quitAct = QAction("E&xit", self, shortcut=QKeySequence.Quit, triggered=self.close)
        menu.addAction(quitAct)

        # Set the title here
        self.setWindowTitle("MineSweeper")

        self.winOrLoseLabel = QLabel("Press E to set a flag")
        flagFont = QFont("Times", 14, QFont.Bold)
        self.winOrLoseLabel.setFont(flagFont)
        self.winOrLoseLabel.setFrameStyle(QFrame.Sunken)
        self.winOrLoseLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.winOrLoseLabel)

        # This is the game logic
        # Start the game here

    def newGame(self):
        print("New game started!")
        # Play the sounds
        sound = QSound("WindowsXPExclamation.wav")
        sound.play("WindowsXPExclamation.wav")
        # Reset the buttons
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                button = QPushButton("")
                button.clicked.connect(lambda _, row=i, col=j: self.buttonClicked(row, col))
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.buttons[i][j] = (button)
                self.buttons[i][j].setStyleSheet("background-color : #A9A9A9")
                self.board.addWidget(self.buttons[i][j], i, j)

        # Call the new game from the model
        self.mine.newGame()
        self.mine.resetReveal()
        self.layout.removeWidget(self.winOrLoseLabel)
        self.winOrLoseLabel = QLabel("")

    def turnOnFlags(self,event):
        if event.key() == Qt.MouseButton:
            print("yes")

    def print_coordinates(self, x, y):
        it = self.board.itemAtPosition(x, y)
        w = it.widget()
        #print(w.pos())

    def buttonClicked(self,row,col):
        clicked = self.sender()
        symbol = clicked.text()  # the buttons have the symbols on them
        print("Button was clicked!")
        #print(clicked.text(), ":", clicked.pos(), clicked.geometry())
        clicked.setEnabled(False)

        sound = QSound("WindowsXPPrintcomplete.wav")
        sound.play("WindowsXPPrintcomplete.wav")
        print(row)
        print(col)

        self.buttons[row][col] = QLabel(str(self.mine.getSquare(row,col)))
        self.buttons[row][col].setAlignment(Qt.AlignCenter)
        self.buttons[row][col].setStyleSheet("background-color : lightblue")
        #self.buttons[row][col] = QLabel(str(self.mine.getSquare(row,col)))
        #self.buttons[row][col] = QLabel("       ?")
        self.board.addWidget(self.buttons[row][col], row, col)

        # Have to tell the model about the move here


        # Update the puzzle
        if self.mine.getGameState() == 0:
            # We lose here
            print("You lost the game")
            self.disableAllButtons()
            self.mine.revealAllBombs(self.board,self.buttons)
            self.setFlagWinOrLoseLabel("You lose")

            sound = QSound("WindowsXPStartup.wav")
            sound.play("WindowsXPStartup.wav")

            pixmap = QPixmap("windows3.png")
            self.buttons[row][col].setStyleSheet("background-color : #ff1919")
            self.buttons[row][col].setPixmap(pixmap)
            self.buttons[row][col].setAlignment(Qt.AlignCenter)
            #exit(0)

        elif self.mine.getGameState() == 1:
            # We win here
            print("You win the game")
            sound = QSound("tada.wav")
            sound.play("tada.wav")
            self.disableAllButtons()
            self.setFlagWinOrLoseLabel("You win")


    def disableAllButtons(self):
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                self.buttons[i][j].setEnabled(False)
                grab = self.puzzle[i][j]
                print(self.puzzle[i][j].revealed())
                if grab.revealed() == True:
                    #self.buttons[i][j].setEnabled(True) #TODO: Something is wrong here
                    self.buttons[i][j] = QLabel(str(self.mine.getSquare(i, j)))
                    self.buttons[i][j].setAlignment(Qt.AlignCenter)


    def setFlagWinOrLoseLabel(self,label):
        self.winOrLoseLabel = QLabel(label)
        flagFont = QFont("Times", 14, QFont.Bold)
        self.winOrLoseLabel.setFont(flagFont)
        self.winOrLoseLabel.setFrameStyle(QFrame.Sunken)
        self.winOrLoseLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.winOrLoseLabel)
        # TODO: Need to now the "Time"

