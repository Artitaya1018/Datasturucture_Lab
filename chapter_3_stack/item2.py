'''
จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack
P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )
D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  
LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

*** Hint ***ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ
'''

class Stack() :
    def __init__(self) :
        self.lst = []
    def push(self, input) :
        self.lst.append(input)
    def isEmpty(self) :
        return not bool(self.lst)
    def pop(self) :
        return self.lst.pop()
    def delete(self, num) :
        self.lst.remove(num)
        return num
    def get_stack (self) :
        return self.lst
    def peek(self) :
        return self.lst[-1]
    
def ManageStack(input) :

    s = Stack()

    for i in input:
        order = i.split()
        if order[0] == "A" : 
            s.push(int(order[1]))
            print("Add = " + order[1])
        elif order[0] == "P" :
            if s.isEmpty() : print(-1)
            else :
                print("Pop =",s.pop())
        elif order[0] == "D" :
            if s.isEmpty() : print(-1)
            else :
                temp = s.get_stack()
                while (int(order[1]) in temp) : print("Delete =",s.delete(int(order[1])))
        elif order[0] == "LD" :
            if s.isEmpty() : print(-1)
            else :
                temp = s.get_stack()
                del_temp_list = []
                for j in temp : 
                    if j < int(order[1]) : del_temp_list.append(j)
                for j in del_temp_list[::-1] :
                    while(j in temp) : print("Delete =",s.delete(j),"Because",j,"is less than "+order[1])
        elif order[0] == "MD" :
            if s.isEmpty() : print(-1)
            else :
                temp = s.get_stack()
                del_temp_list = []
                for j in temp : 
                    if j > int(order[1]) : del_temp_list.append(j)
                for j in del_temp_list[::-1] :
                        while(j in temp) : print("Delete =",s.delete(j),"Because",j,"is more than "+order[1])
    return s

order = input("Enter Input : ").split(",")

s_ans = ManageStack(order)