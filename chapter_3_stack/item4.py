'''
กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น 
ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง 
ต้นไม้ที่เคยเดินผ่านไป

ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

อธิบาย Input :   A  <Heights>  แสดงถึงความสูงของต้นไม้  ,   B  คือการหันหลังกลับมามอง
อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น 
ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 

โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง

class Stack:

    ### Enter Your Code Here ###

S = Stack()


inp = input('Enter Input : ').split(',')

### Enter Your Code Here ###
'''

class Stack:
    def __init__(self, list = None) :
        self.list = []
        if list != None : self.list = list
    def getStack(self) :
        return self.list
    def peek(self) :
        return self.list[-1]
    def push(self, input) :
        self.list.append(input)
    def pop(self) :
        return self.list.pop()
    def size(self) :
        return len(self.list)
    def isEmpty(self) :
        return not bool(self.list)
 
inp = input('Enter Input : ').split(',')

S = Stack()
count = 0

for i in inp :
    order = i.split()
    if order[0] == "A" : 
        if S.isEmpty() : S.push(int(order[1]))
        else :
            while not S.isEmpty() and S.peek() <= int(order[1]) : S.pop()
            S.push(int(order[1]))
    elif order[0] == "B" : print(S.size())