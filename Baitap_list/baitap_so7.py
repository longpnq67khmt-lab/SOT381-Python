n = int(input("Nhập số phần tử mong muốn: "))

list = []
for i in range(n):
  list.append(int((input(f"Giá trị của phần tử {i}: "))))

tong = 0
for i in list:
  tong += i

dtb = tong / len(list)
print(dtb)