# 20. Kiểm tra Chẵn/Lẻ

a = int(input("Hãy nhập cạnh a: "))
b = int(input("Hãy nhập cạnh b: "))
c = int(input("Hãy nhập cạnh c: "))

if (a <= 0) or (b <= 0) or (c <= 0):
	print("Cạnh của tam giác không bé hơn bằng 0")
elif (a + b > c) and (b + c > a) and (a + c > b):
	print("Đây là một tam giác hợp lệ")
	if (a == b == c):
		print("- Tam giác đều")
	elif (a == b) or (b == c) or (a == c):
		print("- Tam giác cân")
	elif (a*a + b*b == c*c):
		print("- Tam giác vuông")
	else:
		print("- Tam giác thường")
else:
	print("Đây là một tam giác không hợp lệ")