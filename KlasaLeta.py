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