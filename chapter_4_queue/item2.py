'''
จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue
โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้
แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ
แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ
ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2
จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด
'''

class Queue() :
    
    def __init__(self,list = None) :
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

inp = input("Enter people : ")

q = Queue()
q1 = Queue()
q2 = Queue()
mins = 0
countQ2 = 0

for i in inp : q.enQueue(i)

while not q.isEmpty() :
    mins += 1
    if (mins-1) % 3 == 0 and (mins-1) != 0 : q1.deQueue()       # ออกนาทีที่4
    if countQ2 == 2 :                                           # นาทีที่ 0 1 2 แล้วกลับมารีเซตใหม่
        countQ2 = 0
        q2.deQueue()
    
    if q1.size() < 5 :                                          # size() = เกิน 5 จะไป list ของ q2
        q1.enQueue(q.deQueue())
    elif q2.size() < 5 :
        q2.enQueue(q.deQueue())

    if not q2.isEmpty() : countQ2 += 1

    print(mins, q.items, q1.items, q2.items)


