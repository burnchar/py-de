#!/usr/bin/env python

from PyQt4 import *
from PyQt4.QtCore import *

sLine = ""
class pydeTemplates:
      
  def getTemplatesListOf(self,language):    
    file = QtCore.QFile(self.filename)	
    if( file.open( QIODevice.ReadOnly) ): 
      self.ts = QtCore.QTextStream(file)   
     
     
    listTemplates = "" #use QStringList instead
    load = False
    while True:
	line = str(self.ts.readLine())     
	if line == "":
	  break	  
	
        if line.find("language") != -1:
	  #new language
	  #print line.split()[1]
	  if line.split()[1] == language:
	    load = True
	  else:
	    load = False
        elif line.find("name") != -1:	
	  #new template  
	  #print line.split(" ", 1)[1] 
	  if load == True:
	   listTemplates += line.split(" ", 1)[1]
		  
        else:
          pass  
	
    file.close()
    return listTemplates

  def __init__(self, filename):
    self.filename = filename
  	
	
if __name__ == '__main__':
  a = pydeTemplates("templates")
  a.getTemplatesListOf("py")	

 


