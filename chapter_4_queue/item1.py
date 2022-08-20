class Queue() :

    def __init__ (self,list = None) :
        if list == None : self.items = []
        else : self.items = list
    
    def enQueue(self,i) :
        self.items.append(i)

    def deQueue(self) :
        return self.items.pop(0)

    def isEmpty(self) :
        return self.items == []
    
    def size(self) :
        return len(self.items)

input = input("Enter Input : ").split(",")
q = Queue() 

for i in input :
    order = i.split()
    if order[0] == 'E' :
        q.enQueue(order[1])
        print("Add " + str(order[1]) + " index is " + str(q.size()-1))
    elif order[0] == 'D' :
        if not q.isEmpty() :
            print("Pop" , str( q.deQueue()) , "size in queue is " , str(q.size()))
        else :
            print("-1")
            
if not q.isEmpty() :
    print("Number in Queue is : " , q.items)
else :
    print("Empty")