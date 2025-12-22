lst = [1, 2, 2, 3, 1, 4, 2]

ket_qua = []

for x in lst:
    if x not in ket_qua:
        ket_qua.append(x)

print(ket_qua)