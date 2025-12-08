# 3. Nhập dãy số và kiểm tra số chẵn hay số lẻ
a, b = map(int, input().split())
uscln = 0
while True:
	if (b % a != 0):
		a = b % a
	else:
		print(f"ƯSCLN: {a} ")
		break
	pass