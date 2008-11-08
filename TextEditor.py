#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PYDE(QWidget):

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)

		#set the initial location, size, and title of the window
		self.setGeometry(300, 100, 500, 500)
		self.setWindowTitle(self.tr('PYDE'))

		#set the initial text and font
		self.text = self.tr("PYDE")
		self.font = QFont()

		self.addWidget()

	def addWidget(self):
		#create the text editor
		textEditor = QTextEdit(self.text)

		#create the font box
		fontLabel = QLabel(self.tr("&Font:"))
		fontCombo = QFontComboBox()
		self.connect(fontCombo, SIGNAL("currentFontChanged(const QFont &)"), textEditor, SLOT('setCurrentFont(QFont(self.font))'))
		fontLabel.setBuddy(fontCombo)

		#set up the horizontal layout
		hlayout = QHBoxLayout()
		hlayout.addWidget(fontLabel)
		hlayout.addWidget(fontCombo, 2)

		#set up the vertical layout
		vlayout = QVBoxLayout()
		vlayout.addLayout(hlayout)
		vlayout.addWidget(textEditor)
		self.setLayout(vlayout)

if __name__ == "__main__":

	#set up the application
	app = QApplication(sys.argv)
	window = PYDE()
	window.show()

	#calls sys.exit when the window is closed
	sys.exit(app.exec_())

