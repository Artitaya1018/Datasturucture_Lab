'''
รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที
แล้วแสดงผลเป็น วินาที
แสดงผลตามตัวอย่าง
'''

print("*** Converting hh.mm.ss to seconds ***")
h, m, s = input("Enter hh mm ss : ").split()

time = (int(h) * 3600) + (int(m) * 60) + int(s)

if int(m) >= 60 or int(m) < 0 :
    print("mm({}) is invalid!". format(int(m)))
elif int(s) >= 60 or int(s) < 0 :
    print("ss({}) is invalid!". format(int(s)))
else :
    print("{:02d}:{:02d}:{:02d} = {:,} seconds". format(int(h), int(m), int(s), time))
