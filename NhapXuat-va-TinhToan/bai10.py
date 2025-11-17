# 10. Tính lãi suất đơn

a = int(input("Nhập vào số tiền muốn gửi: "))
b = float(input("Nhập vào lãi suất (phần trăm/năm): "))
c = int(input("Nhập vào số tháng gửi: "))

print(f"Số tiền lãi: {(a * b * c)/12}")