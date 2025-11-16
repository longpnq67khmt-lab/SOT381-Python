# 12. Năm nhuận

a = int(input("Nhập vào năm muốn kiểm tra: "))

if (a % 4 == 0) and	(a % 100 != 0) or (a / 400 == 0):
	print(f" năm: {a} là một năm nhuận")
else:
	print(f" năm: {a} không phải là một năm nhuận")
