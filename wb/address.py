from PyQt5.QtWidgets import QLineEdit


class AddressBar(QLineEdit):
    """
    AddressBar class inherits from QLineEdit
    Methods:
        __init__
        mousePressEvent
    """

    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        """
        mousePressEvent is a built in method in QLineEdit by redefining it here and passing in an argument
        by default it will now select all the text in the address bar vs just one space
        Author: Jack Pinkston
        """
        self.selectAll()
