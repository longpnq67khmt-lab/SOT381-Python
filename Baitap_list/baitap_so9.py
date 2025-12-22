n = int(input("Nhập số phần tử mong muốn: "))

list1 = []
for i in range(n):
  list1.append(int((input(f"Giá trị của phần tử {i}: "))))

list2 = []
for i in range(n):
  list2.append(int((input(f"Giá trị của phần tử {i}: "))))

list3 = list1 + list2

print(list3)