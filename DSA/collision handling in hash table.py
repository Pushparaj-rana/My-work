class hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
        
    def __getitem__ (self,key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
                
    def __setitem__ (self,key,value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
        if not found:
            self.arr[h].append((key,value))
            
    def __delitem__ (self,key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                print ("del", index)
                del self.arr[h][index]


if __name__ == '__main__':
    t = hashtable()
    t.__setitem__("march 6",23)
    t.__setitem__("march 7", 345)
    t.__setitem__("march 8", 324)
    t.__setitem__("march 17", 77)
    print(t.__getitem__("march 6"))
    print(t.arr)
    t.__setitem__("march 6", 3)
    print(t.__getitem__("march 6"))
    print(t.arr)
    t.__delitem__("march 6")
    print(t.arr)
    print(t.__getitem__("march 6"))