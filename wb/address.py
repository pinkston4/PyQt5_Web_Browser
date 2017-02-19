import sys
import os
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
							 QHBoxLayout, QLabel, QLineEdit, QTabBar,
							 QFrame, QStackedLayout)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


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
		mousePressEvent is a built in method in QLineEdit by redifining it here and passing in an argument 
		by default it will now select all the text in the address bar vs just one space
		"""
		self.selectAll()