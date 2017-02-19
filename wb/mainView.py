import sys
import os
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
							 QHBoxLayout, QLabel, QLineEdit, QTabBar,
							 QFrame, QStackedLayout)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class Container:

	def __init__(self):
		self.container = QWidget()
		self.container.layout = QStackedLayout()
		self.container.setLayout(self.container.layout)