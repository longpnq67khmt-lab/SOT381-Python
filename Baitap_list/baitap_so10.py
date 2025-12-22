cau = input()

cac_tu = cau.split()
tu_dai_nhat = cac_tu[0]

for i in cac_tu:
  if len(i) > len(tu_dai_nhat):
    tu_dai_nhat = i

print(tu_dai_nhat)