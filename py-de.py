#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFont, QTextEdit, QCloseEvent, QFileDialog, QMenu

class Ui_py_de(object):
    def setupUi(self, py_de):
        py_de.setObjectName("py_de")
        py_de.resize(QtCore.QSize(QtCore.QRect(0,0,502,499).size()).expandedTo(py_de.minimumSizeHint()))

        self.centralwidget = QtGui.QTabWidget(py_de)
        self.centralwidget.setObjectName("centralwidget")

        self.centralwidget.setGeometry(QtCore.QRect(50,50,200,200))

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

	self.tablayout = QtGui.QGridLayout(self.tab)

        self.textEdit = QtGui.QTextEdit(self.tab)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")

	self.tablayout.addWidget(self.textEdit, 0, 0, 1, 1)

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.centralwidget.addTab(self.tab,"")
	self.centralwidget.setCurrentIndex(0)

        py_de.setCentralWidget(self.centralwidget)

	self.createMenus(py_de)
	self.createActions(py_de)

        self.statusbar = QtGui.QStatusBar(py_de)
        self.statusbar.setObjectName("statusbar")
        py_de.setStatusBar(self.statusbar)

        self.toolBar = QtGui.QToolBar(py_de)
        self.toolBar.setObjectName("toolBar")
        py_de.addToolBar(QtCore.Qt.TopToolBarArea,self.toolBar)

        self.toolBar.addAction(self.actionBuild)

        self.retranslateUi(py_de)
        QtCore.QObject.connect(self.actionQuit,QtCore.SIGNAL("activated()"),py_de.close)
        QtCore.QObject.connect(self.actionSelect_All,QtCore.SIGNAL("activated()"),self.textEdit.selectAll)
        QtCore.QObject.connect(self.actionCopy,QtCore.SIGNAL("activated()"),self.textEdit.copy)
        QtCore.QObject.connect(self.actionPaste,QtCore.SIGNAL("activated()"),self.textEdit.paste)
	QtCore.QObject.connect(self.actionPython_File,QtCore.SIGNAL("activated()"),self.template)
	
        QtCore.QMetaObject.connectSlotsByName(py_de)

    def openFile(self):
	print "bar"
        fileName = QFileDialog.getOpenFileName()
        loadFile(fileName)

    def createActions(self, py_de):
        self.actionCopy = QtGui.QAction(py_de)
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QtGui.QAction(py_de)
        self.actionPaste.setObjectName("actionPaste")

        self.actionSelect_All = QtGui.QAction(py_de)
        self.actionSelect_All.setObjectName("actionSelect_All")

        self.actionFind = QtGui.QAction(py_de)
        self.actionFind.setObjectName("actionFind")

        self.actionReplace = QtGui.QAction(py_de)
        self.actionReplace.setObjectName("actionReplace")

        self.actionGo_To_Line = QtGui.QAction(py_de)
        self.actionGo_To_Line.setObjectName("actionGo_To_Line")

        self.actionOpen = QtGui.QAction(py_de)
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtGui.QAction(py_de)
        self.actionSave.setObjectName("actionSave")

        self.actionSave_As = QtGui.QAction(py_de)
        self.actionSave_As.setObjectName("actionSave_As")

        self.actionPrint = QtGui.QAction(py_de)
        self.actionPrint.setObjectName("actionPrint")

        self.actionClose = QtGui.QAction(py_de)
        self.actionClose.setObjectName("actionClose")

        self.actionQuit = QtGui.QAction(py_de)
        self.actionQuit.setObjectName("actionQuit")

        self.actionBuild = QtGui.QAction(py_de)
        self.actionBuild.setIcon(QtGui.QIcon("icon_green_arrow.png"))
        self.actionBuild.setObjectName("actionBuild")

        self.actionBuild_All = QtGui.QAction(py_de)
        self.actionBuild_All.setObjectName("actionBuild_All")

        self.actionRun = QtGui.QAction(py_de)
        self.actionRun.setObjectName("actionRun")

        self.actionClean = QtGui.QAction(py_de)
        self.actionClean.setObjectName("actionClean")

        self.actionAbout = QtGui.QAction(py_de)
        self.actionAbout.setObjectName("actionAbout")

        self.actionSelect_Language = QtGui.QAction(py_de)
        self.actionSelect_Language.setObjectName("actionSelect_Language")

        self.actionFortran = QtGui.QAction(py_de)
        self.actionFortran.setObjectName("actionFortran")

        self.actionC = QtGui.QAction(py_de)
        self.actionC.setObjectName("actionC")

        self.actionPython_File = QtGui.QAction(py_de)
        self.actionPython_File.setObjectName("actionPython_File")

        self.actionC_Header_File_h = QtGui.QAction(py_de)
        self.actionC_Header_File_h.setObjectName("actionC_Header_File_h")

        self.menuNew.addAction(self.actionC)
        self.menuNew.addAction(self.actionC_Header_File_h)
        self.menuNew.addAction(self.actionPython_File)
        self.menuNew.addAction(self.actionFortran)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionReplace)
        self.menuEdit.addAction(self.actionGo_To_Line)
        self.menuBuild.addAction(self.actionBuild)
        self.menuBuild.addAction(self.actionBuild_All)
        self.menuBuild.addAction(self.actionRun)
        self.menuBuild.addAction(self.actionClean)
        self.menuTools.addAction(self.menuFormat.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuBuild.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

    def createMenus(self, py_de):
	self.menubar = QtGui.QMenuBar(py_de)
        self.menubar.setGeometry(QtCore.QRect(0,0,502,26))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuNew = QtGui.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")

        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuBuild = QtGui.QMenu(self.menubar)
        self.menuBuild.setObjectName("menuBuild")

        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")

        self.menuFormat = QtGui.QMenu(self.menuTools)
        self.menuFormat.setObjectName("menuFormat")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        py_de.setMenuBar(self.menubar)

    def retranslateUi(self, py_de):
        py_de.setWindowTitle(QtGui.QApplication.translate("py_de", "py_de", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("py_de", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNew.setTitle(QtGui.QApplication.translate("py_de", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("py_de", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBuild.setTitle(QtGui.QApplication.translate("py_de", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("py_de", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFormat.setTitle(QtGui.QApplication.translate("py_de", "Format", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("py_de", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("py_de", "py_de", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("py_de", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("py_de", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_All.setText(QtGui.QApplication.translate("py_de", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setText(QtGui.QApplication.translate("py_de", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReplace.setText(QtGui.QApplication.translate("py_de", "Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGo_To_Line.setText(QtGui.QApplication.translate("py_de", "Go To Line", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("py_de", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("py_de", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("py_de", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setText(QtGui.QApplication.translate("py_de", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("py_de", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("py_de", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild.setText(QtGui.QApplication.translate("py_de", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild_All.setText(QtGui.QApplication.translate("py_de", "Build All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("py_de", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClean.setText(QtGui.QApplication.translate("py_de", "Clean", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("py_de", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_Language.setText(QtGui.QApplication.translate("py_de", "Select Language", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFortran.setText(QtGui.QApplication.translate("py_de", "Fortran File (.f)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionC.setText(QtGui.QApplication.translate("py_de", "C++ Implementation File (.cpp)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPython_File.setText(QtGui.QApplication.translate("py_de", "Python File (.py)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionC_Header_File_h.setText(QtGui.QApplication.translate("py_de", "C++ Header File (.h)", None, QtGui.QApplication.UnicodeUTF8))
	self.centralwidget.setTabText(self.centralwidget.indexOf(self.tab), QtGui.QApplication.translate("py_de", "Untitled 1", None, QtGui.QApplication.UnicodeUTF8))

   
    def template(self):
      #-------Test-------------------------------------------------------------------------------------
      # 1. Detect language selected
      # 2. If templates are associated to this language show pop up window
      # 3. Load list of templates  and display them in a list + option "empty file"
      # 4. Load tempplate selected and copy it on the self.textEdit
      
      # Upgrade: in tools menu, add some functionalities for templates (add/remove template...) - 
      
      templates  = QtCore.QStringList()
      templates.append("Empty")
      templates.append("Hello World")
      QtGui.QInputDialog.getItem(self.centralwidget, 
           QtGui.QApplication.translate("py_de", "Python templates", None, QtGui.QApplication.UnicodeUTF8), 
	   QtGui.QApplication.translate("py_de", "Choose template", None, QtGui.QApplication.UnicodeUTF8), 
	   templates)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    
    #Select language according to the user
    translator = QtCore.QTranslator()
    locale = QtCore.QLocale.system().name().section('_', 0, 0)
    #translator.load(QtCore.QString("pyde_") + locale)  #or translator.load("pyde_fr"); to have directly french version
    app.installTranslator(translator)
    
    py_de = QtGui.QMainWindow()
    ui = Ui_py_de()
    ui.setupUi(py_de)
    py_de.show()
    sys.exit(app.exec_())

