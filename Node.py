class Node:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node) 

    def remove_child(self, child_node):
        self.children = [child for child in self.children 
                        if child is not child_node]
        
    def dfs_search(self, target):
        #print(self.depth, self.value, target[self.depth])
        if self is None:
            return False

        if self.depth == 5 and self.value == target[self.depth]:
            return True

        for child in self.children:
            #print(child.value, child.children)
            if child.value == target[self.depth + 1]:
                if child.dfs_search(target):
                    return True