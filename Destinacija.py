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