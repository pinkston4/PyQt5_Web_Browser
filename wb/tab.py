from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QTabBar
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class TabBar:
    """
    tab bar is where the web engine ties into place
    the tabbar is built with one tab, none of which will be displayed on screen
    Methods:
        __init__
        add_tab
    Author: Jack Pinkston
    """
    def __init__(self):
        self.tabbar = QTabBar()
        self.tab = QTabWidget()
        self.add_tab()

    def add_tab(self):
        """
        add_tab generates the tab and loads the url for that tab
        """
        self.tab.layout = QVBoxLayout()
        self.tab.content = QWebEngineView()
        self.tab.content.load(QUrl.fromUserInput("http://google.com"))
        self.tab.layout.addWidget(self.tab.content)
        self.tab.setLayout(self.tab.layout)
