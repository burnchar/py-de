## Code norms ##

Each visible string must be used with the translate method:

```
QtGui.QApplication.translate("className", "string", "comment", encoding)
```

Example:
```
self.menuFile.setTitle(QtGui.QApplication.translate("py_de", "File", None, QtGui.QApplication.UnicodeUTF8))
```

Note: the comment is here to help the translator in cases where the translation could be
ambiguous.

## Generate xml files ##

1. All the python files that you need to translate have to referenced in the py-de.pro after the "SOURCES" tag.
```
 SOURCES += py-de.py
```
2. In py-de.pro, after "TRANSLATIONS" tag, write the xml files (.ts) that you need: one file for each language. Name them:
```
TRANSLATIONS = pyde_fr.ts pyde_es.ts
```
  * pyde\_fr.ts: french version
  * pyde\_es.ts: spanish version
  * ...

3. Finally launch the following command to generate this files:
```
  $> pylupdate4 py-de.pro
```




## Generate binary files ##

  1. Open QtLinguist.

![http://www.siteduzero.com/uploads/fr/files/118001_119000/118042.png](http://www.siteduzero.com/uploads/fr/files/118001_119000/118042.png)

  1. Load one translation file (.ts)
  1. Translate
  1. Generate the binary file (.qm): File => release

## Adapt internationalization to the application ##

```
app = QtGui.QApplication(sys.argv)
   
#Select language according to the user system
locale = QtCore.QLocale.system().name().section('_', 0, 0)

#load binary translation file (.qm)
translator = QtCore.QTranslator()
translator.load(QtCore.QString("pyde_") + locale)

#add translator to the main app
app.installTranslator(translator)
```