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