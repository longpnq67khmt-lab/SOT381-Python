# 18. Máy tính Đơn giản

a = int(input("Hãy nhập số nguyên a: "))
b = int(input("Hãy nhập số nguyên b: "))
dau = input("Nhập phép toán a (+, -, *, /) b: ")

if (dau == "+"):
	print(f"{a} + {b} = {a + b}")
elif (dau == "-"):
	print(f"{a} - {b} = {a - b}")
elif (dau == "*"):
	print(f"{a} * {b} = {a * b}")
elif (dau == "/"):
	if (b == 0):
		print("Phép toán không hợp lệ")
	else:
		print(f"{a} / {b} = {a / b}")
else:
	print('Dấu không hợp lệ')