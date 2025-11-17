# 11. Đăng nhập Đơn giản

username = input("Tài khoản: ")
password = input("Mật khẩu: ")

if (username == "admin") and (password == "123456"):
	print("Đăng nhập thành công!")
else:
	print("Đăng nhập thất bại!")