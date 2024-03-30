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
    
    def stringIstorije(self):
        return ','.join([str(x) for x in self.getIstorijaPutovanja()])
    
    def stringPreferenci(self):
        return ','.join([str(x) for x in self.getPreference()])
    
    def sacuvajUFajl(self, file, lines, ind):
        ist = []
        pref = []
        if self.getIstorijaPutovanja() != None:
            ist = self.stringIstorije()
        if self.getPreference() != None:
            pref = self.stringPreferenci()
        #pl = self._placanje._brojRacuna + "," + self._placanje._brojRacuna. + "," + self._placanje._stanje
        info = []
        if self.getUsername() != None: 
            info.append(self.getUsername() + '\n')
        else:
            info.append('\n')

        if self.getLozinka() != None: 
            info.append(self.getLozinka() + '\n')
        else:
            info.append('\n')

        if self.getMail() != None: 
            info.append(self.getMail() + '\n')
        else:
            info.append('\n')

        if ist != [] and ist != None:
            info.append(ist + '\n')
        else:
            info.append('\n')

        if pref != [] and pref != None:
            info.append(pref + '\n')
        else:
            info.append('\n')

        if self.getKontakt() != None: 
            info.append(self.getKontakt() + '\n')
        else:
            info.append('\n')

        lines[(6 * ind):(6 * ind + 5)] = info
        file.writelines(lines)

    def signup(self, sgnup, file, lines):
        print("signup")
        for i in range(len(lines) // 6):
            info = lines[(6 * i):(6 * i + 5)]
            ok = True
            for j in range(len(sgnup)):
                if str(info[j]) != str(sgnup[j]):
                    ok = False
                    break
            if ok:
                return True
            
        self.setUsername(sgnup[0])
        self.setLozinka(sgnup[1])
        self.setMail(sgnup[2])
        self.sacuvajUFajl(file, lines, len(lines) // 6 + 1)
        self.logout()
        return False

    def login(self, lgin, lines):
        print("login")
        for i in range(len(lines) // 6):
            info = lines[(6 * i):(6 * i + 6)]
            print(info)
            print(lgin)
            ok = True
            for j in range(len(lgin)):
                if str(info[j]) != str(lgin[j]):
                    ok = False
                    break
            if ok:
                print("ok")
                self.setUsername(info[0])
                self.setLozinka(info[1])
                self.setMail(info[2])
                if info[3] != '\n':
                    self.setIstorijaPutovanja(info[3])
                if info[4] != '\n':
                    self.setPreference(info[4])
                if info[5] != '\n':
                    self.setKontakt(info[5])
                return True
        return False

    def logout(self):
        self._username = None
        self._lozinka = None
        self._mail = None
        self._istorijaPutovanja = None
        self._preference = None
        self._kontakt = None
        self._placanje = None