#!/usr/bin/env python

from PyQt4 import *
from PyQt4.QtCore import *


class pydeTemplates:
  def test(self):
    file = QtCore.QFile("templates")	
    if( file.open( QIODevice.ReadOnly) ): 
      ts = QtCore.QTextStream(file)
      bip = ts.read()
      #a = file.readData(10)
      print a
      file.close()
  def __init__(self):
    pass	    
  	
	
if __name__ == '__main__':
  a = myTemplates()
  a.test()	

 


