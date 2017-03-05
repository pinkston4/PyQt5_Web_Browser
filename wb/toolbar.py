from PyQt5.QtWidgets import QWidget, QHBoxLayout


class ToolBar:
    """
    the TooBar class sets the layout for the toolbar, a horizontal bar
    only method is __init__
    """

    def __init__(self):
        self.toolbar = QWidget()
        self.toolbarLayout = QHBoxLayout()
        self.toolbar.setLayout(self.toolbarLayout)
