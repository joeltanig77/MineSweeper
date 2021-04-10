from PyQt5.QtWidgets import QApplication
from MinesweeperWindow import *


def main():
    app = QApplication([])
    window = MinesweeperWindow()
    window.show()
    window.setFixedSize(600, 600)
    app.exec_()


if __name__ == '__main__':
    main()
