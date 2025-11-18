# 1. Viết chương trình kiểm tra một số có thỏa mãn đồng thời 3 điều kiện:

a = int(input("Nhập vào số a để kiểm tra: "))

if (a % 2 == 0) and (a > 10) and (a % 3 == 0):
	print(f"{a} thỏa mãn hết 3 điều kiện!")
else:
	print(f"{a} không thỏa mãn 3 điều kiện!")