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
    def __init__(self, letovi):
        self._letovi = letovi

    def getLetovi(self):
        return self._letovi
    
    #mozda moze efikacnije
    def traziLet(self, atributi):
        return root.dfs_search(atributi)

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

KlasaEkonomska = KlasaLeta(0, [Sediste(0, 1), Sediste(1, 1)], 500) # 0 - ekonomska
KlasaBiznis = KlasaLeta(1, [Sediste(0, 1), Sediste(1, 1)], 1000) # 1 - biznis
KlasaPrva = KlasaLeta(2, [Sediste(0, 1), Sediste(1, 1)], 2500) # 2 - prva

Polazak = Destinacija("19:30", "04.04.2024", "London", 0) # 0 - polazak
Dolazak = Destinacija("22:00", "04.04.2024", "Madrid", 1) # 1 - dolazak

Let1 = Let(300, 150, [KlasaEkonomska, KlasaBiznis, KlasaPrva], Polazak, Dolazak)


root = Node(-1, -1)
tr_node = Node("London", 0)
root.add_child(tr_node)
sledeci_node = Node("04.04.2024", 1)
tr_node.add_child(sledeci_node)
tr_node = sledeci_node
sledeci_node = Node("19:30", 2)
tr_node.add_child(sledeci_node)

tr_node = sledeci_node
sledeci_node = Node("Madrid", 3)
tr_node.add_child(sledeci_node)

tr_node = sledeci_node
sledeci_node = Node("04.04.2024", 4)
tr_node.add_child(sledeci_node)

tr_node = sledeci_node
sledeci_node = Node("22:00", 5)
tr_node.add_child(sledeci_node)

korisnik = Korisnik()

argumenti = ["London", "04.04.2024", "19:30", "Madrid", "04.04.2024", "22:00"]

aviokompanija = Aviokompanija(root)

print(aviokompanija._letovi.children[0].value)
print(korisnik.dajArgumente(argumenti, aviokompanija))



