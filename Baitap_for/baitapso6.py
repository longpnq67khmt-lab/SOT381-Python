so = int(input("Nhập số cần đảo ngược: "))
so_dao_nguoc = 0

while so > 0:
    chu_so_cuoi = so % 10
    so_dao_nguoc = so_dao_nguoc * 10 + chu_so_cuoi
    so //= 10

print(f"Số đảo ngược: {so_dao_nguoc}")
