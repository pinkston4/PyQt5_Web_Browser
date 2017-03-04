from PyQt5.QtWidgets import QWidget, QHBoxLayout


class ToolBar:

    def __init__(self):
        self.toolbar = QWidget()
        self.toolbarLayout = QHBoxLayout()
        self.toolbar.setLayout(self.toolbarLayout)
