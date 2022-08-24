'''
จงเขียนโปรแกรมโดยใช้ stack เพื่อรับตัวเลขฐาน 10 แล้วเปลี่ยนเป็นเลขฐาน 2 แล้วให้แสดงผลดังตัวอย่าง

class Stack :

    ### Enter Your Code Here ###

def dec2bin(decnum):

    s = Stack()

    ### Enter Your Code Here ###

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))
'''

class Stack:
    def __init__(self, list = None) :
        self.list = []
        if list != None : self.list = list
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

print(" ***Decimal to Binary use Stack***")

decNum = int(input("Enter decimal number : "))

s = Stack()

while decNum > 0:
    if decNum % 2 == 1 :
        s.push(1)
        decNum = decNum//2
    else :
        s.push(0)
        decNum = decNum//2

print("Binary number : ",end ="")
while not s.isEmpty() :
    print(s.pop(),end = "")