import sys
import os
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
							 QHBoxLayout, QLabel, QLineEdit, QTabBar,
							 QFrame, QStackedLayout, QPushButton)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from . import app

class TabBar:
	"""
	TabBar builds the initial default tab loaded with google, and builds the button and functionality
	to add a newtab(which by default will load google)
	Methods:
		__init__
		CloseTab
		addTabs
	"""
	def __init__(self):
		self.tabbar = QTabBar(movable=True, tabsClosable=True)
		self.tabbar.tabCloseRequested.connect(self.CloseTab)
		self.addTabButton = QPushButton("+")
		self.addTabButton.clicked.connect(self.addTabs)
		self.tabCount = 0
		self.tabs = []
		self.addTabs()

	def CloseTab(self, j):
		"""
		Close tabs closes the selected tab based on index
		Arguments:
			j = index of tab you want to remove
		"""
		self.tabbar.removeTab(j)

	def addTabs(self):
		"""
		addTabs builds the initial tab and has the functionality to create additional tabs when 
		the newtab button is pressed
		"""
		j = self.tabCount
		self.tabs.append(QWidget())
		self.tabs[j].layout = QVBoxLayout()
		self.tabs[j].setObjectName('Tab ' + str(j))
		self.tabs[j].content = QWebEngineView()
		self.tabs[j].content.load(QUrl.fromUserInput("http://google.com"))
		self.tabs[j].layout.addWidget(self.tabs[j].content)
		self.tabs[j].setLayout(self.tabs[j].layout)
		self.tabbar.setCurrentIndex(0)

		