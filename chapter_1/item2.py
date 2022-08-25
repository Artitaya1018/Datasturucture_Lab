'''
โจทย์: จงเขียนโปรแกรมรับความเร็วลมเฉลี่ยใน 10 นาที และแสดงผลระดับพายุที่เกิดขึ้น จากการจัดแบ่งความเร็วลมดังนี้

		Speed (km/h)		ระดับพายุ
			0-51.99			Breeze
			52.00-55.99		Depression
			56.00-101.99	        Tropical Storm
			102.00-208.99	        Typhoon
			>= 209			Super Typhoon

โดยแสดงผลตามตัวอย่างการแสดงผล

'''

print(" *** Wind classification ***")
wind = input("Enter wind speed (km/h) : ")

if float(wind) <= 51.99 : print("Wind classification is Breeze.")
elif float(wind) <= 55.99 : print("Wind classification is Depression.")
elif float(wind) <= 101.99 : print("Wind classification is Tropical Storm.")
elif float(wind) <= 208.99 : print("Wind classification is Typhoon.")
else : print("Wind classification is Super Typhoon.") 