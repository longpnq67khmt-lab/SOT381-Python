# TỔNG HỢP KIẾN THỨC PYTHON CƠ BẢN

---

## 1. Toán Tử Và Biểu Thức Trong Python

### 1.1. Toán tử số học

| Toán tử | Ý nghĩa              |
| ------- | -------------------- |
| `+`     | Cộng                 |
| `-`     | Trừ                  |
| `*`     | Nhân                 |
| `/`     | Chia (kết quả float) |
| `//`    | Chia lấy phần nguyên |
| `%`     | Chia lấy phần dư     |
| `**`    | Lũy thừa             |

### 1.2. Toán tử so sánh

| Toán tử | Ý nghĩa           |
| ------- | ----------------- |
| `==`    | Bằng              |
| `!=`    | Khác              |
| `>`     | Lớn hơn           |
| `<`     | Nhỏ hơn           |
| `>=`    | Lớn hơn hoặc bằng |
| `<=`    | Nhỏ hơn hoặc bằng |

### 1.3. Toán tử logic

| Toán tử | Ý nghĩa                             |
| ------- | ----------------------------------- |
| `and`   | True nếu cả hai điều kiện True      |
| `or`    | True nếu ít nhất một điều kiện True |
| `not`   | Phủ định                            |

### 1.4. Toán tử Identity

So sánh vùng nhớ của đối tượng:

* `is`: True nếu cùng tham chiếu một đối tượng
* `is not`: True nếu tham chiếu khác đối tượng

### 1.5. Toán tử Membership

Kiểm tra phần tử có trong chuỗi / list:

* `in`
* `not in`

---

## 2. Nhập Và Xuất Dữ Liệu Trong Python

```python
print("Hello", "World", "!")
print("Hello", "World", "!", sep="-")
print("Hello", end=" ")
print("World")
```

Xử lý lỗi khi ép kiểu:

```python
try:
    number = int(input("Nhập số nguyên: "))
    print(number)
except ValueError:
    print("Giá trị không hợp lệ")
```

---

## 3. Cấu Trúc Điều Khiển If – Elif – Else

```python
if dieu_kien:
    pass
elif dieu_kien_khac:
    pass
else:
    pass
```

Ví dụ:

```python
diem_toan = 8
diem_van = 7.5

if diem_toan >= 8 and diem_van >= 8:
    print("Học sinh giỏi")

if diem_toan >= 9 or diem_van >= 9:
    print("Có môn xuất sắc")
```

---

## 4. Vòng Lặp

### 4.1. Vòng lặp for

```python
for i in range(5):
    print(i)
```

### 4.2. Vòng lặp while

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## 5. List Trong Python

### 5.1. Tạo list

```python
lst = []
lst2 = [1, 2, 3]
lst3 = list(range(5))
lst4 = [0] * 5
```

### 5.2. Duyệt list

```python
for item in lst2:
    print(item)

for i, v in enumerate(lst2):
    print(i, v)
```

### 5.3. Thao tác với list

* Thêm: `append()`, `insert()`, `extend()`
* Sửa: gán theo chỉ số
* Xóa: `remove()`, `pop()`, `del`, `clear()`

### 5.4. Tìm kiếm và sắp xếp

```python
lst.sort()
lst.reverse()
copy_lst = lst.copy()
```

### 5.5. List Comprehension

```python
binh_phuong = [x**2 for x in range(1, 6)]
so_chan = [x for x in range(10) if x % 2 == 0]
```

---

## 6. Hàm (Function)

```python
def cong(a, b):
    return a + b
```

Hàm trả về nhiều giá trị:

```python
def tinh_toan(a, b):
    return a+b, a-b, a*b
```

---

## 7. Chuỗi (String) Trong Python

### 7.1. Kiểm tra chuỗi

```python
s = "Python123"
s.isalnum()
s.isalpha()
```

### 7.2. Biến đổi chuỗi

```python
s.strip()
s.lower()
s.upper()
```

### 7.3. Tìm kiếm và thay thế

```python
s.find("World")
s.replace("World", "Python")
```

### 7.4. Tách và nối chuỗi

```python
items = s.split(",")
new_s = "-".join(items)
```

---