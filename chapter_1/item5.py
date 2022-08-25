# เขียนภาษา Python เพื่อวาดรูปหยิน-หยาง ซึ่งจะรับ input เป็นขนาดของรูปหยิน-หยาง
size = int(input("Enter Input : "))

for i in range(size + 2):
    for j in range((size + 2) * 2):
        if j < (size + 2) - (i+1) : print(".", end = "")
        elif j >= size + 2 : 
            if i == 0 or i == (size + 2) - 1 : print("+", end = "")
            else:
                if j == size + 2 or j == ((size + 2) * 2) - 1 : print("+", end = "")
                else : print("#", end = "")
        else : print("#", end = "")
    print()

for i in range(size + 2):
    for j in range((size + 2) * 2):
        if j <= (size + 2) - 1 :
            if i == 0 or i == (size + 2) - 1 : print("#", end = "")
            else :
                if j == 0 or j == (size + 2) - 1 : print("#", end = "")
                else : print("+", end = "")
        else : 
            if j > ((size + 2) * 2) - (i + 1) : print(".", end = "")
            else : print("+", end = "")
    print()