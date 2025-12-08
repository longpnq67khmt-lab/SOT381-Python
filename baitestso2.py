# baiso2 viết chương trình nhập vào 1 số nguyên, cho biết số đó có chia hết cho đồng thời 3 và 5 hay không
a = int(input("Nhập vào số a: "))
if (a % 3 == 0 and a % 5 == 0):
	print("a chia hết!")
else:
	print("a không chia hết!")
