from enum import Enum
from pickletools import read_uint1
import unittest
import csv

import csv
import random


# Daten aus der Datei MembershipList-District95-20220219.csv

class Mitgliederdaten:
    def __init__(self):
        self.vorname = ""
        self.nachname = ""
        self.mittelname = ""
        self.clubnummer = ""
        self.clubname = ""
        self.mitgliedernummer = ""
        self.email = ""
        self.mobiltelnr = ""
        self.festnetznr = ""
        self.adresse = ""
        self.district = ""
        self.division = ""
        self.area = ""
        self.activeClub = True 
        self.paidmember = True
    def printMitglied(self):
        print("Mitglied " + self.name() + " (Mitgliedsnr. " + self.mitgliedernummer + ")" + " Klub: "+self.clubname + " (Klubnr. " + self.clubnummer + ")") 

    def name(self):
        if len(self.mittelname)==0:
            return self.vorname + " " + self.nachname
        else:
            return self.vorname + " " + self.mittelname + " " + self.nachname


class MitgliederListe:

    def __init__(self):
        self.datenByNumber = {}
        self.datenByPerson = {}
        self.datenByClub = {}
        self.klubs = {}

    def addMember(self,person):
        self.klubs[person.clubnummer] = person.clubname
        self.datenByNumber[person.mitgliedernummer] = person
        self.datenByPerson[person.vorname + " " + person.nachname] = person.mitgliedernummer
        if person.mitgliedernummer in self.datenByClub: 
            klubdaten = self.datenByClub[person.mitgliedernummer]
            klubdaten.append(person.clubnummer)
            print("Dopplung:")
            person.printMitglied()
            self.datenByClub[person.mitgliedernummer] = klubdaten
        else:
            klubdaten = [person.clubnummer]
            self.datenByClub[person.mitgliedernummer] = klubdaten
    
    def printStatistics(self):
        print("Result:")
        print(len(self.datenByNumber))

    def getKlubnameByID(self, klubid):
        return self.klubs[klubid]

    def getMemberIDByName(self,person):
        return self.datenByPerson[person]

    def getMemberByID(self,memberid):
        return self.datenByNumber[memberid]

    def getKlubdatenByMemberID(self,memberid):
        return self.datenByClub[memberid]

    def openFile(self): 
        with open('./MembershipList-District95-20220219.csv', mode ='r') as file:
            # reading the CSV file
            csvFile = csv.reader(file)
            # displaying the contents of the CSV file
            for lines in csvFile:
                print("Lines:")
                print(lines)
                if len(lines) == 0:
                    continue
                member = Mitgliederdaten()
                member.email = lines[29]
                member.vorname = lines[14]
                member.mittelname = lines[15]
                member.nachname = lines[13]
                member.clubnummer = lines[4]
                member.clubname = lines[5]
                member.mitgliedernummer = lines[11]
                member.email = lines[29]
                member.mobiltelnr = lines[26]
                member.festnetznr = lines[24]
                member.adresse = lines[17] + "," + lines[18] + lines[20] + "," + lines[19] + " " + lines[21] + "," + lines[22]
                member.district = lines[1]
                member.division = lines[2]
                member.area = lines[3]
                member.activeClub = lines[6] 
                member.paidmember = lines[12] 
                member.awards = lines[16]
                self.addMember(member)
            self.printStatistics()


     


# Daten aus der eventbrite - CSV Datei  . Nicht alle spalten werden benötigt

# 0: Bestellnr.	
# 1: Bestelldatum	
# 2: Vorname	
# 3: Nachname	
# 4: E-Mail	
# 5: Anzahl	
# 6: Ticketart	
# 7: Bestellungstyp	
# 8: Gesamtzahlungsbetrag	
# 9: Eventbrite-Gebühren	
# 10: Eventbrite-Zahlungsabwicklung	
# 11: Teilnehmerstatus	
# 12: Mobiltelefon	
# 13: What's your member number? / Wie lautet deine Mitgliedsnummer?	
# 14: Have you been a Toastmaster for more than 6 months? / Bist du seit mehr als 6 Monaten Toastmaster?	
# 15: What's your club number? / Wie lautet deine Clubnummer?	
# 16: What's your club name? / Wie lautet der Name deines Clubs?	
# 17: Which language(s) do you speak? / Welche Sprache(n) sprichst du?	
# 18: Would you like to support us during the contests (e.g. by taking a role)? / Würdest du uns während der Wettbewerbe unterstützen wollen (z.B. durch Übernahme einer Rolle)?	
# 19: Which roles/tasks would you take? / Welche Rollen/Aufgaben würdest du übernehmen?	
# 20: Have you completed levels 1 and 2 of any pathway in Pathways OR 6 projects from the Competent Communication Handbook? / Hast du die Stufen 1 und 2 eines beliebigen Pfads in Pathways ODER 6 Projekte aus dem Handbuch Kompetente Kommunikation abgeschlossen?	
# 21: Which country do you come from? / Aus welchem Land kommst du?	
# 22: please specify / bitte spezifizieren	
# 23: Lieferadresse	
# 24 Adresszusatz	
# 25: Ort Lieferadresse	
# 26: Bundesland Lieferadresse	
# 27: Postleitzahl Lieferadresse	
# 28: Land Lieferadresse	
# 29

class Answer(Enum):
    YES=0
    NO=1
    UNKNOWN=2

class Antwort:
    def __init__(self,name1,name2,value):
        self.nameenglish = name1
        self.namedeutsch = name2
        self.value = value 

    def Yes():
        return Antwort("Yes","Ja",Answer.YES)
        
    def No():
        return Antwort("No","Nein",Answer.YES)

    def Unknown():
        return Antwort("","",Answer.UNKNOWN)
        
    @staticmethod
    def whatAnswer(value):
        if type(value)==None:
            return Antwort.Unknown()
        if value.__contains__(Antwort.No().nameenglish) or value.__contains__(Antwort.No().namedeutsch):
            return Antwort.No() 
        if value.__contains__(Antwort.Yes().nameenglish) or value.__contains__(Antwort.Yes().namedeutsch):
            return Antwort.Yes()
        return Antwort.Unknown()
    

        



    

class Role(Enum):
    BALLOTCOUNTER = 1
    TIMER = 2
    SEARGANT = 3
    TECHSUPPORT = 4
    PRESENTER = 5
    OTHER = 6
    VOTINGJUDGE = 7
    TIEBREAKINGJUDGE = 8 
    CONTESTCHAIR = 9
    CHIEFJUDGE = 10 

class Language(Enum):
    DEUTSCH = 0
    ENGLISH = 1
    SWEDISH = 2
    NONE = 3

class Sprache:
    def __init__(self):
        self.name = ""
        self.lang = Language.NONE
    
    @staticmethod
    def english():
        lng = Sprache()
        lng.name="EN"
        lng.lang = Language.ENGLISH
    def deutsch():
        lng = Sprache()
        lng.name="DE"
        lng.lang = Language.DEUTSCH


class Rolle: 
    def __init__(self):
        self.german = ""
        self.english = ""
        self.role = Role.OTHER

    @staticmethod 
    def roleBallotCounter():
        bc = Rolle()
        bc.german = "Stimmenzähler"
        bc.english = "Ballot Counter"
        bc.role = Role.BALLOTCOUNTER
        return bc 
    @staticmethod 
    def roleTimer():
        bc = Rolle()
        bc.german = "Zeitnehmer"
        bc.english = "Timer"
        bc.role = Role.TIMER
        return bc 

    @staticmethod 
    def roleSeargantAtArms():
        bc = Rolle()
        bc.german = "Saalmeister"
        bc.english = "Sergeant at Arms"
        bc.role = Role.SEARGANT
        return bc 

    @staticmethod 
    def rolePresenter():
        bc = Rolle()
        bc.german = "Moderator"
        bc.english = "Presenter"
        bc.role = Role.PRESENTER
        return bc 

    @staticmethod 
    def roleTechnicalSupport():
        bc = Rolle()
        bc.german = "Technischer Support"
        bc.english = "Technical Support"
        bc.role = Role.TECHSUPPORT
        return bc 
    
    @staticmethod 
    def roleOther():
        bc = Rolle()
        bc.german = "Sonstige"
        bc.english = "Other"
        bc.role = Role.OTHER
        return bc 

    @staticmethod 
    def roleVotingJudge():
        bc = Rolle()
        bc.german = "Punktrichter"
        bc.english = "Voting Judge"
        bc.role = Role.VOTINGJUDGE
        return bc 

    @staticmethod 
    def roleTieBreakingJudge():
        bc = Rolle()
        bc.english = "Tie-breaking Judge"
        bc.german = "Gleichstandsrichter"
        bc.role = Role.TIEBREAKINGJUDGE
        return bc 

    @staticmethod 
    def roleContestChair():
        bc = Rolle()
        bc.german = "Wettbewerbsvorsitzender"
        bc.english = "Contest Chair"
        bc.role = Role.CONTESTCHAIR
        return bc 

    @staticmethod 
    def roleChiefJudge():
        bc = Rolle()
        bc.german = "Hauptrichter"
        bc.english = "Chief Judge"
        bc.role = Role.CHIEFJUDGE
        return bc 
    
    @staticmethod
    def identifyRulesByString(value):
        data = []
        rollen = [Rolle.roleBallotCounter(),Rolle.roleChiefJudge(),Rolle.roleContestChair(),Rolle.roleOther(),Rolle.rolePresenter(),Rolle.roleSeargantAtArms(),Rolle.roleTechnicalSupport(),Rolle.roleTieBreakingJudge(),Rolle.roleTimer(),Rolle.roleVotingJudge()]
        for rule in rollen: 
            if (value.__contains__(rule.german) or value.__contains__(rule.english)):
                data.append(rule)
        return data
        
    
    



class AngemeldetePersonEventbrite: 
    def hatAufgaben(self):
        if type(self.rollen) == None:
            return False
        return len(self.rollen)>0
    
    def __init__(self):
        self.bestellnummer = 0   # 0 
        self.bestelldatum = 0    # 1
        self.vorname = ""        # 2
        self.nachname = ""       # 3
        self.email = ""          # 4
        self.mobiltelefon = ""   # 12 
        self.mitgliedsnummer = ""   # 13 
        self.sixMonth = True  # 14 
        self.clubnummer = ""      # 15
        self.clubname = ""        # 16 
        self.sprachen = []  #17 
        self.rollen = []
        self.level1And2Competed = True  # 20
        self.countryOrigin = "" # 21 

    
    def language(value):
        data = []
        languages = [Sprache.deutsch(),Sprache.english()]
        for lang in languages:
            if value.__contains__(lang.name):
                data.append(lang.lang)
        return languages 

class ListeVonAngemeldetenPersonenEventbrite:
    def __init__(self):
        self.daten = []

    def addPerson(self,person):
        self.daten.append(person)

    #    def filter(name, daten):
    #        resultat = ListeVonAngemeldetenPersonenEventbrite()
    #        resultat.daten = list(filter(lambda x : getattr(x,name) == "ja" ,daten.daten))
    #        return resultat 
    
    @staticmethod
    def filterRolle(rolle,daten): 
        resultat = ListeVonAngemeldetenPersonenEventbrite()
        resultat.daten = list(filter(lambda x : (rolle in x.rollen == True), daten.daten))
        return resultat 

    @staticmethod
    def magAufgabe(daten):
        resultat = ListeVonAngemeldetenPersonenEventbrite()
        resultat.daten = list(filter(lambda x : len(x.rollen)>0, daten.daten))
        return resultat 

    @staticmethod
    def istSeitMehrAlsSechsMonatenDabei(daten):
        resultat = ListeVonAngemeldetenPersonenEventbrite()
        resultat.daten = list(filter(lambda x : x.sixMonth==True, daten.daten))
        return resultat 

    @staticmethod
    def level1Und2(daten):
        resultat = ListeVonAngemeldetenPersonenEventbrite()
        resultat.daten = list(filter(lambda x : x.level1And2Completed==True, daten.daten))
        return resultat

    @staticmethod
    def sprache(sprache, daten):
        resultat = ListeVonAngemeldetenPersonenEventbrite()
        resultat.daten = list(filter(lambda x : (sprache in x.sprachen), daten.daten))
        return resultat

    def selectPersons(anzahl,daten):
        personen = ListeVonAngemeldetenPersonenEventbrite() 
        for x in range(anzahl):
            r = random.randint(0,len(daten.daten)-1)
            person = daten.daten[r]
            personen.addPerson(person)
            daten.daten.pop(r)
        return (daten,personen)

    def print(self):
        for person in self.daten:
            sixMonth = "Nein"
            if (person.sixMonth==True):
                sixMonth="Ja"
            Level1Und2 = "Nein"
            if (person.level1And2Competed==True):
                Level1Und2="Ja"
            hatAufgaben = "Nein"
            if (person.hatAufgaben()==True):
                hatAufgaben="Ja"
            value = ""
            value1 = ""
            for rolle in person.rollen:
                value =  value + value1 + rolle.german + " / " + rolle.english
                if value1 == "":
                    value1 = ","
            print(person.vorname + " " + person.nachname + " : Mag Aufgabe übernehmen:" + hatAufgaben  + " ist seit mehr als 6 Monaten dabei:" + sixMonth + " level 1 und 2 :" + Level1Und2 + " Rollen:" + value)
             
 

class CSVReader():
    
# opening the CSV file
    def openFile(self): 
        self.listeVonPersonen = ListeVonAngemeldetenPersonenEventbrite()
        with open('./eventbrite-report.csv', mode ='r') as file:
            # reading the CSV file
            csvFile = csv.reader(file)
            # displaying the contents of the CSV file
            for lines in csvFile:
                if  (type(lines) == None)==False:
                    if len(lines) == 0:
                        continue
                person = AngemeldetePersonEventbrite()
                person.bestellnummer = lines[0]
                person.bestelldatum = lines[1]
                person.vorname = lines[2]
                person.nachname = lines[3]
                person.email =  lines[3]
                person.mobiltelefon = lines[12]  # 12 
                person.mitgliedsnummer =lines[13]   # 13 
                print(Antwort.No())
                person.sixMonth = Antwort.whatAnswer(lines[14])
                if lines[14].__contains__("Yes")==True or  lines[14].__contains__("Ja")==True:
                    person.sixMonth=True
                person.clubnummer = lines[15]    # 15
                person.clubname = lines[16]        # 16 
                person.sprachen = lines[17] ##["de","en"]  #17 
                person.rollen = Rolle.identifyRulesByString(lines[19])
                person.level1And2Competed=False
                if lines[20].__contains__("Yes")==True or  lines[20].__contains__("Ja")==True:
                    person.level1And2Competed = True  # 20
                person.countryOrigin = lines[21]  # 21 
                self.listeVonPersonen.addPerson(person)
                #self.data.append(person)
        return self #self.listeVonPersonen

    

print("start ") 

member = MitgliederListe()
member.openFile()
mitglied = member.getMemberByID(member.getMemberIDByName("Christian Baars"))
mitglied.printMitglied()
daten = member.getKlubdatenByMemberID("07835234")
for klubnummer in daten:
    print(member.getKlubnameByID(klubnummer))
print(daten)
print("done")

#liste = CSVReader().openFile().listeVonPersonen
#liste.print()
#

#magAufgabe = ListeVonAngemeldetenPersonenEventbrite.magAufgabe(liste)

#ListeVonAngemeldetenPersonenEventbrite.pri nt("mag aufgaben:", magAufgabe)

#v = liste.spracheDE(liste.istSeitMehrAlsSechsMonatenDabei(liste.level1Und2(liste.magAufgabe(liste.daten))))

#saaldiener = ListeVonAngemeldetenPersonenEventbrite.saaldiener(magAufgabe)
#leiter = ListeVonAngemeldetenPersonenEventbrite.wettbewerbsleiter(magAufgabe)
#zeitnehmer = ListeVonAngemeldetenPersonenEventbrite.counter(magAufgabe)
#preisrichter = ListeVonAngemeldetenPersonenEventbrite.preisrichter(magAufgabe)

#ListeVonPersonen.print("preisrichter:", preisrichter)
#ListeVonPersonen.print("zeitnehmer:", zeitnehmer)
#ListeVonPersonen.print("saaldiener:", saaldiener)
#ListeVonPersonen.print("leiter:", leiter)

#datentupel  = ListeVonAngemeldetenPersonenEventbrite.selectPersons(6,preisrichter)

#ListeVonAngemeldetenPersonenEventbrite.print("Preisrichter: " , datentupel[1])
#ListeVonPersonen.print("->" , daten[0])

#ListeVonAngemeldetenPersonenEventbrite.print("Moderator: " , ListeVonAngemeldetenPersonenEventbrite.selectPersons(1,ListeVonAngemeldetenPersonenEventbrite.moderator(datentupel[0]))[1])
