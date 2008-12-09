#!/usr/bin/env python

from PyQt4 import *
from PyQt4.QtCore import *

sLine = ""
class pydeTemplates:
      
  def getTemplatesListOf(self,language):    
    #file = QtCore.QFile(self.filename)	
    listTemplates = QtCore.QStringList()
    file = open(self.filename, 'r')

    for line in  file.readlines():
      if line.find("<" + language + ">") != -1:
	#right language
	#get template name
	listTemplates.append(line.split(" ", 1)[1].strip())
	
    file.close()
    return listTemplates

  def loadTemplate(self, language, template):
    file = open(self.filename, 'r')	
    templateContent = ""
    read = False
    for line in file.readlines():
      print line
      if read:
	#template found => read template      
	if line.find("<end>") != -1:
          break
	else:
          templateContent += line 
      elif line.find("<" + language + ">") != -1:
	#first check right language
	if line.split(" ", 1)[0].strip("<>") == language:
	  #second, check right template
	  if line.split(" ", 1)[1].strip() == template:
	    #read and store template    
            read = True
    return templateContent
	      
  def newTemplate(self, template, language, name):
    file = QtCore.QFile(self.filename)	
    if( file.open( QIODevice.Append) ):
      buf = "\n<"
      buf += language
      buf += "> "
      buf += name + "\n"
      buf += template
      buf += "\n<end>"
      file.write(str(buf))
  
  def __init__(self, filename):
    self.filename = filename
  	
	
if __name__ == '__main__':
  a = pydeTemplates("templates")
  a.getTemplatesListOf("py")	

 


