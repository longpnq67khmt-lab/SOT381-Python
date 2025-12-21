so = input("Nhập số hoặc chuỗi: ")
dao = ""

for ky_tu in so:
    dao = ky_tu + dao
    print(dao)

if so == dao:
    print("Là số/chuỗi đối xứng")
else:
    print("Không phải số/chuỗi đối xứng")
