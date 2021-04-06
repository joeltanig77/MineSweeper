from PyQt5.QtWidgets import QApplication
from MinesweeperWindow import *

def main():
   app = QApplication([])
   window = MinesweeperWindow()
   window.show()
   app.exec_()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
