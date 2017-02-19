import sys
import os
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
							 QHBoxLayout, QLabel, QLineEdit, QTabBar,
							 QFrame, QStackedLayout)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class ToolBar:

	def __init__(self):
		self.toolbar = QWidget()
		self.toolbarLayout = QHBoxLayout()
		self.toolbar.setLayout(self.toolbarLayout)