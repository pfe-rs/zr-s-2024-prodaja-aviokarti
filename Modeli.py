from Node import *
from KlasaLeta import *
from Sediste import *
from Destinacija import *
from Let import *
from Korisnik import *
from Aviokompanija import *
from Placanje import *

file = open("Korisnici.txt", "r+")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i][:len(lines[i])-1]


""""
aviokompanija = Aviokompanija()

korisnik = Korisnik()
#korisnik.setUsername("pavleiv")
#korisnik.setLozinka("qwerty")

print(korisnik.signup(['asdf', 'asdf123']))
print(korisnik.login(['asdf', 'asdf123']))
print(korisnik.getUsername(), korisnik.getLozinka())
print(korisnik.login(['pavleiv', 'qwerty123']))   
print(korisnik.getUsername(), korisnik.getLozinka())


    def kupiKartu(self, sediste, klasaLeta):
        sediste.setDostupnost(False)
        self.get
        for x in klasaLeta.getSedista():
            if x.getId() == sediste.getId():
                klasaLeta.getSedista().remove(x)




KlasaEkonomska = KlasaLeta(0, [Sediste(0, 1), Sediste(1, 1)], 500) # 0 - ekonomska
KlasaBiznis = KlasaLeta(1, [Sediste(0, 1), Sediste(1, 1)], 1000) # 1 - biznis
KlasaPrva = KlasaLeta(2, [Sediste(0, 1), Sediste(1, 1)], 2500) # 2 - prva

Polazak = Destinacija("19:30", "04.04.2024", "London", 0) # 0 - polazak
Dolazak = Destinacija("22:00", "04.04.2024", "Madrid", 1) # 1 - dolazak

Let1 = Let(300, 150, [KlasaEkonomska, KlasaBiznis, KlasaPrva], Polazak, Dolazak)

argumenti = ["London", "04.04.2024", "19:30", "Madrid", "04.04.2024", "22:00"]

aviokompanija.dodajLet(Let1)

#print(aviokompanija._letovi.children[0].value)
#print(korisnik.dajArgumente(argumenti, aviokompanija))
"""
file.close()