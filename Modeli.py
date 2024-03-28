class Node:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node) 

    def remove_child(self, child_node):
        self.children = [child for child in self.children 
                        if child is not child_node]
        
    def dfs_search(self, target):
        if self is None:
            return False

        if self.depth == 5 and self.value == target[self.depth]:
            return True

        for child in self.children:
            #print(child.value, child.children)
            if child.value == target[self.depth + 1]:
                if child.dfs_search(target):
                    return True

class Destinacija:
    def __init__(self, vreme, datum, mesto, polazakDolazak):
        self._vreme = vreme
        self._datum = datum
        self._mesto = mesto
        self._polazakDolazak = polazakDolazak

    def getVreme(self):
        return self._vreme
    
    def getDatum(self):
        return self._datum
    
    def getMesto(self):
        return self._mesto
    
    def getPolazakDolazak(self):
        return self._polazakDolazak

class Sediste:
    def __init__(self, id, dostupnost):
        self._id = id
        self._dostupnost = dostupnost
    
    def getId(self):
        return self._id
    
    def getDostupnost(self):
        return self._dostupnost
    
    def setDostupnost(self, dostupnost):
        self._dostupnost = dostupnost

class KlasaLeta:
    def __init__(self, id, sedista, cena):
        self._id = id
        self._sedista = sedista
        self._cena = cena

    def getId(self):
        return self._id

    def getSedista(self):
        return self._sedista
    
    def getCena(self):
        return self._cena
    
    def proveriZauzetost(self):
        if len(self._sedista) == 0:
            return True
        return False

class Let:
    def __init__(self, brojPutnika, trajanje, klase, polazak, dolazak):
        self._brojPutnika = brojPutnika
        self._trajanje = trajanje
        self._klase = klase
        self._polazak = polazak
        self._dolazak = dolazak

    def getBrojPutnika(self):
        return self._brojPutnika
    
    def getTrajanje(self):
        return self._trajanje
    
    def getKlase(self):
        return self._klase
    
    def getPolazak(self):
        return self._polazak
    
    def getDolazak(self):
        return self._dolazak
    
class Aviokompanija:
    def __init__(self):
        self._letovi = Node(-1, -1)

    def getLetovi(self):
        return self._letovi
    
    def traziLet(self, atributi):
        return self.getLetovi().dfs_search(atributi)
    
    def dodajLet(self, let):
        tr_node = self.getLetovi()
        polazak = let.getPolazak()
        dolazak = let.getDolazak()
        destinacije = [polazak.getMesto(), polazak.getDatum(), polazak.getVreme(), dolazak.getMesto(), dolazak.getDatum(), dolazak.getVreme()]
        for i in range(6):
            for child in tr_node.children:
                #print("Dodavanje")
                #print(tr_node.value)
                #print(destinacije[i], child.value)
                #for child2 in child.children:
                #    print(child2.value)
                if destinacije[i] == child.value:
                    print("desilo se")
                    tr_node = child
                    break
            tr_node.add_child(Node(destinacije[i], i))
            tr_node = tr_node.children[-1]

class Korisnik:
    def __init__(self):
        self._username = None
        self._lozinka = None
        self._mail = None
        self._istorijaPutovanja = None
        self._preference = None
        self._kontakt = None
        self._kartica = None

    def getUsername(self):
        return self._username
    
    def setUsername(self, username):
        self._username = username

    def getLozinka(self):
        return self._lozinka
    
    def setLozinka(self, lozinka):
        self._lozinka = lozinka 

    def getMail(self):
        return self._mail
    
    def setMail(self, mail):
        self._mail = mail

    def getIstorijaPutovanja(self):
        return self._istorijaPutovanja
    
    def setIstorijaPutovanja(self, istorijaPutovanja):
        self._istorijaPutovanja = istorijaPutovanja

    def getPreference(self):
        return self._preference
    
    def setPreference(self, preference):
        self._preference = preference

    def getKontakt(self):
        return self._kontakt
    
    def setKontakt(self, kontakt):
        self._kontakt = kontakt

    def getKartica(self):
        return self._kartica
    
    def setKartica(self, kartica):
        self._kartica = kartica

    def dajArgumente(self, atributi, aviokompanija):
        return aviokompanija.traziLet(atributi)

    def login(self):
        pass

    def logout(self):
        self._username = None
        self._lozinka = None
        self._mail = None
        self._istorijaPutovanja = None
        self._preference = None
        self._kontakt = None
        self._kartica = None


    def kupiKartu(self, sediste, klasaLeta):
        sediste.setDostupnost(False)
        for x in klasaLeta.getSedista():
            if x.getId() == sediste.getId():
                klasaLeta.getSedista().remove(x)




KlasaEkonomska = KlasaLeta(0, [Sediste(0, 1), Sediste(1, 1)], 500) # 0 - ekonomska
KlasaBiznis = KlasaLeta(1, [Sediste(0, 1), Sediste(1, 1)], 1000) # 1 - biznis
KlasaPrva = KlasaLeta(2, [Sediste(0, 1), Sediste(1, 1)], 2500) # 2 - prva

Polazak = Destinacija("19:30", "04.04.2024", "London", 0) # 0 - polazak
Dolazak = Destinacija("22:00", "04.04.2024", "Madrid", 1) # 1 - dolazak

Let1 = Let(300, 150, [KlasaEkonomska, KlasaBiznis, KlasaPrva], Polazak, Dolazak)



korisnik = Korisnik()
aviokompanija = Aviokompanija()
#print(aviokompanija._letovi.children[0].value)





a = input("uneti 'preference' da se ooguci podesavanje ili 'let' da bi se pretrazio let: ")
while a not in ['preference', 'let']:
    a = input("uneti 'preference' da se ooguci podesavanje ili 'let' da bi se pretrazio let: ")
if a == "preference":
    korisnik.setPreference(input("uneti preference: ").split())
    a = input("uneti 'let' ukoliko zelite da nastavite kupovinu: ")


if a == "let":

    argumenti = input("uneti redom mesto polaska, datum i vreme potom destinaciju, datim dolaska i vreme sletanja: ").split()    #["London", "04.04.2024", "19:30", "Madrid", "04.04.2024", "22:00"]


    while not korisnik.dajArgumente(argumenti, aviokompanija):
        argumenti = input("NE POSTOJI LET POKUSAJ PONOVO: ").split()    #["London", "04.04.2024", "19:30", "Madrid", "04.04.2024", "22:00"]

    
    klasa = input("uneti 0 za ekonomsku, 1 za biznis, 2 za prvu klasu: ")
    while not klasa in ["1", "2", "0"]:
        klasa = input("uneti 0 za ekonomsku, 1 za biznis, 2 za prvu klasu: ")

    sedista = []

    while True:
        if klasa == "0":
            if not KlasaEkonomska.proveriZauzetost():
                sedista = KlasaEkonomska.getSedista()
                klasa = KlasaEkonomska
                break
            else:
                sedista = []
                print("klasa nije dostupna")
                klasa = input("klasa nije dostupna, uneti 1 ili 2: ")
                break

        elif klasa == "1":
            if not KlasaBiznis.proveriZauzetost():
                sedista = KlasaBiznis.getSedista()
                klasa = KlasaBiznis
                break
            else:
                sedista = []
                print("klasa nije dostupna")
                klasa = input("klasa nije dostupna, uneti 0 ili 2: ")
                break

        elif klasa == "2":
            if not KlasaPrva.proveriZauzetost():
                sedista = KlasaPrva.getSedista()
                klasa = KlasaPrva
                break
            else:
                sedista = []
                print("klasa nije dostupna")
                klasa = input("klasa nije dostupna, uneti 0 ili 1: ")
                break

        print(sedista)

    sediste = Sediste(int(input("uneti redni broj sedista: ")), 1)
    
    while not sediste.getDostupnost():
        sediste = Sediste(int(input("SEDISTE NIJE DOSTUPNO uneti redni broj sedista: ")), 1)

    korisnik.kupiKartu(sediste, klasa)
    print('CESTITAMO KUPILI STE KARTU')



korisnik.logout()


    



argumenti = ["London", "04.04.2024", "19:30", "Madrid", "04.04.2024", "22:00"]

aviokompanija.dodajLet(Let1)

#print(aviokompanija._letovi.children[0].value)
print(korisnik.dajArgumente(argumenti, aviokompanija))