class Stack() :

    def __init__(self, list = None) :           # constructor : เป็นการตั้งค่า list ให้มีการสร้างถ้า == None , ถ้ามีการให้ทำการเอา list นั้น
        if list == None : self.items = []
        else : self.items = list                
    
    def push(self,i) :                         # การเอาค่าใส่ list                     
        self.items.append(i)
    
    def pop(self) :                            # การค่าใน list ออกไป
        return self.items.pop()                
    
    def isEmpty(self) :                        # การถามว่า list ว่างหรือไม่  ใช่ = True , ไม่ = False
        return self.items == []
    
    def size(self) :                           # บอกขนาด,จำนวนสมาชิก ที่อยู่ใน list
        return len(self.items)

print(" *** Stack Implement by Python list***")
ls = [ e for e in input("Enter data stack : ").split()]        
s = Stack()
for e in ls :
    s.push(e)
print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty() :
    s.pop()
print(s.size(),"Data in stack",s.items)