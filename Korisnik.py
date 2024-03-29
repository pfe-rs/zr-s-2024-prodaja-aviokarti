class Korisnik:
    def __init__(self):
        self._username = None
        self._lozinka = None
        self._mail = None
        self._istorijaPutovanja = None
        self._preference = None
        self._kontakt = None
        self._placanje = None

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

    def getPlacanje(self):
        return self._placanje
    
    def setPlacanje(self, placanje):
        self._placanje = placanje

    def dajArgumente(self, atributi, aviokompanija):
        return aviokompanija.traziLet(atributi)
    
    def signup(self, sgnup, file, lines):
        print("signup")
        for line in lines:
            #print("bbb")
            info = line.split(",")
            ok = True
            for i in range(len(sgnup)):
                if info[i] != sgnup[i]:
                    ok = False
                    break
            if ok:
                return True
        info = ','.join([str(x) for x in sgnup])
        file.write(info + "\n")

        lines.append(info)
        return False

    def login(self, lgin, lines):
        print("login")
        for line in lines:
            info = line.split(",")
            ok = True
            for i in range(len(lgin)):
                if info[i] != lgin[i]:
                    ok = False
                    break
            if ok:            
                self.setUsername(lgin[0])
                self.setLozinka(lgin[1])
                return True
        return False


    def logout(self):
        self._username = None
        self._lozinka = None
        self._mail = None
        self._istorijaPutovanja = None
        self._preference = None
        self._kontakt = None
        self._kartica = None