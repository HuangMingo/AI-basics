# Bắt đầu Module 1 – Buổi 2

## Kiểu dữ liệu, toán tử và điều kiện

**Thời lượng đề xuất:** 120 phút  
**Sản phẩm cuối buổi:** Chương trình nhập điểm, kiểm tra dữ liệu và xếp loại học lực, kèm ít nhất 5 test case.

## 1. Kiểm tra nhanh kiến thức Buổi 1

Trước khi học nội dung mới, hãy tự trả lời:

1. `input()` trả về kiểu dữ liệu gì? string
2. Vì sao phải dùng `float()` khi nhập cân nặng hoặc chiều cao? vì input() trả về str
3. `=` và `==` khác nhau như thế nào? Gán giá trị vs so sánh giá trị
4. `raise ValueError(...)` dùng để làm gì? phát sinh ngoại lệ và dừng chương trình
5. Vì sao cần kiểm tra cả dữ liệu hợp lệ và dữ liệu không hợp lệ?   vì có thể xảy a ngoại lệ

Nếu chưa trả lời được ít nhất 4/5 câu, hãy xem lại Buổi 1 trước khi tiếp tục.

## 2. Mục tiêu đầu ra

Sau buổi học, bạn cần:

- Phân biệt được `int`, `float`, `str` và `bool`.
- Ép kiểu dữ liệu bằng `int()`, `float()`, `str()` và `bool()`.
- Sử dụng được các toán tử so sánh `==`, `!=`, `<`, `<=`, `>` và `>=`.
- Kết hợp điều kiện bằng `and`, `or` và `not`.
- Viết được cấu trúc `if/elif/else` đúng thứ tự.
- Tránh so sánh số thực bằng phép bằng tuyệt đối khi kết quả có sai số.
- Viết chương trình xếp loại học lực có kiểm tra đầu vào và ít nhất 5 test case.

## 3. Bốn kiểu dữ liệu cơ bản

### `int` – số nguyên

```python
age = 20
number_of_images = 150
```

### `float` – số thực

```python
score = 8.5
learning_rate = 0.01
```

### `str` – chuỗi ký tự

```python
name = "An"
label = "cat"
```

### `bool` – giá trị đúng hoặc sai

```python
is_valid = True
is_finished = False
```

Dùng `type()` để kiểm tra kiểu dữ liệu:

```python
print(type(20))       # <class 'int'>
print(type(8.5))      # <class 'float'>
print(type("An"))    # <class 'str'>
print(type(True))     # <class 'bool'>
```

## 4. Ép kiểu dữ liệu

`input()` luôn trả về `str`, vì vậy dữ liệu nhập thường cần được chuyển kiểu trước khi tính toán.

```python
age = int(input("Tuổi của bạn: "))
score = float(input("Điểm của bạn: "))
```

Một số ví dụ:

```python
int("20")       # 20
float("8.5")    # 8.5
str(20)          # "20"
bool(1)          # True
bool(0)          # False
```

Không phải chuỗi nào cũng chuyển được thành số:

```python
float("tám")    # Phát sinh ValueError
```

Vì vậy, phần ép kiểu dữ liệu nhập nên được đặt trong `try/except`:

```python
try:
    score = float(input("Nhập điểm: "))
except ValueError:
    print("Điểm phải là một số.")
```

## 5. Toán tử so sánh

Các phép so sánh trả về `True` hoặc `False`:

```python
score = 8.5

print(score == 8.5)   # True
print(score != 10)    # True
print(score > 5)      # True
print(score >= 8)     # True
print(score < 5)      # False
print(score <= 10)    # True
```

Phân biệt hai toán tử quan trọng:

- `=` dùng để gán giá trị.
- `==` dùng để so sánh hai giá trị.

```python
score = 8.5           # Gán giá trị
print(score == 8.5)   # So sánh
```

## 6. Toán tử logic

### `and`

Kết quả chỉ đúng khi cả hai điều kiện đều đúng:

```python
score = 8.5
is_valid = score >= 0 and score <= 10
```

### `or`

Kết quả đúng khi có ít nhất một điều kiện đúng:

```python
is_invalid = score < 0 or score > 10
```

### `not`

Đảo ngược giá trị đúng và sai:

```python
is_valid = True
print(not is_valid)   # False
```

## 7. Cấu trúc `if/elif/else`

Python kiểm tra điều kiện từ trên xuống dưới và dừng ở nhánh đúng đầu tiên.

```python
def classify_score(score):
    if score >= 8.5:
        return "Giỏi"
    elif score >= 7.0:
        return "Khá"
    elif score >= 5.0:
        return "Trung bình"
    else:
        return "Chưa đạt"
```

Thứ tự điều kiện rất quan trọng. Phải kiểm tra ngưỡng cao trước:

```python
# Sai vì điểm 9 cũng thỏa mãn score >= 5
if score >= 5:
    return "Trung bình"
elif score >= 8.5:
    return "Giỏi"
```

## 8. Kiểm tra điểm không hợp lệ

Điểm hợp lệ nằm trong khoảng từ 0 đến 10.

```python
def classify_score(score):
    if score < 0 or score > 10:
        raise ValueError("Điểm phải nằm trong khoảng từ 0 đến 10")

    if score >= 8.5:
        return "Giỏi"
    elif score >= 7.0:
        return "Khá"
    elif score >= 5.0:
        return "Trung bình"
    else:
        return "Chưa đạt"
```

Phần nhập dữ liệu cần nằm trong `try` để xử lý cả hai trường hợp: nhập chữ và nhập số ngoài khoảng.

```python
try:
    score = float(input("Nhập điểm từ 0 đến 10: "))
    result = classify_score(score)
    print(f"Xếp loại: {result}")
except ValueError as error:
    print(f"Dữ liệu không hợp lệ: {error}")
```

## 9. So sánh số thực

Số thực trong máy tính có thể có sai số biểu diễn:

```python
print(0.1 + 0.2 == 0.3)   # Có thể là False
```

Khi cần kiểm tra hai số thực gần bằng nhau, dùng `math.isclose()`:

```python
import math

result = 0.1 + 0.2
print(math.isclose(result, 0.3))   # True
```

Trong test case có kết quả số thực, bạn cũng có thể làm tròn trước khi so sánh:

```python
assert round(0.1 + 0.2, 2) == 0.30
```

## 10. Bài thực hành có hướng dẫn

Tạo tệp `student_grade.py`.

### Mức 1 – Nhập và in điểm

- Nhập tên học sinh.
- Nhập điểm từ bàn phím.
- In tên và điểm.

### Mức 2 – Kiểm tra dữ liệu

- Từ chối điểm nhỏ hơn 0 hoặc lớn hơn 10.
- Xử lý trường hợp người dùng nhập chữ hoặc chuỗi rỗng.
- Thông báo rõ nguyên nhân lỗi.

### Mức 3 – Xếp loại học lực

Dùng các ngưỡng sau cho bài tập:

- Từ 8.5 đến 10: `Giỏi`.
- Từ 7.0 đến dưới 8.5: `Khá`.
- Từ 5.0 đến dưới 7.0: `Trung bình`.
- Từ 0 đến dưới 5.0: `Chưa đạt`.

Tách quy tắc trên thành hàm:

```python
def classify_score(score):
    # Viết phần kiểm tra và xếp loại tại đây.
    pass
```

### Mức 4 – Kiểm thử

Tạo ít nhất 5 test case, nên bao gồm:

1. Một điểm thuộc loại Giỏi.
2. Một điểm đúng tại ranh giới 8.5.
3. Một điểm đúng tại ranh giới 5.0.
4. Một điểm âm.
5. Một điểm lớn hơn 10.

Mẫu kiểm tra kết quả hợp lệ:

```python
assert classify_score(8.5) == "Giỏi"
```

Mẫu kiểm tra dữ liệu không hợp lệ:

```python
def expect_value_error(score):
    try:
        classify_score(score)
    except ValueError:
        return True
    return False


assert expect_value_error(-1)
```

## 11. Tiêu chí hoàn thành

Bạn hoàn thành Buổi 2 khi:

- [x] Phân biệt và đưa được ví dụ về `int`, `float`, `str`, `bool`.
      int la kieu so nguyen   n = 5
      float la so thuc    f = 4.5
      str la kieu chuoi c = "An"
      bool la True hoac False
- [ ] Giải thích được sự khác nhau giữa `=`, `==` và `!=`.
- [ ] Sử dụng đúng `and`, `or`, `not` trong điều kiện.
- [ ] Viết được hàm `classify_score(score)` bằng `if/elif/else`.
- [ ] Chương trình từ chối điểm ngoài khoảng và dữ liệu không chuyển được thành số.
- [ ] Có ít nhất 5 test case, gồm các giá trị bình thường, ranh giới và không hợp lệ.
- [ ] Giải thích được vì sao không nên luôn so sánh số thực bằng `==`.
- [ ] Tự giải thích được phần mã mình viết.

## 12. Câu hỏi tự kiểm tra

1. `input()` trả về `str` hay `float`?
2. `int("8")` và `float("8")` tạo ra kết quả khác nhau như thế nào?
3. Biểu thức `score >= 0 and score <= 10` có ý nghĩa gì?
4. Khi nào điều kiện dùng `or` phù hợp hơn `and`?
5. Vì sao phải kiểm tra ngưỡng điểm cao trước trong bài xếp loại?
6. `elif` khác một câu lệnh `if` độc lập như thế nào?
7. Vì sao `0.1 + 0.2 == 0.3` có thể trả về `False`?
8. Khi nào nên dùng `math.isclose()`?

## 13. Bài tập về nhà – 10 bài điều kiện tăng dần

1. Kiểm tra một số là dương, âm hay bằng 0.
2. Kiểm tra một số nguyên là chẵn hay lẻ.
3. Tìm số lớn hơn trong hai số.
4. Tìm số lớn nhất trong ba số.
5. Kiểm tra một năm có phải năm nhuận hay không.
6. Kiểm tra tuổi có đủ điều kiện từ 18 trở lên hay không.
7. Xếp loại học lực từ một điểm số.
8. Tính giá vé theo nhóm tuổi do bạn tự định nghĩa.
9. Kiểm tra ba cạnh có tạo thành tam giác hay không.
10. Viết chương trình tính tiền điện theo ít nhất ba bậc giá giả định và ghi rõ các bậc trong comment.

Với mỗi bài:

- Viết rõ Input → Process → Output.
- Kiểm tra dữ liệu không hợp lệ nếu có.
- Tạo ít nhất 3 test case.
- Ghi kết quả mong đợi trong comment.

## 14. Nhật ký học tập

Sau khi hoàn thành, điền ngắn gọn:

- Điều tôi đã hiểu: 
- Lỗi tôi đã gặp:
- Nguyên nhân của lỗi:
- Cách tôi sửa lỗi:
- Điều tôi còn chưa chắc:
