#!/usr/bin/env python

from PyQt4 import *
from PyQt4.QtCore import *

sLine = ""
class pydeTemplates:
      
  def getTemplatesListOf(self,language):    
    file = QtCore.QFile(self.filename)	
    listTemplates = QtCore.QStringList()
    if( file.open( QIODevice.ReadOnly) ): 
      ts = QtCore.QTextStream(file)   

      while True:
  	line = str(ts.readLine())     
     	if line == "":
	  #end of file
	  break	  
        if line.find("<" + language + ">") != -1:
	  #right language
	  #get template name
	  listTemplates.append(line.split(" ", 1)[1])
	
      file.close()
    return listTemplates

  def loadTemplates(self, language, template):
    file = QtCore.QFile(self.filename)	
    templateContent = ""
    if( file.open( QIODevice.ReadOnly) ): 
      ts = QtCore.QTextStream(file)  
      while True:
        line = str(ts.readLine())     
	if line.find("<" + language + ">") != -1:
	  #first check right language
	  if line.split(" ", 1)[0].strip("<>") == language:
	    #second, check right template
	    if line.split(" ", 1)[1] == template:
	      #read and store template    
              while True:
	        line = str(ts.readLine()) 
	        if line.find("<end>") != -1:
		  break
	        else:
		  templateContent += line + "\n"
	      #template read, leave file reading
              break
	if line == "":
	  #end of file
	  break	     
      
    return templateContent
  
  def __init__(self, filename):
    self.filename = filename
  	
	
if __name__ == '__main__':
  a = pydeTemplates("templates")
  a.getTemplatesListOf("py")	

 


