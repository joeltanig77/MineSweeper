from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import Qt
from MinesweeperModel import *


class RightClickableButton(QPushButton):
    rightClicked = pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            QPushButton.mousePressEvent(self, event)

        elif event.button() == Qt.RightButton:
            self.rightClicked.emit()


# This is the view controller

class MinesweeperWindow(QMainWindow, QWidget):
    def __init__(self):
        super(MinesweeperWindow, self).__init__()
        self.mine = MinesweeperModel()
        self.setStyleSheet("background-color: grey")
        # Add a widget at the center
        widget = QWidget()
        self.setCentralWidget(widget)
        # we'll stack the puzzle above the grid of buttons with this
        self.layout = QVBoxLayout()
        widget.setLayout(self.layout)
        self.smallLayout = QHBoxLayout()
        self.seconds = 0
        self.muteFlag = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.winOrLoseLabel = QLabel()
        self.revealLabel = QLabel()
        self.middleTitle = QLabel()
        self.timerShow = QLabel()
        self.moveCount = QLabel()
        self.middleTitle.setText(f"Sweep the field and avoid the cursed Windows operating system!\n"
                                 f"There are {self.mine.getBombsInPlay()} bombs in play")
        self.middleTitle.setFrameStyle(QFrame.Sunken)
        font = QFont("Times", 12, QFont.Bold)
        self.middleTitle.setFont(font)
        self.moveCount.setText("Move Count: 0")
        self.timerShow.setText("Seconds: " + str(self.seconds))
        self.seconds += 1
        self.muteButton = ""
        self.gameHappen = False
        self.revealMode = True

        # GUI set up
        self.middleTitle.setAlignment(Qt.AlignCenter)
        self.moveCount.setAlignment(Qt.AlignLeft)
        self.timerShow.setAlignment(Qt.AlignRight)
        self.smallLayout.addWidget(self.moveCount)
        self.smallLayout.addWidget(self.timerShow)
        self.layout.addWidget(self.middleTitle)
        self.layout.addLayout(self.smallLayout)

        self.buttons = [[0] * (10) for i in range(10)]

        self.mine.newGame()

        self.puzzle = self.mine.getPuzzle()

        # Add grid logic
        self.board = QGridLayout()
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                button = RightClickableButton("")
                button.clicked.connect(lambda _, row=i, col=j: self.buttonClicked(row, col))
                # Right click may be implemented later
                # button.rightClicked.connect(lambda _, row=i,col=j: self.buttonClicked(row,col))
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.buttons[i][j] = button
                self.buttons[i][j].setStyleSheet("background-color : #A9A9A9")
                self.board.addWidget(self.buttons[i][j], i, j)
        self.layout.addLayout(self.board)

        # only two menu items, so may as well set them up here
        menu = self.menuBar().addMenu("&Game")
        newAct = QAction("&New", self, shortcut=QKeySequence.New, triggered=self.newGame)
        menu.addAction(newAct)
        self.muteButton = QAction("&Mute", self, shortcut=QKeySequence('Ctrl+M'), triggered=self.changeMuteFlag)
        menu.addAction(self.muteButton)
        menu.addSeparator()
        quitAct = QAction("E&xit", self, shortcut=QKeySequence.Quit, triggered=self.close)
        menu.addAction(quitAct)

        # Set the title here
        self.setWindowTitle("MineSweeper")

        self.revealLabel = QLabel("Press E to switch to flag mode")
        flagFont = QFont("Times", 14, QFont.Bold)
        self.revealLabel.setFont(flagFont)
        self.revealLabel.setFrameStyle(QFrame.Sunken)
        self.revealLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.revealLabel)

        flagFont = QFont("Times", 14, QFont.Bold)
        self.winOrLoseLabel.setFont(flagFont)
        self.winOrLoseLabel.setFrameStyle(QFrame.Sunken)
        self.winOrLoseLabel.setAlignment(Qt.AlignCenter)

        self.startTime()

        # This is the game logic
        # Restart the game here

    def newGame(self):
        print("New game started!")
        self.moveCount.setText("Move Count: 0")
        self.startTime()
        self.seconds = 0
        self.revealMode = True
        if self.gameHappen:
            self.layout.removeWidget(self.winOrLoseLabel)
        # Play the sounds
        if not self.muteFlag:
            sound = QSound("WindowsXPExclamation.wav")
            sound.play("WindowsXPExclamation.wav")
        # Reset the buttons
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                button = RightClickableButton("")
                button.clicked.connect(lambda _, row=i, col=j: self.buttonClicked(row, col))
                # button.rightClicked.connect(lambda _, row=i, col=j: self.buttonClicked(row, col))
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.buttons[i][j] = (button)
                self.buttons[i][j].setStyleSheet("background-color : #A9A9A9")
                self.board.addWidget(self.buttons[i][j], i, j)

        # Call the new game from the model
        self.mine.newGame()
        self.mine.resetReveal()
        self.winOrLoseLabel = QLabel("")

    def keyPressEvent(self, event):
        # Do toggle mode and and keep track of where you clicked, use the lamda command
        if event.key() == Qt.Key_E:
            if not self.revealMode:
                self.revealLabel.setText("Press E to switch to flag mode")
            else:
                self.revealLabel.setText("Press E to switch to reveal mode")
                print("Flag Mode")
            self.revealMode = not self.revealMode

    def buttonClicked(self, row, col):
        clicked = self.sender()
        self.updateMoveCount()
        print("Button was clicked!")
        print(row)
        print(col)
        # If we did not click a flag then do these commands
        if self.revealMode:
            if not self.muteFlag:
                sound = QSound("WindowsNavigationStart.wav")
                sound.play("WindowsNavigationStart.wav")
            clicked.setEnabled(False)
            self.buttons[row][col] = QLabel(str(self.mine.getSquare(row, col)))
            self.buttons[row][col].setAlignment(Qt.AlignCenter)
            self.buttons[row][col].setStyleSheet("background-color : lightblue")
            self.board.addWidget(self.buttons[row][col], row, col)

        else:
            # If we are in flag mode and the tile is not set as a flag then make it a flag and set the icon
            if not self.mine.getSquareForFlag(row, col).getFlag():
                self.mine.getSquareForFlag(row, col).flagToggle()
                button = QPushButton()
                button.setIcon(QIcon("error2.png"))
                button.setIconSize(QSize(25, 25))
                button.clicked.connect(lambda _, row1=row, col1=col: self.buttonClicked(row1, col1))
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.buttons[row][col] = (button)
                self.buttons[row][col].setStyleSheet("background-color : #A9A9A9")
                self.board.addWidget(self.buttons[row][col], row, col)
            # Else turn off the flag
            elif self.mine.getSquareForFlag(row, col).getFlag():
                self.buttons[row][col].setIcon(QIcon())
                self.mine.getSquareForFlag(row, col).flagToggle()

        # Update the puzzle
        if self.mine.getGameState() == 0:
            # We lose here
            print("You lost the game")
            self.timer.stop()
            self.disableAllButtons()
            self.mine.revealAllBombs(self.board, self.buttons)
            self.setFlagWinOrLoseLabel("You lose")
            if not self.muteFlag:
                sound = QSound("WindowsXPStartup.wav")
                sound.play("WindowsXPStartup.wav")

            pixmap = QPixmap("windows3.png")
            self.buttons[row][col].setStyleSheet("background-color : #ff1919")
            self.buttons[row][col].setPixmap(pixmap)
            self.buttons[row][col].setAlignment(Qt.AlignCenter)
            self.gameHappen = True

        elif self.mine.getGameState() == 1:
            # We win here
            print("You win the game")
            self.timer.stop()
            if not self.muteFlag:
                sound = QSound("tada.wav")
                sound.play("tada.wav")
            self.disableAllButtons()
            self.setFlagWinOrLoseLabel("You win")
            self.gameHappen = True

    def disableAllButtons(self):
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                self.buttons[i][j].setEnabled(False)
                grab = self.puzzle[i][j]
                print(self.puzzle[i][j].revealed())
                if grab.revealed() == True:
                    # self.buttons[i][j].setEnabled(True)
                    self.buttons[i][j] = QLabel(str(self.mine.getSquare(i, j)))
                    self.buttons[i][j].setAlignment(Qt.AlignCenter)

    def setFlagWinOrLoseLabel(self, label):
        # Sets the label to notify user if they won or lost the game
        self.winOrLoseLabel = QLabel(label)
        flagFont = QFont("Times", 14, QFont.Bold)
        self.winOrLoseLabel.setFont(flagFont)
        self.winOrLoseLabel.setFrameStyle(QFrame.Sunken)
        self.winOrLoseLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.winOrLoseLabel)

    def updateMoveCount(self):
        self.moveCount.setText("Move Count: " + str(self.mine.getMoveCount()))

    def showTime(self):
        # Update our seconds every time our system clock ticks
        self.timerShow.setText("Seconds: " + str(self.seconds))
        self.seconds += 1

    def startTime(self):
        self.timer.start(1000)

    def changeMuteFlag(self):
        # This mutes the game based on if the mute button is pressed
        if self.muteFlag == False:
            self.muteButton.setText("Un&mute")
        else:
            self.muteButton.setText("&Mute")
        self.muteFlag = not self.muteFlag
