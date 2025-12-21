n = int(input("Nhập n: "))

for so in range(2, n + 1):
    so_nguyen_to = True

    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            so_nguyen_to = False
            break

    if so_nguyen_to:
        print(f"{so} là số nguyên tố")
