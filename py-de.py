#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFont, QTextEdit, QCloseEvent, QFileDialog, QMenu
from PyQt4.QtGui import QInputDialog, QPrintDialog, QPrinter, QPainter
from PyQt4.QtGui import QDialog, QPaintDevice
from PyQt4.Qsci import QsciScintilla, QsciScintillaBase, QsciLexerPython
import pydeTemplates

class Ui_py_de(object):
    def setupUi(self, py_de):
        self.printer = QPrinter()

        ####################################
        ## Set up our initial window object
        ####################################

        py_de.setObjectName("py_de")
        py_de.resize(QtCore.QSize(QtCore.QRect(0,0,800,570).size()).expandedTo(py_de.minimumSizeHint()))

        self.centralwidget = QtGui.QTabWidget(py_de)
        self.centralwidget.setObjectName("centralwidget")

        self.centralwidget.setGeometry(QtCore.QRect(50,50,200,200))

	    ####################################
       	## Set up tabs
       	####################################

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.tablayout = QtGui.QGridLayout(self.tab)

	    ####################################
        ## The actual text box.
        ####################################

        self.textEdit = QsciScintilla(self.tab)

        #####################################
        ### Set the syntax highlighting.
        #####################################

        ## define the font to use
        self.font = QtGui.QFont()
        self.font.setFamily("Consolas")
        self.font.setFixedPitch(True)
        self.font.setPointSize(10)
        # the font metrics here will help
        # building the margin width later
        self.fm = QtGui.QFontMetrics(self.font)

        ## set the default font of the editor
        ## and take the same font for line numbers
        self.textEdit.setFont(self.font)
        self.textEdit.setMarginsFont(self.font)

        ## Line numbers
        # conventionaly, margin 0 is for line numbers
        self.textEdit.setMarginWidth(0, self.fm.width( "00000" ) + 5)
        self.textEdit.setMarginLineNumbers(0, True)

        ## Edge Mode shows a red vertical bar at 80 chars
        self.textEdit.setEdgeMode(QsciScintilla.EdgeLine)
        self.textEdit.setEdgeColumn(80)
        self.textEdit.setEdgeColor(QtGui.QColor("#FF0000"))

        ## Folding visual : we will use boxes
        self.textEdit.setFolding(QsciScintilla.BoxedTreeFoldStyle)

        ## Braces matching
        self.textEdit.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        ## Editing line color
        self.textEdit.setCaretLineVisible(True)
        self.textEdit.setCaretLineBackgroundColor(QtGui.QColor("#CDA869"))

        ## Margins colors
        # line numbers margin
        self.textEdit.setMarginsBackgroundColor(QtGui.QColor("#333333"))
        self.textEdit.setMarginsForegroundColor(QtGui.QColor("#CCCCCC"))

        # folding margin colors (foreground,background)
        self.textEdit.setFoldMarginColors(QtGui.QColor("#99CC66"),QtGui.QColor("#333300"))

        ## Choose a lexer
        lexer = QsciLexerPython()
        lexer.setDefaultFont(self.font)
        self.textEdit.setLexer(lexer)

        ## Render on screen
        self.textEdit.show()

        ## Show this file in the self.textEdit

        #####################################
        ## end of syntax highlighting.
        #####################################

	    ####################################
        ## Set up the sizes of everything
        ####################################

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")

        self.tablayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.centralwidget.addTab(self.tab,"")
        self.centralwidget.setCurrentIndex(0)

        py_de.setCentralWidget(self.centralwidget)

        self.createMenus(py_de)
        self.createActions(py_de)
        self.createToolBar(py_de)

        self.retranslateUi(py_de)

        #self.createTab(py_de)

        conn = QtCore.QObject.connect
        conn(self.actionNewTemplate,QtCore.SIGNAL("activated()"),self.newTemplate)
        conn(self.actionClose,QtCore.SIGNAL("triggered()"),self.closeTab)
        conn(self.actionQuit,QtCore.SIGNAL("activated()"),py_de.close)
        conn(self.actionOpen,QtCore.SIGNAL("activated()"),self.openFile)
        conn(self.actionPrint,QtCore.SIGNAL("activated()"),self.printFile)
        conn(self.actionSave,QtCore.SIGNAL("activated()"),self.saveFile)
        conn(self.actionSave_As,QtCore.SIGNAL("activated()"),self.saveAsFile)
        conn(self.actionSelect_All,QtCore.SIGNAL("activated()"),self.textEdit.selectAll)
        conn(self.actionGo_To_Line,QtCore.SIGNAL("activated()"),self.goToLine)
        conn(self.actionCopy,QtCore.SIGNAL("activated()"),self.textEdit.copy)
        conn(self.actionCut,QtCore.SIGNAL("activated()"),self.textEdit.cut)
        conn(self.actionPaste,QtCore.SIGNAL("activated()"),self.textEdit.paste)
        conn(self.actionPython_File,QtCore.SIGNAL("activated()"),self.newPythonFile)
        conn(self.actionC,QtCore.SIGNAL("activated()"),self.newCFile)
        conn(self.actionC_Header_File_h,QtCore.SIGNAL("activated()"),self.newCHeaderFile)
        conn(self.actionFortran,QtCore.SIGNAL("activated()"),self.newFortranFile)
        conn(self.actionPython_File,QtCore.SIGNAL("activated()"),lambda x="py":self.template(x))
        conn(self.actionC,QtCore.SIGNAL("activated()"),lambda x="cpp":self.template(x))
        conn(self.actionFortran,QtCore.SIGNAL("activated()"),lambda x="f":self.template(x))


        QtCore.QMetaObject.connectSlotsByName(py_de)


	    ####################################
        ## Method for creating a tab
        ####################################

    def createTab(self, py_de, ext, filename=""):
        newTabName = "tab" + str(self.centralwidget.count())
        newTextEditName = "textEdit" + str(self.centralwidget.count())
        print "createTab(): creating tab %s" % (newTabName)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(newTabName)
        self.tablayout = QtGui.QGridLayout(self.tab)
        self.centralwidget.addTab(self.tab,"")
        newTabIndex = self.centralwidget.indexOf(self.tab)
        if filename == "":
            filename = "Untitled" + str((newTabIndex + 1))
        newTabTitle = str(filename) + str(ext)
        self.centralwidget.setCurrentIndex(self.centralwidget.indexOf(self.tab))
        self.centralwidget.setTabText(newTabIndex, QtGui.QApplication.translate("py_de", newTabTitle, None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit = QsciScintilla(self.tab)
        self.textEdit.setFont(self.font)
        self.textEdit.setMarginsFont(self.font)
        self.textEdit.setMarginWidth(0, self.fm.width( "00000" ) + 5)
        self.textEdit.setMarginLineNumbers(0, True)
        self.textEdit.setEdgeMode(QsciScintilla.EdgeLine)
        self.textEdit.setEdgeColumn(80)
        self.textEdit.setEdgeColor(QtGui.QColor("#FF0000"))
        self.textEdit.setFolding(QsciScintilla.BoxedTreeFoldStyle)
        self.textEdit.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.textEdit.setCaretLineVisible(True)
        self.textEdit.setCaretLineBackgroundColor(QtGui.QColor("#CDA869"))
        self.textEdit.setMarginsBackgroundColor(QtGui.QColor("#333333"))
        self.textEdit.setMarginsForegroundColor(QtGui.QColor("#CCCCCC"))
        self.textEdit.setFoldMarginColors(QtGui.QColor("#99CC66"),QtGui.QColor("#333300"))
        lexer = QsciLexerPython()
        lexer.setDefaultFont(self.font)
        self.textEdit.setLexer(lexer)
        self.textEdit.show()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(1))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName(newTextEditName)
        self.tablayout.addWidget(self.textEdit, 0, 0, 1, 1)


	#####################################
	## Functions for menu button actions
	#####################################

    def openFile(self):
        fileName = QFileDialog.getOpenFileName()
        print fileName
        index = fileName.lastIndexOf("/")
        newFileName = fileName[index+1:]
        print newFileName
        self.createTab(py_de, "", newFileName)
        self.textEdit.setText(open(fileName).read())

    def printFile(self):
        printDialog = QPrintDialog(self.printer, py_de)
        if printDialog.exec_() == QDialog.Accepted:
            margin = 10
            pageNum = 1
            yPos = 0

            printJob = QPainter()
            printJob.begin(self.printer)
            printJob.setFont(self.font)
            fm = printJob.fontMetrics()

            #textRect = printJob.boundingRect(margin, )
            for i in range(self.textEdit.lines()):
                if margin + yPos > self.printer.height() - margin:
                    pageNum += 1
                    self.printer.newPage()
                    yPos = 0
                printJob.drawText(margin,               # X
                                  margin + yPos,        # Y
                                  self.printer.width(), # Width
                                  self.printer.height(),# Height
                                  QtCore.Qt.AlignTop,       # Alignment
                                  self.textEdit.text(i - 1)# The text to print

                                  )
                yPos += fm.lineSpacing()
            printJob.end


#/#



    def saveFile(self):
        fileName = QFileDialog.getSaveFileName()
        f = open(fileName, "w")
        f.write(self.textEdit.text())

    def saveAsFile(self):
        QKeySequence(self.textEdit.trUtf8("Ctrl+Shft+S", "File|Save As"))
        fileName = QFileDialog.getSaveFileName()
        f = open(fileName, "w")
        f.write(self.textEdit.text())

    def goToLine(self):
        maxLine = str(self.textEdit.lines())
        newLineNumber, ok = QInputDialog.getInteger(self.centralwidget,
                                                    "Go to line",
                                                    "Line number: (1, " + maxLine+")")
        if ok:
            pass
            # TODO: Find docs on qscintilla's gotoline(int)


    def cut(self):
        QKeySequence(self.textEdit.trUtf8("Ctrl+X", "Edit|Cut"))

    def copy(self):
        QKeySequence(self.textEdit.trUtf8("Ctrl+C", "Edit|Copy"))

    def paste(self):
        QKeySequence(self.textEdit.trUtf8("Ctrl+V", "Edit|Paste"))

    def find(self):
        QKeySequence(self.textEdit.trUtf8("Ctrl+F", "Edit|Find"))

    def newPythonFile(self):
        ext = ".py"
        self.createTab(py_de, ext)

    def newCFile(self):
        ext = ".cpp"
        self.createTab(py_de, ext)

    def newCHeaderFile(self):
        ext = ".h"
        self.createTab(py_de, ext)

    def newFortranFile(self):
        ext = ".f"
        self.createTab(py_de, ext)

    def closeTab(self):
        self.centralwidget.removeTab(self.centralwidget.currentIndex())


	    ##################################
        ## Function for adding actions to
	    ## various menu items.
        ##################################

    def createActions(self, py_de):
        self.actionCopy = QtGui.QAction(py_de)
        self.actionCopy.setIcon(QtGui.QIcon("images/edit-copy.png"))
        self.actionCopy.setObjectName("actionCopy")

        self.actionCut = QtGui.QAction(py_de)
        self.actionCut.setIcon(QtGui.QIcon("images/edit-cut.png"))
        self.actionCut.setObjectName("actionCut")

        self.actionPaste = QtGui.QAction(py_de)
        self.actionPaste.setIcon(QtGui.QIcon("images/edit-paste.png"))
        self.actionPaste.setObjectName("actionPaste")

        self.actionSelect_All = QtGui.QAction(py_de)
        self.actionSelect_All.setIcon(QtGui.QIcon("images/edit-select-all.png"))
        self.actionSelect_All.setObjectName("actionSelect_All")

        self.actionFind = QtGui.QAction(py_de)
        self.actionFind.setIcon(QtGui.QIcon("images/edit-find.png"))
        self.actionFind.setObjectName("actionFind")

        self.actionReplace = QtGui.QAction(py_de)
        self.actionReplace.setIcon(QtGui.QIcon("images/PLACEHOLDER.jpg"))
        self.actionReplace.setObjectName("actionReplace")

        self.actionGo_To_Line = QtGui.QAction(py_de)
        self.actionGo_To_Line.setIcon(QtGui.QIcon("images/PLACEHOLDER.jpg"))
        self.actionGo_To_Line.setObjectName("actionGo_To_Line")

        self.actionOpen = QtGui.QAction(py_de)
        self.actionOpen.setIcon(QtGui.QIcon("images/document-open.png"))
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtGui.QAction(py_de)
        self.actionSave.setIcon(QtGui.QIcon("images/document-save.png"))
        self.actionSave.setObjectName("actionSave")

        self.actionSave_As = QtGui.QAction(py_de)
        self.actionSave_As.setIcon(QtGui.QIcon("images/document-save-as.png"))
        self.actionSave_As.setObjectName("actionSave_As")

        self.actionPrint = QtGui.QAction(py_de)
        self.actionPrint.setIcon(QtGui.QIcon("images/document-print.png"))
        self.actionPrint.setObjectName("actionPrint")

        self.actionClose = QtGui.QAction(py_de)
        self.actionClose.setIcon(QtGui.QIcon("images/dialog-close.png"))
        self.actionClose.setObjectName("actionClose")

        self.actionQuit = QtGui.QAction(py_de)
        self.actionQuit.setIcon(QtGui.QIcon("images/application-exit.png"))
        self.actionQuit.setObjectName("actionQuit")

        self.actionBuild = QtGui.QAction(py_de)
        self.actionBuild.setIcon(QtGui.QIcon("images/run-build-file.png"))
        self.actionBuild.setObjectName("actionBuild")

        self.actionBuild_All = QtGui.QAction(py_de)
        self.actionBuild_All.setIcon(QtGui.QIcon("images/run-build.png"))
        self.actionBuild_All.setObjectName("actionBuild_All")

        self.actionRun = QtGui.QAction(py_de)
        self.actionRun.setIcon(QtGui.QIcon("images/arrow-right.png"))
        self.actionRun.setObjectName("actionRun")

        self.actionClean = QtGui.QAction(py_de)
        self.actionClean.setIcon(QtGui.QIcon("images/edit-clear.png"))
        self.actionClean.setObjectName("actionClean")

        self.actionAbout = QtGui.QAction(py_de)
        self.actionAbout.setIcon(QtGui.QIcon("images/help-about.png"))
        self.actionAbout.setObjectName("actionAbout")

        self.actionSelect_Language = QtGui.QAction(py_de)
        self.actionSelect_Language.setIcon(QtGui.QIcon("images/PLACEHOLDER.jpg"))
        self.actionSelect_Language.setObjectName("actionSelect_Language")

        self.actionFortran = QtGui.QAction(py_de)
        self.actionFortran.setIcon(QtGui.QIcon("images/file-fortran.png"))
        self.actionFortran.setObjectName("actionFortran")

        self.actionC = QtGui.QAction(py_de)
        self.actionC.setIcon(QtGui.QIcon("images/file-cpp.png"))
        self.actionC.setObjectName("actionC")

        self.actionPython_File = QtGui.QAction(py_de)
        self.actionPython_File.setIcon(QtGui.QIcon("images/file-python.png"))
        self.actionPython_File.setObjectName("actionPython_File")

        self.actionC_Header_File_h = QtGui.QAction(py_de)
        self.actionC_Header_File_h.setIcon(QtGui.QIcon("images/file-header.png"))
        self.actionC_Header_File_h.setObjectName("actionC_Header_File_h")

        self.actionNewTemplate = QtGui.QAction(py_de)
        self.actionNewTemplate.setObjectName("actionNewTemplate")

        self.menuNew.setIcon(QtGui.QIcon("images/document-new.png"))


        self.menuNew.addAction(self.actionC)
        self.menuNew.addAction(self.actionC_Header_File_h)
        self.menuNew.addAction(self.actionPython_File)
        self.menuNew.addAction(self.actionFortran)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
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
        self.menuTools.addAction(self.actionNewTemplate)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuBuild.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

	    ####################################
        ## Method for creating a toolbar
        ####################################

    def createToolBar(self, py_de):
        self.toolBar = QtGui.QToolBar(py_de)
        self.toolBar.setObjectName("toolBar")
        py_de.addToolBar(QtCore.Qt.TopToolBarArea,self.toolBar)

        self.toolBar.addAction(self.actionBuild)


	    ####################################
        ## Method for creating menus
        ####################################

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
        self.actionCut.setText(QtGui.QApplication.translate("py_de", "Cut", None, QtGui.QApplication.UnicodeUTF8))
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
        self.actionQuit.setText(QtGui.QApplication.translate("py_de", "Quit Py-DE", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild.setText(QtGui.QApplication.translate("py_de", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild_All.setText(QtGui.QApplication.translate("py_de", "Build All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("py_de", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClean.setText(QtGui.QApplication.translate("py_de", "Clean", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("py_de", "About Py-DE", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_Language.setText(QtGui.QApplication.translate("py_de", "Select Language", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFortran.setText(QtGui.QApplication.translate("py_de", "Fortran File (.f)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionC.setText(QtGui.QApplication.translate("py_de", "C++ Implementation File (.cpp)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPython_File.setText(QtGui.QApplication.translate("py_de", "Python File (.py)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionC_Header_File_h.setText(QtGui.QApplication.translate("py_de", "C++ Header File (.h)", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget.setTabText(self.centralwidget.indexOf(self.tab), QtGui.QApplication.translate("py_de", "Untitled 1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewTemplate.setText(QtGui.QApplication.translate("py_de", "Add file as new template", None, QtGui.QApplication.UnicodeUTF8))

    def newTemplate(self):
      o = pydeTemplates.pydeTemplates("templates")

      listLanguage = QtCore.QStringList()
      listLanguage.append("Fortran")
      listLanguage.append("Python")
      listLanguage.append("C++")

      language, res = QtGui.QInputDialog.getItem(self.centralwidget,
           QtGui.QApplication.translate("py_de", "Python templates", None, QtGui.QApplication.UnicodeUTF8),
           QtGui.QApplication.translate("py_de", "Choose language", None, QtGui.QApplication.UnicodeUTF8),
           listLanguage)
      if res:
        templateName, res = QtGui.QInputDialog.getText(self.centralwidget,
            QtGui.QApplication.translate("py_de", "Template name", None, QtGui.QApplication.UnicodeUTF8),
            QtGui.QApplication.translate("py_de", "Template name", None, QtGui.QApplication.UnicodeUTF8))
        if res:
          lang=""
          if language == "Fortran":
            lang="f"
          elif language == "C++":
            lang="cpp"
          elif language == "Python":
            lang="py"
        o.newTemplate(self.textEdit.text(), lang, templateName)

    def template(self, language):
      # Upgrade: in tools menu, add some functionalities for templates (add/remove template...) -

      #load list of templates for language selected
      o = pydeTemplates.pydeTemplates("templates")
      templates  = QtCore.QStringList(o.getTemplatesListOf(language))
      templates.prepend("Empty")

      #display dialogbox with a listbox containing list of templates
      template, res = QtGui.QInputDialog.getItem(self.centralwidget,
           QtGui.QApplication.translate("py_de", "Python templates", None, QtGui.QApplication.UnicodeUTF8),
           QtGui.QApplication.translate("py_de", "Choose template", None, QtGui.QApplication.UnicodeUTF8),
           templates)
      if res:
        #load template in the editor
        self.textEdit.setText(o.loadTemplate(language, template))

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
