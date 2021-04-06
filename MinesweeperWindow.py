from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MinesweeperModel import *

# This is the view controler

class MinesweeperWindow(QMainWindow):
    def __init__(self):
        super(MinesweeperWindow,self).__init__()

        # Add a widget at the center
        widget = QWidget()
        self.setCentralWidget(widget)

        # we'll stack the puzzle above the grid of buttons with this
        layout = QVBoxLayout()
        widget.setLayout(layout)

        #TODO: Figure out how to reference the bottom widget




        #Add grid logic
        mine = MinesweeperModel()
        mine.newGame()