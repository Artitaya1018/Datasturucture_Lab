class Queue() :

    def __init__(self,list = None) :
        if list == None : self.items = list
    
    def enQueue(self,i) :
        self.items.append(i)

    def deQueue(self) :
        return self.items.pop(0)

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)

input = input("Enter Input : ").split(",")

activity = { '0':'Eat', '1':'Game', '2':'Learn', '3':'Movie'}
Location = { '0': 'Res.', '1':'ClassR.', '2':'SuperM.', '3':'Home'}

q = Queue()
q1 = Queue()
score = 0

for i in input :
    myq = i.split()[0]
    yrq = i.split()[1]
    
    if myq.split(":")[0] == yrq.split(":")[0] and myq.split(":")[1] == yrq.split(":")[1] : score += 4
    elif myq.split(":")[1] == yrq.split(":")[1] : score += 2
    elif myq.split(":")[0] == yrq.split(":")[0] : score += 1
    else : score -= 5

    q.enQueue(myq)
    q1.enQueue(yrq)



print("My   Queue",q.items)
print("Your Queue",q1.items)
print("My   Activity:Location = ",activity[q.items])
print("My   Activity:Location = ",activity[q1.items])



