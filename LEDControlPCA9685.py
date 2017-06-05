#!/usr/bin/env python
# coding: latin-1
# Autor:   Ingmar Stapel
# Datum:   20170605
# Version:   1.0
# Homepage:   http://custom-build-robots.com
# Dieses Programm ist das sogenannte Steuerprogramm fuer die 
# Helligkeit z. B. eines LED Bandes ueber die Konsole und Tastatur
# vom PC aus.


# Es werden verschiedene Python Klassen importiert deren Funktionen
# im Programm benoetigt werden fuer die Programmverarbeitung.
import sys, tty, termios, os, readchar

# Das Programm L298NHBridgePCA9685.py wird als Modul geladen. Es 
# stellt die Funktionen fuer die Steuerung der H-Bruecke zur 
# Verfuegung.
import L298NHBridgePCA9685 as HBridge

# Variablen Definition der Helligkeit für den Linken Kanal an der
# L298N H-Bruecke.
channel_left = 0
channel_right = 0

# Das Menue fuer den Anwender wenn er das Programm ausfuehrt.
# Das Menue erklaert mit welchen Tasten die LED geregelt wird.
print("w/s: heller / dunkler")
print("x: Programm beenden")

# Die Funktion getch() nimmt die Tastatureingabe des Anwenders
# entgegen. Die gedrueckten Buchstaben werden eingelesen. Sie werden
# benoetigt um die Helligkeit der LED festzulegen.
def getch():
   ch = readchar.readchar()
   return ch

# Die Funktion printscreen() gibt immer das aktuelle Menue aus
# sowie die Helligkeit der LED.
def printscreen():
   # der Befehl os.system('clear') leert den Bildschirmihalt vor
   # jeder Aktualisierung der Anzeige. So bleibt das Menue stehen
   # und die Bildschirmanzeige im Terminal Fenster steht still.
   os.system('clear')
   print("========== LED Kontroller ==========")   
   print("w/s: heller / dunkler")
   print("x:   Programm beenden")
   print("========== LED Helligkeit ==========")
   print "Helligkeit linker Kanal:  ", channel_left*100, "%"
   print "Helligkeit rechter Kanal:  ", channel_right*100, "%"
# Diese Endlosschleife wird erst dann beendet wenn der Anwender 
# die Taste X tippt. Solange das Programm laeuft wird ueber diese
# Schleife die Eingabe der Tastatur eingelesen.
while True:
   # Mit dem Aufruf der Funktion getch() wird die Tastatureingabe 
   # des Anwenders eingelesen. Die Funktion getch() liesst den 
   # gedrueckte Buchstabe ein und uebergibt diesen an die 
   # Variablechar. So kann mit der Variable char weiter 
   # gearbeitet werden.
   char = getch()
   
   # Die LED wird heller.
   if(char == "w"):
      # Die LED wird in Schritten von 10% heller mit jedem 
	  # Tastendruck des Buchstaben "w" bis maximal 100%.
      channel_left = channel_left + 0.1
      channel_right = channel_right + 0.1
	  
      if channel_left > 1:
         channel_left = 1
      if channel_right > 1:
         channel_right = 1		 
      # Dem Programm L298NHBridgePCA9685 welches zu beginn  
      # importiert wurde wird die Helligkeit fuer 
      # die LED uebergeben.
      HBridge.setMotorLeft(channel_left)
      HBridge.setMotorRight(channel_right)
      printscreen()

   # Die LED wird dunkler wenn die Taste "s" gedrueckt wird.
   if(char == "s"):
      # Die LED wird in Schritten von 10% dunler mit jedem 
	  # Tastendruck des Buchstaben "w" bis maximal 0%.
      channel_left = channel_left - 0.1
      channel_right = channel_right - 0.1
	  
      if channel_left < -1:
         channel_left = -1
      if channel_right < -1:
         channel_right = -1       
      # Dem Programm L298NHBridgePCA9685 welches zu beginn  
      # importiert wurde wird die Helligkeit fuer 
      # die LED uebergeben.     
      HBridge.setMotorLeft(channel_left)
      HBridge.setMotorRight(channel_right)	  
      printscreen()
      
   # Mit der Taste "x" wird die Endlosschleife beendet 
   # und das Programm wird ebenfalls beendet. Zum Schluss wird 
   # noch die Funktion exit() aufgerufen die das PWM signal beendet.
   if(char == "x"):
      HBridge.setMotorLeft(0)
      HBridge.exit()
      print("Program Ended")
      break
   
   # Die Variable char wird pro Schleifendurchlauf geleert. 
   # Das ist notwendig um weitere Eingaben sauber zu übernehmen.
   char = ""
   
# Ende des Programmes
