from Modeli import *
import pytest

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
"""
for child in aviokompanija.getLetovi().children:
    print(child.value)
    for child2 in child.children:
        print(child2.value)
"""

@pytest.mark.parametrize("test_input,expected", [(["London", "04.04.2024", "19:30", "Madrid", "04.04.2024", "22:00"], True), (["Beograd", "04.07.2024", "12:15", "Moskva", "06.07.2024", "03:00"], True), (["Kanbera", "12.05.2024", "17:00", "Sidni", "12.05.2024", "17:55"], True)])
def test_eval(test_input, expected):
    assert korisnik.dajArgumente(test_input, aviokompanija) == expected