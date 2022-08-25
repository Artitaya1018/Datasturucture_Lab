# เขียนภาษา Python เพื่อวาดรูปหัวใจ ซึ่งจะรับ input เป็นขนาดของรูปหัวใจ โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป

print("*** Fun with Drawing ***")
size = int(input("Enter input : "))
for i in range(size) :
    for j in range(size * 4 - 3):
        if j < (size-1) - i or (j > (size-1) + i and j < (size*3-3) - i) or j > (size*3-3) + i: print(".", end = "")
        elif (j > (size-1) - i and j < (size-1) + i) or (j > (size*3-3) - i and j < (size*3-3) + i): print("+", end = "")
        else : print("*", end = "")
    print()

for i in range(size * 2 - 2) :
    for j in range(size * 4 - 3):
        if j <= i or j >= (size*4-4) - i: print(".", end = "")
        elif j > (i+1) and j < (size*4-4) - (i+1) : print("+", end = "")
        else : print("*", end = "")
    print() 