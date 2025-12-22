n = int(input("Nhập số phần tử mong muốn: "))

list = []
for i in range(n):
  list.append((input(f"Giá trị của phần tử {i}: ")))

print(f"Vị trí của phần từ x trong list là: {list.index("x")}")