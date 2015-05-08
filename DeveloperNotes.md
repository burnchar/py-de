#This is a wiki for developers

# QT Tutorials #

http://zetcode.com/tutorials/pyqt4/

http://wiki.python.org/moin/PyQt

http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qtextedit.html

### Internationalization of PyQt4 Applications ###

http://docs.huihoo.com/pyqt/pyqt4.html#internationalisation-of-pyqt-applications

http://www.siteduzero.com/tutoriel-3-11350-traduire-son-programme-avec-qt-linguist.html


# QT Calculator by Charles Burns #

```
#!/usr/bin/env python
# simple.py

import sys, operator, math
from decimal import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QPushButton, QLineEdit, QLayout, QFont, QShortcut, QKeySequence
from PyQt4.QtCore import Qt, SLOT, SIGNAL

# TODO:
# Implement recursive descent parser for full expressions
# Compute pi based on current context's precision

class Calculator(QWidget):
	__waitingForNumber = False
	__hasDecimalPoint = False
	__multOperator = ""
	__addOperator = ""
	__product = Decimal(0)
	__sum = Decimal(0)
	__maxDisplayChars = 25
	__precision = 42

	def __init__(self, parent = None):
		getcontext().prec = self.__precision
		QWidget.__init__(self, parent)
		self.setWindowTitle('Lab 6 Calculator')
		self.setWindowIcon(QtGui.QIcon('calcicon.png'))
		self.setFont(QFont("Courier New", 18, QFont.Bold))

		grid = QtGui.QGridLayout()
		grid.setSizeConstraint(QLayout.SetFixedSize)

		self.display = QLineEdit('0.', self)
		self.display.setAlignment(QtCore.Qt.AlignRight)
		#self.display.setMaxLength(self.__maxDisplayChars)
		self.display.setReadOnly(True)
		grid.addWidget(self.display, 0, 0, 1, 5)

		# I could put this in a loop, but I wanted to keep it simple
		self.btnSquare = self.createButton('x^2', grid, self.btnSquareClicked)
		self.btnDigit7 = self.createButton('7', grid, self.btnDigitClicked)
		self.btnDigit8 = self.createButton('8', grid, self.btnDigitClicked)
		self.btnDigit9 = self.createButton('9', grid, self.btnDigitClicked)
		self.btnDivide = self.createButton('/', grid, self.mult)

		self.btnExponent = self.createButton('x^y', grid, self.mult)
		self.btnDigit4 = self.createButton('4', grid, self.btnDigitClicked)
		self.btnDigit5 = self.createButton('5', grid, self.btnDigitClicked)
		self.btnDigit6 = self.createButton('6', grid, self.btnDigitClicked)
		self.btnMultiply = self.createButton('*', grid, self.mult)

		self.btnSquareRoot = self.createButton('Sqrt', grid, self.btnSqrtClicked)
		self.btnDigit1 = self.createButton('1', grid, self.btnDigitClicked)
		self.btnDigit2 = self.createButton('2', grid, self.btnDigitClicked)
		self.btnDigit3 = self.createButton('3', grid, self.btnDigitClicked)
		self.btnSubtract = self.createButton('-', grid, self.add)

		self.btnPercent = self.createButton('%', grid, self.btnPercentClicked)
		self.btnDigit0 = self.createButton('0', grid, self.btnDigitClicked)
		self.btnPeriod = self.createButton('.', grid, self.btnPeriodClicked)
		self.btnChangeSign = self.createButton('+/-', grid, self.btnChangeSignClicked)
		self.btnAdd = self.createButton('+', grid, self.add)

		self.btnPi = self.createButton('Pi', grid, self.btnPiClicked)
		self.btnInvert = self.createButton('1/x', grid, self.btnInvertClicked)
		self.btnFactorial = self.createButton('!', grid, self.btnFactorialClicked)
		self.btnExponent = self.createButton('Clr', grid, self.btnClearClicked)
		self.btnEquals = self.createButton('=', grid, self.btnEqualsClicked)

		self.setLayout(grid)

	def keyPressEvent(self, event):
		result = {
			Qt.Key_0: lambda : self.btnDigitClicked(self.btnDigit0),
			Qt.Key_1: lambda : self.btnDigitClicked(self.btnDigit1),
			Qt.Key_2: lambda : self.btnDigitClicked(self.btnDigit2),
			Qt.Key_3: lambda : self.btnDigitClicked(self.btnDigit3),
			Qt.Key_4: lambda : self.btnDigitClicked(self.btnDigit4),
			Qt.Key_5: lambda : self.btnDigitClicked(self.btnDigit5),
			Qt.Key_6: lambda : self.btnDigitClicked(self.btnDigit6),
			Qt.Key_7: lambda : self.btnDigitClicked(self.btnDigit7),
			Qt.Key_8: lambda : self.btnDigitClicked(self.btnDigit8),
			Qt.Key_9: lambda : self.btnDigitClicked(self.btnDigit9),
			Qt.Key_Plus: lambda : self.add('+'),
			Qt.Key_Minus: lambda : self.add('-'),
			Qt.Key_Asterisk: lambda : self.mult('*'),
			Qt.Key_Slash: lambda : self.mult('/'),
			Qt.Key_Backslash: lambda : self.mult('\\'),
			Qt.Key_Exclam: lambda : self.btnFactorialClicked(),
			Qt.Key_Percent: lambda : self.btnPercentClicked(),
			Qt.Key_Period: lambda : self.btnPeriodClicked(),
			Qt.Key_Comma: lambda : self.btnPeriodClicked(),
			Qt.Key_Enter: lambda : self.btnEqualsClicked(),
			Qt.Key_Return: lambda : self.btnEqualsClicked(),
			Qt.Key_Equal: lambda : self.btnEqualsClicked(),
			Qt.Key_P: lambda : self.btnPiClicked(),
			Qt.Key_R: lambda : self.btnInvertClicked(),
			Qt.Key_At: lambda : self.btnSqrtClicked(),
			Qt.Key_Y: lambda : self.mult('^'),
			Qt.Key_S: lambda : self.btnSquareClicked(),
			Qt.Key_Escape: lambda : self.btnClearClicked(),
		}
		result.get(event.key(), self.unmappedKeyPressed)()

	def createButton(self, text, layout, handler):
		retval = QPushButton(text)
		self.connect(retval, SIGNAL("clicked()"), handler)
		layout.addWidget(retval)
		return retval

	def unmappedKeyPressed(self):
		pass

	def btnSquareClicked(self):
		newDisplay = Decimal(self.getDisplay()) ** 2
		self.setDisplay(newDisplay)
		self.__waitingForNumber = True
		self.__hasDecimalPoint = False

	def btnSqrtClicked(self):
		newDisplay = Decimal(self.getDisplay()) ** Decimal("0.5")
		self.setDisplay(newDisplay)
		self.__waitingForNumber = True
		self.__hasDecimalPoint = False

	def btnPercentClicked(self):
		newDisplay = Decimal(self.getDisplay()) / 100
		self.setDisplay(newDisplay)
		self.__waitingForNumber = True
		self.__hasDecimalPoint = False

	def btnPiClicked(self):
		newDisplay = Decimal(str("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117"))
		self.setDisplay(newDisplay)
		self.__waitingForNumber = True
		self.__hasDecimalPoint = False

	def setDisplay(self, value):
		toDisplay = str(value)
		rounded = Decimal(0)
		if type(value) == type(rounded): # If we got a Decimal
			getcontext().prec = (self.__maxDisplayChars - 8)
			rounded = +Decimal(value) # Round down to fit
			toDisplay = str(rounded)
			if len(toDisplay) >= 2 and toDisplay[-1] == '0' and not 'E' in toDisplay and '.' in toDisplay:
				toDisplay = toDisplay.rstrip('0')

		if not '.' in toDisplay:
			toDisplay += '.'
		self.display.setText(toDisplay)
		getcontext().prec = self.__precision

	# Returns display as string containing a number with no trailing '.'
	def getDisplay(self):
		retval = str(self.display.text()).rstrip('.')
		try: Decimal(retval)
		except:
			retval = "0"
		return retval

	def add(self, operator = None):
		if not operator:
			operator = str(self.sender().text())
		number = Decimal(self.getDisplay())

		if self.__multOperator:
			self.setDisplay(self.__product)
			number = self.__product
			self.__product = 0
			self.__multOperator = ""
		if self.__addOperator:
			self.compute(operator, number)
			self.setDisplay(self.__sum)
		else:
			self.__sum = number
		self.__addOperator = operator
		self.__waitingForNumber = True


	def mult(self, operator = None):
		if not operator:
			operator = str(self.sender().text())
		if operator.lower() == "x^y": operator = '^'
		number = Decimal(self.getDisplay())
		if self.__multOperator:
			self.compute(self.__multOperator, number)
			self.__multOperator = ""
			self.setDisplay(self.__product)
		else:
			self.__product = number
		self.__multOperator = operator
		self.__waitingForNumber = True

	def btnPeriodClicked(self):
		self.__hasDecimalPoint = True
		if self.__waitingForNumber == True:
			self.setDisplay(Decimal('0'))
		self.__waitingForNumber = False;

	# TODO: Refactor this
	def btnDigitClicked(self, mySender = False):
		newDisplay = "0"
		displayVal = self.getDisplay()
		buttonVal = ""
		if mySender:
			buttonVal = str(mySender.text())
		else:
			buttonVal = str(self.sender().text())
		if self.__waitingForNumber:
			newDisplay = buttonVal
			self.__waitingForNumber = False
		else:
			if(self.__hasDecimalPoint):
				if not '.' in self.getDisplay():
					newDisplay = self.getDisplay() + '.' + buttonVal
				else:
					newDisplay = self.getDisplay() + buttonVal
			elif Decimal(displayVal).to_integral_value(rounding = ROUND_FLOOR) > 0:
				newDisplay = str((Decimal(displayVal) * 10) + int(buttonVal))
			elif not buttonVal == '0':
				newDisplay = buttonVal
		self.setDisplay(newDisplay)

	def btnInvertClicked(self):
		try:
			newDisplay = 1 / Decimal(self.getDisplay())
		except(ZeroDivisionError):
			newDisplay = "Zero has no inverse."
		self.setDisplay(newDisplay)
		self.__waitingForNumber = True

	def btnFactorialClicked(self):
		number = Decimal(self.getDisplay())
		if not long(number) == number:
			self.setDisplay("Must be a whole number")
		else:
			result = Decimal(1)
			while number > 1:
				result, number = long(result) * number, number - 1
			self.setDisplay(result)
		self.__waitingForNumber = True

	def btnEqualsClicked(self):
		number = Decimal(self.getDisplay())
		if self.__multOperator:
			self.compute(self.__multOperator, number)
			number = self.__product
			self.__product = 0
			self.__multOperator = ""
		if self.__addOperator:
			self.compute(self.__addOperator, number)
			self.__addOperator = ""
		else:
			self.__sum = number
		self.__waitingForNumber = True
		self.setDisplay(self.__sum)
		self.__sum = 0

	def compute(self, operator, number):
		if operator == '+':
			self.__sum += number
		elif operator == '-':
			self.__sum -= number
		elif operator == '*':
			self.__product *= number
		elif operator == '/':
			self.__product /= number
		elif operator == '^':
			self.__product **= number
		return True

	#Factor with add operation function
	def btnChangeSignClicked(self):
		try:
			num = Decimal(str(self.display.text()))
			num *= -1
			self.setDisplay(str(num))
		except ValueError:
			self.setDisplay("Invalid number")

	def btnClearClicked(self):
		self.__hasDecimalPoint = False
		self.__waitingForNumber = True
		self.__addOperator = ""
		self.__multOperator = ""
		self.setDisplay('0')




app = QtGui.QApplication(sys.argv)

calc = Calculator()
calc.show()

retval = app.exec_()
sys.exit(retval)
```