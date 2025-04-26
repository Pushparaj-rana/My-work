class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linklist:
    def __init__(self,):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr is not None:
            if itr.next:
                llstr = llstr + str(itr.data) + "--->"
            else:
                llstr = llstr + str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self,data):
        node =  Node (data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
    def insert_value(self,data_list):
        #self.head = None
        for data in data_list:
            self.insert_at_end(data)
        
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception ("invalid index")
        
        if index == 0:
            self.head = self.head.next

        count=0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    def insert_after_value(self,data_after,data_to_insert):
        itr =  self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
            itr = itr.next
    def find_by_value(self,data):
        itr = self.head
        while itr:
            if itr.data == data:
                print ("value exist")
                break
            itr = itr.next
        print ("Value does not exist")


        

    

if __name__ == '__main__':
    ll = linklist()
    ll.insert_at_begining(4514)
    ll.insert_at_begining(4511)
    ll.insert_at_begining(453)
    ll.insert_at_begining(45)
    ll.insert_at_end(33)
    ll.get_length()
    ll.insert_at(5,99)
    ll.insert_value([88,999])
    ll.remove_at(3)
    ll.insert_after_value(33,"yey")
    ll.find_by_value(3)
    ll.print()