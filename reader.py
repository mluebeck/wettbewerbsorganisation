import unittest
import csv

import csv
import random

class AngemeldetePerson:
    def __init__(self, vorname, nachname, mitgliedsnummer, sixMonth, clubnummer, clubname, spracheDe, spracheEn, magAufgabe, level1Und2, preisrichter, moderator, zeitnehmer, counter, wettbewerbsleiter, saaldiener): 
        self.vorname = vorname 
        self.nachname = nachname 
        self.mitgliedsnummer = mitgliedsnummer
        self.sixMonth = sixMonth
        self.clubnummer = clubnummer
        self.clubname = clubname 
        self.spracheDe = spracheDe
        self.spracheEn = spracheEn
        self.magAufgabe = magAufgabe
        self.Level1Und2 = level1Und2
        self.preisrichter = preisrichter
        self.moderator = moderator
        self.zeitnehmer = zeitnehmer
        self.counter = counter 
        self.wettbewerbsleiter = wettbewerbsleiter 
        self.saaldiener  = saaldiener 

class ListeVonPersonen:
    def __init__(self):
        self.daten = []
    def addPerson(self,person):
        self.daten.append(person)

    def filter(name, daten):
         resultat = ListeVonPersonen()
         resultat.daten = list(filter(lambda x : getattr(x,name) == "ja" ,daten.daten))
         return resultat 

    def magAufgabe(daten):
         return ListeVonPersonen.filter("magAufgabe",daten) 

    def istSeitMehrAlsSechsMonatenDabei(daten):
        return ListeVonPersonen.filter("sixMonth",daten) 

    def level1Und2(daten):
        return ListeVonPersonen.filter("Level1Und2",daten) 

    def spracheDE(daten):
        return ListeVonPersonen.filter("spracheDE",daten) 

    def spracheEN(daten):
        return ListeVonPersonen.filter("spracheEN",daten) 

    #Preisrichter,Moderator,Zeitnehmer,Auszähler,Wettbewerbsleiter,Saaldiener
    def preisrichter(daten):
        return ListeVonPersonen.filter("preisrichter",daten) 

    def counter(daten):
        resultat = ListeVonPersonen()
        resultat.daten = list(filter(lambda x : x.counter == "ja" ,daten.daten))
        return resultat 

    def moderator(daten):
        resultat = ListeVonPersonen()
        resultat.daten = list(filter(lambda x : x.moderator == "ja" ,daten.daten))
        return resultat 

    def zeitnehmer(daten):
        resultat = ListeVonPersonen()
        resultat.daten = list(filter(lambda x : x.zeitnehmer == "ja" ,daten.daten))
        return resultat 

    def wettbewerbsleiter(daten):
        resultat = ListeVonPersonen()
        resultat.daten = list(filter(lambda x : x.wettbewerbsleiter == "ja" ,daten.daten))
        return resultat 

    def saaldiener(daten):
        resultat = ListeVonPersonen()
        resultat.daten = list(filter(lambda x : x.saaldiener == "ja" ,daten.daten))
        return resultat 

    def selectPersons(anzahl,daten):
        personen = ListeVonPersonen() 
        for x in range(anzahl):
            r = random.randint(0,len(daten.daten)-1)
            person = daten.daten[r]
            personen.addPerson(person)
            daten.daten.pop(r)
        return (daten,personen)

    def print(value,daten):
        for person in daten.daten:
           print(value + ": "+person.vorname + " " + person.nachname + " : Mag Aufgabe übernehmen:" + person.magAufgabe + " ist seit mehr als 6 Monaten dabei:" + person.sixMonth + " level 1 und 2 :" + person.Level1Und2 + ", DE :" + person.spracheDe + ", EN :" + person.spracheEn)
  
 

class CSVReader():
    
# opening the CSV file
    def openFile(self): 
        self.listeVonPersonen = ListeVonPersonen()
        with open('./wettbewerbe/data.csv', mode ='r') as file:
            # reading the CSV file
            csvFile = csv.reader(file)
            # displaying the contents of the CSV file
            for lines in csvFile:
                #print(lines)
                #print(lines[16])
                person = AngemeldetePerson(lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6],lines[7],lines[8],lines[9],lines[10],lines[11],lines[12],lines[13],lines[14],lines[15])
                self.listeVonPersonen.addPerson(person)
                #self.data.append(person)
        return self #self.listeVonPersonen

    

print("start ") 

liste = CSVReader().openFile().listeVonPersonen

magAufgabe = ListeVonPersonen.magAufgabe(liste)

ListeVonPersonen.print("mag aufgaben:", magAufgabe)

#v = liste.spracheDE(liste.istSeitMehrAlsSechsMonatenDabei(liste.level1Und2(liste.magAufgabe(liste.daten))))

saaldiener = ListeVonPersonen.saaldiener(magAufgabe)
leiter = ListeVonPersonen.wettbewerbsleiter(magAufgabe)
zeitnehmer = ListeVonPersonen.counter(magAufgabe)
preisrichter = ListeVonPersonen.preisrichter(magAufgabe)

#ListeVonPersonen.print("preisrichter:", preisrichter)
#ListeVonPersonen.print("zeitnehmer:", zeitnehmer)
#ListeVonPersonen.print("saaldiener:", saaldiener)
#ListeVonPersonen.print("leiter:", leiter)

datentupel  = ListeVonPersonen.selectPersons(6,preisrichter)

ListeVonPersonen.print("Preisrichter: " , datentupel[1])
#ListeVonPersonen.print("->" , daten[0])

ListeVonPersonen.print("Moderator: " , ListeVonPersonen.selectPersons(1,ListeVonPersonen.moderator(datentupel[0]))[1])
