class Placanje:
    def __init__(self, brRac, stanje, nacin):
        self._brojRacuna = brRac
        self._stanje = stanje
        self._nacin = nacin


    def getBrojRacuna(self):
        return self._brojRacuna
    
    def getStanje(self):
        return self._stanje
    
    def getBrojNacin(self):
        return self._nacin
    

    def setBrojRacuna(self, rc):
        self._brojRacuna = rc
    
    def setStanje(self, suma):
        self._stanje = suma
    
    def setBrojNacin(self, nacin):
        self._nacin = nacin

    def plati(self, suma):
        if self._stanje >= suma:
            self._stanje -= suma
        else:
            print("NEMATE DOVOLJNO NOVCA")


    
    
    
