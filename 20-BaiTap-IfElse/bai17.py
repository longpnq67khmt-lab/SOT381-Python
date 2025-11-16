# 17. Giải phương trình bậc 2

import math

a = int(input("Hãy nhập a: "))
b = int(input("Hãy nhập b: "))
c = int(input("Hãy nhập c: "))

if (a == 0):
	if (b == 0):
		print("Phương trình có vô số nghiệm!")
	else:
		print("Phương trình có 1 nghiệm: x = ", -c / b)
else:
	delta = b*b - 4*a*c
	if (delta < 0):
		print("Vô nghiệm!")
	elif (delta == 0):
		x = -b / 2*a
		print(f"Có nghiệm kép: {x}")
	else:
		x1 = (-b + math.sqrt(delta)) / (2*a)
		x2 = (-b - math.sqrt(delta)) / (2*a)
		print(f"Phương trình có 2 nghiệm phân biệt lần lượt là: {x1}, {x2} ")