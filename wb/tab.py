from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabBar, QPushButton
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from . import app


class TabBar:
    """
    TabBar builds the initial default tab loaded with google, and builds the button and functionality
    to add a newtab(which by default will load google)
    Methods:
        __init__
        close_tab
        add_tab
    """
    def __init__(self):
        self.tabbar = QTabBar(movable=True, tabsClosable=True)
        self.tabbar.tabCloseRequested.connect(self.close_tab)
        self.addTabButton = QPushButton("+")
        self.addTabButton.clicked.connect(self.add_new_tabs)
        self.tabCount = 0
        self.tabs = []
        self.add_tab()

    def close_tab(self, j):
        """
        Close tabs closes the selected tab based on index
        Arguments:
            j = index of tab you want to remove
        """
        self.tabbar.removeTab(j)

    def add_tab(self):
        """
        addTabs builds the initial tab and has the functionality to create additional tabs when
        the newtab button is pressed
        """
        # self.tabCount += 1
        self.tabs.append(QWidget())
        self.tabs[self.tabCount].layout = QVBoxLayout()
        self.tabs[self.tabCount].setObjectName('Tab ' + str(self.tabCount))
        self.tabs[self.tabCount].content = QWebEngineView()
        self.tabs[self.tabCount].content.load(QUrl.fromUserInput("http://google.com"))
        self.tabs[self.tabCount].layout.addWidget(self.tabs[self.tabCount].content)
        self.tabs[self.tabCount].setLayout(self.tabs[self.tabCount].layout)
        # self.tabbar.setCurrentIndex(0)

    def add_new_tabs(self):
        self.tabCount += 1
        self.tabs.append(QWidget())
        self.tabs[self.tabCount].layout = QVBoxLayout()
        self.tabs[self.tabCount].setObjectName('Tab ' + str(self.tabCount))
        self.tabs[self.tabCount].content = QWebEngineView()
        self.tabs[self.tabCount].content.load(QUrl.fromUserInput("http://google.com"))
        self.tabs[self.tabCount].layout.addWidget(self.tabs[self.tabCount].content)
        self.tabs[self.tabCount].setLayout(self.tabs[self.tabCount].layout)
        app.CreateApp().update_layout()
