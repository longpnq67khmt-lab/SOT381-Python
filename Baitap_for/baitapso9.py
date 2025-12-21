von = float(input("Nhập vốn ban đầu: "))
lai_suat = float(input("Nhập lãi suất năm (%): "))
nam = int(input("Nhập số năm: "))

for i in range(1, nam + 1):
    von *= (1 + lai_suat / 100)
    print(f"Năm {i}: {von:,.0f} VND")
