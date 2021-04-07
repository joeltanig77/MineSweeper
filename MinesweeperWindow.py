from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import Qt
from MinesweeperModel import *

# This is the view controler

class MinesweeperWindow(QMainWindow):
    def __init__(self):
        super(MinesweeperWindow,self).__init__()
        self.mine = MinesweeperModel()

        # Add a widget at the center
        widget = QWidget()
        self.setCentralWidget(widget)

        # we'll stack the puzzle above the grid of buttons with this
        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.buttons =[]

        #Add grid logic
        self.board = QGridLayout()
        for i in range(100):
            button = QPushButton("X")
            button.clicked.connect(self.buttonClicked)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.buttons.append(button)
            row = i // 10 # integer division by # of columns to get the row
            col = i % 10  # remainder when divided by # of cols gives us a column
            self.board.addWidget(self.buttons[i],row,col)
        QTimer.singleShot(0, lambda: self.print_coordinates(1, 1))
        layout.addLayout(self.board)


        # only two menu items, so may as well set them up here
        menu = self.menuBar().addMenu("&Game")
        newAct = QAction("&New", self, shortcut=QKeySequence.New, triggered=self.newGame)
        menu.addAction(newAct)
        menu.addSeparator()
        quitAct = QAction("E&xit", self, shortcut=QKeySequence.Quit, triggered=self.close)
        menu.addAction(quitAct)

        # Set the title here
        self.setWindowTitle("MineSweeper")

        # This is the game logic
        # Start the game here
        self.mine.newGame()
      #  while mine.getGameState() == -1:
            #Ask for user input here
       #     pass

        print(self.mine.getSquare(0, 0))
        print("Yes")
        if self.mine.getGameState() == 0:
            self.mine.revealAllBombs()
            exit(0)

    def newGame(self):
        print("New game started!")

        # Reset the buttons
        for button in self.buttons:
            button.setEnabled(True)

        # Call the new game from the model
        self.mine.newGame()


    def print_coordinates(self, x, y):
        it = self.board.itemAtPosition(x, y)
        w = it.widget()
        print(w.pos())

    def buttonClicked(self):
        clicked = self.sender()
        symbol = clicked.text()  # the buttons have the symbols on them
        print("Button was clicked!")

        clicked.setEnabled(False)
        # Have to tell the model about the move here
        self.mine.getSquare(0,0)

        # Update the puzzle
        if self.mine.getGameState() == 0:
            # We lose here
            print("You lost the game")
            pass
        elif self.mine.getGameState() == 1:
            # We win here
            print("You win the game")
            pass
        else:
            # Continue the game
            pass


    @pyqtSlot()
    def on_clicked(self):
        button = self.sender()
        print(button.text(), ":", button.pos(), button.geometry())