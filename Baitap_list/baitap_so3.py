n = int(input("Nhập số phần tử mong muốn: "))

list = []
for i in range(n):
  list.append(int(input(f"Giá trị của phần tử {i}: ")))
print(list)

so_chan = 0
so_le = 0

for i in list:
  if i % 2 == 0:
    so_chan += 1
  else:
    so_le += 1
    
print(f"Tổng số chẵn: {so_chan}")
print(f"Tổng số lẻ: {so_le}")