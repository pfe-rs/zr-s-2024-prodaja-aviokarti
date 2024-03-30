class Let:
    def __init__(self, brojPutnika, trajanje, klase, polazak, dolazak):
        self._brojPutnika = brojPutnika
        self._trajanje = trajanje
        self._klase = klase
        self._polazak = polazak
        self._dolazak = dolazak

    def __str__(self):
        return str(self.getPolazak()) + ',' + str(self.getDolazak())

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