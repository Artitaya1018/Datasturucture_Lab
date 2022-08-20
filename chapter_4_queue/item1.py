""" ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา

    E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป

    D           ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue หลังจากทำการ dequeue แล้ว

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty *** """

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