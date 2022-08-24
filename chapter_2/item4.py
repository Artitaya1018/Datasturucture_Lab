'''
หาค่าฐานของอายุของน้องสายไหม ที่อายุ 20,21 ตลอดกาล เช่น
hbd(65) = "saimai is just 21, in base 32!"
hdb(21) = "saimai is just 21, in base 10!"
hdb(8888) = "saimai is just 20, in base 4444!"

def hbd(age):

    ### Enter Your Code Here ###

year = input("Enter year : ")

print(hbd(int(year)))
'''

def hbd(age):
    i = 1
    while (True) :
        if age / i == 2 or (age - 1) / i == 2 :
            if age % 2 == 1 :
                return "saimai is just 21, in base "+str(i)+"!"
            else :
                return "saimai is just 20, in base "+str(i)+"!" 
        else : i += 1

year = input("Enter year : ")
print(hbd(int(year)))