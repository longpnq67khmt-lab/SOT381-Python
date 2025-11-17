# 4.Tính chỉ số BMI

height = float(input("Nhập vào chiều cao của bạn (m): "))
weight = int(input("Nhập vào cân nặng của bạn (kg): "))

BMI = weight / (height * height)
print(f"Chỉ số BMI là: {BMI}")