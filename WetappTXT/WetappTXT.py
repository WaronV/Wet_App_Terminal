import random 
import datetime
import re
import sys

class Dog():
    def __init__ (self,opiekunImie=" ",opiekunNazwisko=" ",opiekunPesel=[0], numer=0, nazwa=" ", rasa=" ", wiek=0):
        self.opiekunImie=opiekunImie
        self.opiekunNazwisko=opiekunNazwisko
        self.opiekunPesel=opiekunPesel
        self.numer=numer
        self.nazwa=nazwa
        self.rasa=rasa
        self.wiek=wiek

    def dodaj(self):

        self.opiekunImie=input("Podaj imie opiekuna: ").lower()
        self.opiekunNazwisko=input("Podaj nazwisko opiekuna: ").lower()
        self.opiekunPesel=sprawdzPesel()
        self.numer=losujNumer()
        with open("DogsNumbers.txt", "a") as plik:
            plik.writelines("\n"+self.numer)
        self.nazwa=input("Podaj nazwe psa: ").lower()
        self.rasa=input("Podaj rase psa: ").lower()
        self.wiek=input("Podaj wiek psa: ")
        self.dataDodania=datetime.date.today()

    def __str__ (self):
        return "Imie opiekuna:"+self.opiekunImie+"\nNazwisko opiekuna:"+self.opiekunNazwisko+"\nPesel opiekuna:"+self.opiekunPesel+"\nNumer psa:"+self.numer+"\nNazwa psa:"+self.nazwa+"\nRasa psa:"+self.rasa+"\nWiek psa:"+self.wiek+"\nData dodana:"+str(self.dataDodania)+"\n/\n"
    def wczytajPsy(self):
        tab=[]
        tabc=[]
        y=""
        with open("BazaDanych.txt", "r") as plik:
            while True:
                x=plik.read(1)
                if x==":":
                    while True:
                        x=plik.read(1)
                        if x=="\n":
                            break
                        y=y+x
                    tab.append(y)
                    y=""
                if x=="":
                    break
        tabc.append(self.__init__(tab[0],tab[1],tab[2],tab[3],tab[4],tab[5],tab[6]))
        print(tab)
        print(tabc)
        del tab, y
        return tabc

def info(z,plik=0):
    with open("BazaDanych.txt", "r") as plik:
        for numberline, k in enumerate(plik):
            if numberline>(z[0]-4) and numberline<(z[0]+4):
                k=k.replace("\n","")
                print(k)

def sprawdzPesel():
    tab=[]
    with open("BazaDanych.txt", "r") as plik:
        tab=[k.replace("Pesel opiekuna: ", "").replace("\n","") for k in plik if re.match("Pesel", k)]

    while True:
        m=0
        n=input("Podaj pesel opiekuna: ")
        if len(n) != 11:
            print("niewłasciwy pesel ")
            continue
        for x in list(n):
            try:
                x=int(x)
                m=m+1
            except ValueError: 
                break

        if m==11 and n not in tab:
            del m, tab
            return n
        else: 
            print("niewłasciwy pesel ")

def losujNumer():  
    while True:
        plik=open('DogsNumbers.txt','r')
        tab2=[]
        for i in range(0,6):
            tab2.append(random.randint(0,9))
        tab2="".join([str(elm) for elm in tab2])
        if tab2 in plik.read():
            continue
        plik.close()
        break
    return tab2

def dodajPsa():
    #zmienna=Dog()
    zmienna.dodaj()
    with open("BazaDanych.txt", "a") as plik:
        plik.writelines(zmienna.__str__())

def szukajPsa(func):
    while True:
        z=input("Podaj numer psa")
        with open("BazaDanych.txt", "r") as plik:
            numberline=[numberline for numberline, k in enumerate(plik) if re.search(z,k)]
        func(numberline)
    del numberline, z

def przegladajPsy():
    with open("BazaDanych.txt", "r") as plik:
        for x in plik:
            x=plik.read()
            print(x)

def usunPsa(z):
    line=[]
    with open("BazaDanych.txt", "r") as plik:
        line=plik.readlines()
    with open("BazaDanych.txt", "w") as plik:
        for numberline, lines in enumerate(line):
            print(numberline)
            if numberline<(z[0]-4) or numberline>(z[0]+4):
                plik.write(lines)
    del line

def editPsa(z):
    print("\nCo chcesz nadpisac? \n1) Imie opiekuna \n2) Nazwisko opiekuna \n3) Pesel opiekuna \n4) Numer psa \n5) Nazwa psa\n6) Rasa psa\n7) Wiek psa\n" )
    x=input()
    if x=="1":
        print("x")
    elif x=="2":
        print("x")
    elif x=="3":
        print("x")
    elif x=="4":
        print("x")
    elif x=="5":
        print("x")
    elif x=="6":
        print("x")
    elif x=="7":
        print("x")
    else:
        print("nieprawidlowa komenda")

def funcexit():
    while True:
        x=input("a) zapisz \nb) niezapisuj \nc) anuluj \n").lower()
        if x=="a":
            print("x")
        elif x=="b":
            sys.exit(0)
        elif x=="c":
            break
        else:
            print("nieprawidlowa komenda")


#--------------------------------------------menu glowne--------------------------------------------
tab=[]

zmienna=Dog()
tab=zmienna.wczytajPsy()
while True: #menu glowne
    x=input("\nCo chcesz zrobic? \na) Dodaj psa \nb) Przegladaj psa \nc) Szukaj psa \nd) edytuj psa \ne) usun psa\nx) zamknij program\n").lower()
    if x=="a":
        dodajPsa()
    elif x=="b":
        przegladajPsy()
    elif x=="c":
        szukajPsa(info)
    elif x=="d":
        szukajPsa(editPsa)
    elif x=="e":
        szukajPsa(usunPsa)
    elif x=="x":
        funcexit()
    else:
        print("nieprawidlowa komenda")

#-----------------------------------------------------------------------------------------------------
