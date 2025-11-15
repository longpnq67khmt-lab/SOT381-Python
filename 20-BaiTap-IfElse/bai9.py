height = float(input("Nhập vào chiều cao của bạn (m): "))
weight = int(input("Nhập vào cân nặng của bạn (kg): "))

BMI = weight / (height * height)

print(f"Chỉ số BMI của bạn là: {BMI}")
if (BMI < 18.5):
	print(f"- Tình trạng: gầy")
elif (BMI >= 25):
	print(f"- Tình trạng: thừa cân")
else:
	print(f"- Tình trạng: bình thường")
