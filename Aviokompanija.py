from Node import *

class Aviokompanija:
    def __init__(self):
        self._letovi = Node(-1, -1)

    def getLetovi(self):
        return self._letovi
    
    def traziLet(self, atributi):
        return self.getLetovi().dfs_search(atributi)
    
    def dodajLet(self, let):
        tr_node = self.getLetovi()
        polazak = let.getPolazak()
        dolazak = let.getDolazak()
        destinacije = [polazak.getMesto(), polazak.getDatum(), polazak.getVreme(), dolazak.getMesto(), dolazak.getDatum(), dolazak.getVreme()]
        for i in range(6):
            for child in tr_node.getChildren():
                #print("Dodavanje")
                #print(tr_node.value)
                #print(destinacije[i], child.value)
                #for child2 in child.children:
                #    print(child2.value)
                if destinacije[i] == child.getValue():
                    print("desilo se")
                    tr_node = child
                    break
            tr_node.addChild(Node(destinacije[i], i))
            tr_node = tr_node.getChildren()[-1]