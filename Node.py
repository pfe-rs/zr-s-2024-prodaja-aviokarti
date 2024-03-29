class Node:
    def __init__(self, value, depth):
        self._value = value
        self._depth = depth
        self._children = []
    
    def getChildren(self):
        return self._children
    
    def getDepth(self):
        return self._depth
    
    def getValue(self):
        return self._value
    
    def setValue(self, value):
        self._value = value

    def addChild(self, child_node):
        self.getChildren().append(child_node) 

    def removeChild(self, child_node):
        self.setChildren([child for child in self.getChildren() 
                        if child is not child_node]) 
        
    def dfs_search(self, target):
        #print(self.depth, self.value, target[self.depth])
        if self is None:
            return False

        if self.getDepth() == 5 and self.getValue() == target[self.getDepth()]:
            return True

        for child in self.getChildren():
            #print(child.value, child.children)
            if child.getValue() == target[self.getDepth() + 1]:
                if child.dfs_search(target):
                    return True