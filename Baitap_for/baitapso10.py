so = input("Nhập số: ")
n = len(so)
tong = sum(int(chu_so)**n for chu_so in so)

if tong == int(so):
    print(f"{so} là số Armstrong")
else:
    print(f"{so} không phải số Armstrong")