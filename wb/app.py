import sys
import os
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
							 QHBoxLayout, QLabel, QLineEdit, QTabBar,
							 QFrame, QStackedLayout)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from . import tab
from . import address
from . import toolbar
from . import mainView

class CreateApp:

	def __init__(self):
		self.createLayout()

	def createLayout(self):
		self.layout = QVBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0, 0, 0, 0)

		self.tabbar = tab.TabBar()

		self.addressBar = address.AddressBar()

		self.toolbar = toolbar.ToolBar()
		self.toolbar.toolbarLayout.addWidget(self.addressBar)
		self.toolbar.toolbarLayout.addWidget(self.tabbar.addTabButton)

		self.container = mainView.Container()

		self.layout.addWidget(self.tabbar.tabbar)
		self.layout.addWidget(self.toolbar.toolbar)
		self.layout.addWidget(self.container.container)

		self.container.container.layout.addWidget(self.tabbar.tabs[0])
		self.container.container.layout.setCurrentWidget(self.tabbar.tabs[0])
		self.tabbar.tabbar.addTab("New Tab")
		self.tabbar.tabbar.setTabData(0, 'tab' + str(0))




