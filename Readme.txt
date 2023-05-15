# AQI Project

## Variablen
Die wichtigsten globalen Variablen sind im File config.py abgelegt.
Um sie zu verwenden muss das File zu beginn jedes Codes importiert werden => import config
Die Variablen können über config.<Varibale> im Code verwendet werden.

## Preprocessing Funktionen
Die wichtigsten Funktionen sind im File preprocessing_functions.py definiert.
Um sie zu verwenden muss das File zu beginn jedes Codes importiert werden => import preprocessing_functions as pf
Die Funktionen können über pf.<Funktion> im Code verwendet werden.

## Dateninput
Der Input der Daten erfolgt aus dem File "weatherindex1.ipynb"
Es holt die Daten mittels webscraping & WebAPI ab, formt sie um und legt sie in der Datenbank ab

## Datenbank
Die Datenbank wird als Docker Container instanziiert
Um den container zu instanziieren muss das File docker-compose.yml ausgeführt werden

## Modellerstellung
Die erstellung des Models erfolgt über das File "Modeling" (?)
Es greift auf die Datenbank zu für die Datenaufbereitung
Als Ergebnis der Modellierung wird ein Model "AQI_model.pkl" bereitgestellt.

## Presentation
Der Aufruf der Funktion für die Vorhersage erfolgt aus dem File presentation.ipynb
Dieses startet auch den Webservice und ruft die Webpages & Forms auf

### Webpages
Die Benötigten Webpages (Home.html & prediction.html) sind im Folder templates abgelegt
Sie werden vom Presentation File aufgerufen

### Formular
Das auf der Webpage home.html aufgerufene Formular ist im File AQI_form.py definiert

