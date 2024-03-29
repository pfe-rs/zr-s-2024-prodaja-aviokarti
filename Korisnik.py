class Korisnik:
    def __init__(self):
        self._username = None
        self._lozinka = None
        self._mail = None
        self._istorijaPutovanja = None
        self._preference = None
        self._kontakt = None
        self._placanje = None
        self.rezervisaneKarte = []

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
    
    def setIstorijaPutovanja(self, novo):
        self._istorijaPutovanja.append(novo)

    def getPreference(self):
        return self._preference
    
    def setPreference(self, preference):
        self._preference = preference

    def getKontakt(self):
        return self._kontakt
    
    def setKontakt(self, kontakt):
        self._kontakt = kontakt

    def getNacinPlacanja(self):
        return self._placanje
    
    def setNacinPlacanja(self, placanje):
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
    
    def getRezervisaneKarte(self):
        return self._rezervisaneKarte
    
    def setRezervisaneKarte(self, novo):
        self._rezervisaneKarte.append(novo)

    def logout(self):
        self._username = None
        self._lozinka = None
        self._mail = None
        self._istorijaPutovanja = None
        self._preference = None
        self._kontakt = None
        self._kartica = None
    
    def kupiKartu(self, sediste, klasaLeta):
        sediste.setDostupnost(False)
        self.get
        for x in klasaLeta.getSedista():
            if x.getId() == sediste.getId():
                klasaLeta.getSedista().remove(x)


    def birajSediste(self, sediste):
        return sediste.getDostupnost()
    
    def otkaziLet(self, let):
        for x in self.getRezervisaneKarte():
            if (x.getPolazak().getDatum(), x.getPolazak().getVreme(), x.getPolazak().getDatum(), x.getDolazak().getDatum(), x.getDolazak().getVreme(), x.getDolazak().getDatum()) == (let.getPolazak().getDatum(), let.getPolazak().getVreme(), let.getPolazak().getDatum(), let.getDolazak().getDatum(), let.getDolazak().getVreme(), let.getDolazak().getDatum()):
                Korisnik.getRezervisaneKarte().remove(x)

    def rezervisiKartu(self, let, klasa, sediste):
        self.setRezervisaneKarte([let, klasa, sediste])

    def izmenaRezervacije(self, i, let, arg):
        pass
        '''
        if arg == "let":
            self.setRezervisaneKarte()[i] = let
        elif arg == "sediste":
            self.getRezervisaneKarte()
        elif arg'''