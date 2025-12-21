n = int(input("Nhập vị trí n: "))
if n <= 1:
    print(f"Số Fibonacci thứ {n} là: {n}")
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(f"Số Fibonacci thứ {n} là: {b}")