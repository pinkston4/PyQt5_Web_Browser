import sys
from PyQt5.QtWidgets import QApplication, QFrame
from wb.app import CreateApp


class App(QFrame):
    """
    This is where the app is initialized
    only one method and it is the __init__ method
    essentially this module acts as the on off switch for the app
    Author: Jack Pinkston
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Web Browser")
        self.wb_app = CreateApp()
        self.setLayout(self.wb_app.layout)
        self.show()
        self.setBaseSize(1280, 720)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
