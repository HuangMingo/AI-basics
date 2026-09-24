# Bắt đầu Module 1 – Buổi 3

## Vòng lặp và hàm

**Thời lượng đề xuất:** 120 phút  
**Sản phẩm cuối buổi:** Chương trình tính `mean`, `min`, `max` bằng vòng lặp, không dùng các hàm dựng sẵn `sum()`, `min()` và `max()`, kèm ít nhất 5 test case.

## 1. Kiểm tra nhanh kiến thức Buổi 2

Hãy tự trả lời trước khi xem nội dung mới:

1. `input()` luôn trả về kiểu dữ liệu gì?
2. `=` khác `==` như thế nào?
3. Điều kiện `score < 0 or score > 10` có ý nghĩa gì?
4. Vì sao `0.1 + 0.2 == 0.3` có thể trả về `False`?
5. `try/except` trong `student_grade.py` giúp chương trình xử lý tình huống nào?
6. Hàm `classify_score(score)` nhận gì và trả về gì?

Chỉ tiếp tục khi bạn có thể tự giải thích ít nhất 5/6 câu.

## 2. Mục tiêu đầu ra

Sau buổi này, bạn có thể:

- Dùng `for` để duyệt qua một dãy giá trị.
- Dùng `range()` để tạo dãy số cho vòng lặp.
- Dùng `while` khi số lần lặp phụ thuộc vào điều kiện.
- Giải thích và sử dụng đúng `break` và `continue`.
- Viết hàm có tham số và giá trị `return`.
- Phân biệt biến cục bộ và biến bên ngoài hàm.
- Tách một bài toán thành các hàm nhỏ, dễ kiểm thử.
- Tính `mean`, `min`, `max` không dùng hàm dựng sẵn.

## 3. Vòng lặp dùng để làm gì?

Vòng lặp giúp thực hiện một nhóm lệnh nhiều lần. Thay vì viết:

```python
print(1)
print(2)
print(3)
```

ta có thể viết:

```python
for number in range(1, 4):
    print(number)
```

Mỗi lần vòng lặp chạy được gọi là một **lần lặp**.

## 4. Vòng lặp `for`

### Duyệt qua danh sách

```python
scores = [7.5, 8.0, 6.5, 9.0]

for score in scores:
    print(score)
```

Trong mỗi lần lặp, `score` lần lượt nhận một giá trị trong `scores`.

### Biến tích lũy

Để tính tổng, ta bắt đầu từ `0` và cộng dồn từng giá trị:

```python
values = [2, 4, 6]
total = 0

for value in values:
    total = total + value

print(total)  # 12
```

`total` được gọi là biến tích lũy.

## 5. Hàm `range()`

```python
for number in range(5):
    print(number)
```

Kết quả là `0, 1, 2, 3, 4`. Giá trị kết thúc `5` không được lấy.

Các dạng thường dùng:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Ví dụ:

```python
for number in range(2, 11, 2):
    print(number)  # 2, 4, 6, 8, 10
```

## 6. Vòng lặp `while`

`while` tiếp tục chạy khi điều kiện còn là `True`:

```python
count = 1

while count <= 3:
    print(count)
    count = count + 1
```

Phải có lệnh làm thay đổi điều kiện. Nếu quên `count = count + 1`, vòng lặp có thể chạy mãi.

### Khi nào dùng `for`, khi nào dùng `while`?

- Dùng `for` khi duyệt qua một dãy hoặc biết rõ phạm vi lặp.
- Dùng `while` khi việc dừng lại phụ thuộc vào một điều kiện.

## 7. `break` và `continue`

### `break` – thoát khỏi vòng lặp

```python
for number in range(1, 10):
    if number == 5:
        break
    print(number)
```

Chương trình chỉ in `1, 2, 3, 4`.

### `continue` – bỏ qua lần lặp hiện tại

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Chương trình in `1, 2, 4, 5`.

## 8. Định nghĩa và gọi hàm

```python
def calculate_area(width, height):
    area = width * height
    return area


result = calculate_area(4, 3)
print(result)  # 12
```

Trong ví dụ này:

- `calculate_area` là tên hàm.
- `width` và `height` là tham số.
- `4` và `3` là đối số khi gọi hàm.
- `return` gửi kết quả về nơi gọi hàm.

### `return` khác `print()`

```python
def add(a, b):
    return a + b
```

`return` cho phép lưu và tiếp tục xử lý kết quả:

```python
total = add(2, 3)
double_total = total * 2
```

`print()` chỉ hiển thị dữ liệu ra màn hình.

## 9. Phạm vi biến

```python
def calculate_double(number):
    result = number * 2
    return result
```

`number` và `result` là biến cục bộ. Chúng chỉ tồn tại bên trong hàm.

Nên truyền dữ liệu qua tham số và nhận kết quả qua `return`, thay vì để hàm phụ thuộc vào nhiều biến bên ngoài.

## 10. Bài thực hành có hướng dẫn

Tạo tệp `statistics_loop.py` trong thư mục Buổi 3.

### Mức 1 – Tính tổng

Viết hàm:

```python
def calculate_total(values):
    total = 0

    for value in values:
        # Cộng value vào total.
        pass

    return total
```

Không dùng `sum()`.

### Mức 2 – Tính trung bình

Viết hàm `calculate_mean(values)` theo công thức:

```text
mean = tổng các giá trị / số lượng giá trị
```

Yêu cầu:

- Dùng vòng lặp để tính tổng.
- Không dùng `sum()`.
- Nếu danh sách rỗng, ném `ValueError` với thông báo rõ ràng.

### Mức 3 – Tìm giá trị nhỏ nhất và lớn nhất

Viết hai hàm:

```python
def find_minimum(values):
    pass


def find_maximum(values):
    pass
```

Gợi ý:

1. Từ chối danh sách rỗng.
2. Dùng phần tử đầu tiên làm giá trị nhỏ nhất hoặc lớn nhất tạm thời.
3. Duyệt qua các giá trị.
4. Cập nhật kết quả tạm thời khi gặp giá trị nhỏ hơn hoặc lớn hơn.

Không dùng `min()` hoặc `max()`.

### Mức 4 – Tách chương trình thành hàm

Tạo hàm tổng hợp:

```python
def summarize(values):
    return {
        "mean": calculate_mean(values),
        "min": find_minimum(values),
        "max": find_maximum(values),
    }
```

Sau đó gọi hàm với:

```python
numbers = [4, 7, 2, 9, 3]
print(summarize(numbers))
```

Kết quả mong đợi:

```text
{'mean': 5.0, 'min': 2, 'max': 9}
```

### Mức 5 – Kiểm thử

Tạo ít nhất 5 test case, bao gồm:

1. Danh sách nhiều số dương.
2. Danh sách có số âm.
3. Danh sách chỉ có một phần tử.
4. Danh sách có các giá trị trùng nhau.
5. Danh sách rỗng phải gây ra `ValueError`.

Ví dụ:

```python
assert calculate_mean([2, 4, 6]) == 4
assert find_minimum([-2, 5, 1]) == -2
assert find_maximum([7]) == 7
```

Tự viết hàm kiểm tra `ValueError` tương tự Buổi 2.

## 11. Cách tự kiểm chứng

Chạy tệp:

```powershell
py -X utf8 "Bat dau Module 1 - Buoi 3\statistics_loop.py"
```

Sau đó kiểm tra:

- Chương trình kết thúc mà không có `AssertionError`.
- Kết quả của `[4, 7, 2, 9, 3]` là `mean = 5.0`, `min = 2`, `max = 9`.
- Trong tệp không có lời gọi `sum(`, `min(` hoặc `max(`.
- Bạn có thể giải thích giá trị của biến tích lũy sau mỗi lần lặp.

## 12. Tiêu chí hoàn thành

Bạn hoàn thành Buổi 3 khi:

- [ ] Giải thích được khi nào dùng `for` và khi nào dùng `while`.
- [ ] Dự đoán đúng các giá trị do `range()` tạo ra.
- [ ] Phân biệt được `break` và `continue`.
- [ ] Viết được hàm có tham số và `return`.
- [ ] Giải thích được phạm vi của biến cục bộ.
- [ ] Tính được `mean`, `min`, `max` bằng vòng lặp, không dùng hàm dựng sẵn tương ứng.
- [ ] Chương trình từ chối danh sách rỗng bằng `ValueError`.
- [ ] Có ít nhất 5 test case, gồm trường hợp bình thường, biên và không hợp lệ.
- [ ] Tự giải thích được phần mã mình viết.

## 13. Câu hỏi tự kiểm tra

1. `range(2, 8, 2)` tạo ra những số nào?
2. Vì sao `range(5)` không tạo ra số `5`?
3. Điều gì có thể xảy ra nếu điều kiện của `while` không bao giờ trở thành `False`?
4. `break` khác `continue` như thế nào?
5. `return` khác `print()` như thế nào?
6. Vì sao nên khởi tạo giá trị nhỏ nhất tạm thời bằng phần tử đầu tiên thay vì luôn dùng `0`?
7. Vì sao không thể tính mean của danh sách rỗng?
8. Biến được tạo bên trong hàm có thể dùng trực tiếp bên ngoài hàm không?

## 14. Bài tập về nhà

Viết hàm:

```python
def normalize_min_max(values):
    pass
```

Công thức chuẩn hóa mỗi giá trị `x`:

```text
(x - minimum) / (maximum - minimum)
```

Yêu cầu:

- Tự tìm `minimum` và `maximum` bằng vòng lặp.
- Trả về một danh sách mới; không thay đổi danh sách ban đầu.
- Từ chối danh sách rỗng.
- Xử lý trường hợp mọi giá trị bằng nhau để không chia cho `0`.
- Có ít nhất 5 test case.
- Viết 3–5 dòng nhật ký: lỗi đã gặp, cách sửa và điều còn chưa chắc.

Không chuyển sang Buổi 4 chỉ vì đã đọc xong. Chỉ chuyển khi các tiêu chí ở Mục 12 đã được kiểm chứng.
