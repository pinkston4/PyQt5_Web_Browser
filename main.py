import sys
import os
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
							 QHBoxLayout, QLabel, QLineEdit, QTabBar,
							 QFrame, QStackedLayout)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from wb.app import CreateApp

class App(QFrame):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("PyQt5 Web Browser")
		self.wb_app = CreateApp()
		self.setLayout(self.wb_app.layout)
		self.show()
		self.setBaseSize(1280, 720)

if __name__ =='__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())
