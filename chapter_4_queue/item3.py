'''
กฤษฎาได้มาทำงานพิเศษในช่วงปิดเทอมที่ร้านหนังสือการ์ตูนแห่งหนึ่ง  โดยเจ้าของร้านได้สั่งให้กฤษฎามาจัดหนังสือการ์ตูน Attack On Titan 
เพื่อที่จะวางขายในวันรุ่งขึ้น  โดยกฤษฎาได้จัดหนังสือไปเรื่อยๆจนรู้สึกเบื่อหน่าย  จึงได้คิดเกมสนุกๆขึ้นมานั่นคือ  ในชั้นหนังสือจะมีแค่ด้านหน้ากับด้านหลังที่จะใส่หนังสือเข้าไปได้เรื่อยๆ 
และจะนำหนังสือออกได้แค่ด้านหน้า และใส่หนังสือเพิ่มได้แค่ด้านหลัง  โดยเมื่อเล่นเกมนี้ไปเรื่อยๆ กฤษฎาก็ลืมว่าในชั้นหนังสือนั้นมีหนังสือซ้ำกันหรือไม่  
กฤษฎาเลยอยากให้คุณเขียนโปรแกรม Python เพื่อมาช่วยกฤษฎาคิดว่ามีหนังสือซ้ำกันในชั้นนั้นหรือไม่

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นหนังสือที่มีอยู่ในชั้นอยู่แล้ว  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
D                -> เป้นการนำหนังสือด้านหน้าออกจากชั้น
E <value>   -> เป็นการนำหนังสือ Attack On Titan เล่มที่ value เข้าชั้นหนังสือจากด้านหลัง
'''

class Queue() :

    def __init__(self,list = None) :
        if list == None : self.items =[]
        else : self.items =list

    def enQueue(self,i) :
        self.items.append(i)
    
    def deQueue(self) :
        return self.items.pop(0)

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)

input = input("Enter Input : ").split("/")
num = input[0].split()
q = Queue(num)

for i in input[1].split(",") :
    order = i.split()
    if order[0] == 'E' : q.enQueue(order[1])
    else : q.deQueue()

duplicated = False
for i in range(len(q.items)):                               # มันจะวนทุกตัว เช่น i เริ่ม 0 แต่ j จะเริ่ม 0+1
    for j in range(i+1, len(q.items)):
        if q.items[i] == q.items[j] : duplicated = True     # ที่ตั้งตัวแปร duplicated เป็น boolean เพราะถ้าปริ้นเลยจะทำการปริ้นซ้ำๆ

if duplicated : print("Duplicate")
else : print("NO Duplicate")