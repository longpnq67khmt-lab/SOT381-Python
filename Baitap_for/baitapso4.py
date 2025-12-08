# 4. Kiểm tra số hoàn hảo

import math

a = int(input("Nhập vào số kiểm tra: "))
sum = 0

for i in range(1, a):
	if a % i == 0:
		sum += i

if (sum == a):
	print(f"{a} là một số hoàn hảo!")
