from PyQt4 import QtGui
import sys

sys.path.insert(0, '.')
from gui.ui_main import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_hello_world.clicked.connect(self.hello_world)

    def hello_world(self):
        QtGui.QMessageBox.information(self, 'Hello World', 'Hello World!')


if __name__ == '__main__':

    # Use Existing Adams QAplication
    app = QtGui.QApplication.instance()

    # Create the GUI
    main_editor = MainWindow()
    main_editor.show()
