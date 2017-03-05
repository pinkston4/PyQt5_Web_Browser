from PyQt5.QtWidgets import QWidget, QStackedLayout


class Container:
    """
    Container is the main display of the application
    """

    def __init__(self):
        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout)
