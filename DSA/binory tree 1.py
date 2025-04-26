class binary_search_treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = binary_search_treenode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binary_search_treenode(data)

    def search (self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def in_order_travelsal(self):
        element = []
        if self.left:
            element += self.left.in_order_travelsal()
        element.append(self.data)
        if self.right:
            element += self.right.in_order_travelsal()

        return element
    
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
            
    def find_maxx(self):
        if self.right :
            return self.right.find_maxx()
        else:
            return self.data
            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)


        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    rootnode = binary_search_treenode(elements[0])

    for i in range(1,len(elements)):
        rootnode.add_child(elements[i])
    return rootnode

if __name__ == '__main__':

    numbers_tree = build_tree([17, 4, 1, 20, 9])
    print(numbers_tree.in_order_travelsal())
    #print(numbers_tree.find_max())
    #print(numbers_tree.find_maxx())
    #print(numbers_tree.find_min())
    numbers_tree.delete(4)
    print(numbers_tree.in_order_travelsal())