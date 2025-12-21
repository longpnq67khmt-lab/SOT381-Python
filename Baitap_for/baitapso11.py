import random

so_bi_mat = random.randint(1, 100)
lan_doan = 0

while True:
    doan = int(input("Đoán số (1-100): "))
    lan_doan += 1
    
    if doan < so_bi_mat:
        print("Số lớn hơn!")
    elif doan > so_bi_mat:
        print("Số nhỏ hơn!")
    else:
        print(f"Chính xác! Số đó là {so_bi_mat}")
        print(f"Bạn đã đoán {lan_doan} lần")
        break