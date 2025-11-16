# 16. Giải phương trình bậc 1

a = int(input("Hãy nhập a: "))
b = int(input("Hãy nhập b: "))

if (a == 0):
	if (b == 0):
		print("Phương trình có vô số nghiệm!")
	else:
		print("Phương trình vô nghiệm!")
else:
	x = -b/a
	print(f"Phương trình có 1 nghiệm: {x}")
