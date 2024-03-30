from Node import *
from KlasaLeta import *
from Sediste import *
from Destinacija import *
from Let import *
from Korisnik import *
from Aviokompanija import *
import pytest

file = open("Korisnici.txt", "r")
lines = file.readlines()
#print("Linije:")
print(lines)
for i in range(len(lines)):
    #print("hhh")
    lines[i] = lines[i][:len(lines[i])-1]
    #print(lines[i])
file.close()

file = open("Korisnici.txt", "w")

aviokompanija = Aviokompanija()
korisnik = Korisnik()
KlasaEkonomska = KlasaLeta(0, [Sediste(0, 1), Sediste(1, 1)], 500) # 0 - ekonomska
KlasaBiznis = KlasaLeta(1, [Sediste(0, 1), Sediste(1, 1)], 1000) # 1 - biznis
KlasaPrva = KlasaLeta(2, [Sediste(0, 1), Sediste(1, 1)], 2500) # 2 - prva

Polazak1 = Destinacija("19:30", "04.04.2024", "London", 0) # 0 - polazak
Dolazak1 = Destinacija("22:00", "04.04.2024", "Madrid", 1) # 1 - dolazak
Polazak2 = Destinacija("12:15", "04.07.2024", "Beograd", 0) # 0 - polazak
Dolazak2 = Destinacija("03:00", "06.07.2024", "Moskva", 1) # 1 - dolazak
Polazak3 = Destinacija("17:00", "12.05.2024", "Kanbera", 0) # 0 - polazak
Dolazak3 = Destinacija("17:55", "12.05.2024", "Sidni", 1) # 1 - dolazak

Let1 = Let(300, 150, [KlasaEkonomska, KlasaBiznis, KlasaPrva], Polazak1, Dolazak1)
Let2 = Let(300, 150, [KlasaEkonomska, KlasaBiznis, KlasaPrva], Polazak2, Dolazak2)
Let3 = Let(300, 150, [KlasaEkonomska, KlasaBiznis, KlasaPrva], Polazak3, Dolazak3)
aviokompanija.dodajLet(Let1)
aviokompanija.dodajLet(Let2)
aviokompanija.dodajLet(Let3)

argumenti = []
"""
korisnik.setUsername("pavleiv")
korisnik.setLozinka("qwerty123")
korisnik.setMail("pavleivanovic888@gmail.com")
korisnik.setIstorijaPutovanja([str(Let1), str(Let2), str(Let3)])
korisnik.setPreference(["Ekonomska", "Pariz"])
korisnik.setKontakt("065 5190202")
"""

#print([str(Let1), str(Let2), str(Let3)])
argumenti.append("pavleiv")
argumenti.append("qwerty123")
argumenti.append("pavleivanovic888@gmail.com")
#argumenti.append([str(Let1), str(Let2), str(Let3)])
#argumenti.append(["Ekonomska", "Pariz"])
#argumenti.append("065 5190202")

korisnik.signup(argumenti,file, lines)
file.close()
korisnik.login(argumenti[:2], lines)
print(korisnik.getUsername(), korisnik.getLozinka())
@pytest.mark.parametrize("test_input,expected", [(["London", "04.04.2024", "19:30", "Madrid", "04.04.2024", "22:00"], True), (["Beograd", "04.07.2024", "12:15", "Moskva", "06.07.2024", "03:00"], True), (["Kanbera", "12.05.2024", "17:00", "Sidni", "12.05.2024", "17:55"], True)])
def test_eval(test_input, expected):
    assert korisnik.dajArgumente(test_input, aviokompanija) == expected