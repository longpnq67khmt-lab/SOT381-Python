def timso(list1):
  so_lon = max(list1)
  so_be = min(list1)
  return so_lon, so_be

ds = [1, 2, 3]
so_lon, so_be = timso(ds)

print(so_lon)
print(so_be)