n = int(input("Nhập số phần tử mong muốn: "))

list = []
for i in range(n):
  list.append(int((input(f"Giá trị của phần tử {i}: "))))

list.sort()
print(list)