# Bắt đầu Module 1 – Buổi 4

## Cấu trúc dữ liệu Python

**Thời lượng đề xuất:** 120 phút  
**Sản phẩm cuối buổi:** Chương trình phân tích danh sách tên file ảnh và đếm số file theo nhãn loài bằng `dict`.

## 1. Kiểm tra nhanh kiến thức Buổi 3

Hãy tự trả lời trước khi xem phần mới:

1. Khi nào nên dùng `for`, khi nào nên dùng `while`?
2. `range(2, 8, 2)` tạo ra những giá trị nào?
3. `break` khác `continue` như thế nào?
4. `return` khác `print()` như thế nào?
5. Vì sao không nên khởi tạo giá trị nhỏ nhất tạm thời bằng `0`?
6. Hàm `assert_raises_value_error()` trong bài trước kiểm tra điều gì?

Chỉ tiếp tục khi bạn có thể tự giải thích ít nhất 5/6 câu.

## 2. Mục tiêu đầu ra

Sau buổi này, bạn có thể:

- Phân biệt `list`, `tuple`, `set` và `dict`.
- Chọn cấu trúc dữ liệu phù hợp với bài toán.
- Truy cập, thêm, sửa và xóa phần tử trong `list` và `dict`.
- Dùng slicing để lấy một phần của chuỗi hoặc danh sách.
- Dùng `set` để loại giá trị trùng nhau.
- Viết list comprehension đơn giản, dễ đọc.
- Đếm tần suất nhãn loài trong danh sách tên file bằng `dict`.

## 3. `list` – danh sách có thứ tự

`list` phù hợp khi cần lưu nhiều giá trị theo thứ tự và có thể thay đổi chúng.

```python
animals = ["cat", "dog", "tiger"]

print(animals[0])   # cat
print(animals[-1])  # tiger
```

Chỉ số bắt đầu từ `0`. Chỉ số âm đếm từ cuối danh sách.

### Thêm, sửa và xóa

```python
animals.append("elephant")
animals[1] = "wolf"
animals.remove("cat")
```

- `append(value)`: thêm một phần tử vào cuối.
- Gán qua chỉ số: thay đổi một phần tử.
- `remove(value)`: xóa lần xuất hiện đầu tiên của giá trị.

## 4. Slicing – lấy một phần dữ liệu

Cú pháp chung:

```python
values[start:stop:step]
```

`stop` không được lấy, tương tự `range()`.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[::2])   # [10, 30, 50]
print(numbers[::-1])  # [50, 40, 30, 20, 10]
```

Slicing cũng dùng được với chuỗi:

```python
file_name = "cat_001.jpg"
print(file_name[:-4])  # cat_001
```

## 5. `tuple` – dãy giá trị không thay đổi

`tuple` có thứ tự như `list`, nhưng không thể sửa trực tiếp sau khi tạo.

```python
image_size = (1920, 1080)
width, height = image_size

print(width)   # 1920
print(height)  # 1080
```

Nên dùng `tuple` khi một nhóm giá trị có cấu trúc cố định, ví dụ kích thước `(width, height)` hoặc tọa độ `(x, y)`.

## 6. `set` – tập hợp không trùng lặp

`set` chỉ giữ các giá trị duy nhất. Không nên dựa vào vị trí của phần tử trong `set`.

```python
labels = ["cat", "dog", "cat", "tiger", "dog"]
unique_labels = set(labels)

print(unique_labels)
print(len(unique_labels))  # 3
```

Thêm và kiểm tra phần tử:

```python
unique_labels.add("wolf")

if "cat" in unique_labels:
    print("Có nhãn cat")
```

## 7. `dict` – ánh xạ khóa sang giá trị

Mỗi phần tử của `dict` gồm một `key` và một `value`.

```python
animal_counts = {
    "cat": 3,
    "dog": 2,
    "tiger": 1,
}

print(animal_counts["cat"])  # 3
```

Trong bài đếm tần suất:

- Khóa là nhãn loài.
- Giá trị là số lần nhãn xuất hiện.

### Cập nhật số đếm

```python
animal_counts = {}

for label in ["cat", "dog", "cat"]:
    if label not in animal_counts:
        animal_counts[label] = 0

    animal_counts[label] += 1

print(animal_counts)  # {'cat': 2, 'dog': 1}
```

Có thể viết gọn bằng `get()`:

```python
animal_counts[label] = animal_counts.get(label, 0) + 1
```

`get(label, 0)` trả về giá trị hiện tại; nếu khóa chưa tồn tại thì trả về `0`.

### Duyệt `dict`

```python
for label, count in animal_counts.items():
    print(label, count)
```

## 8. Chọn cấu trúc nào?

| Cấu trúc | Có thứ tự | Thay đổi được | Cho phép trùng | Dùng khi |
|---|---:|---:|---:|---|
| `list` | Có | Có | Có | Cần một dãy giá trị có thứ tự |
| `tuple` | Có | Không | Có | Nhóm giá trị cố định |
| `set` | Không dùng vị trí | Có | Không | Cần giá trị duy nhất hoặc kiểm tra thành viên |
| `dict` | Theo thứ tự thêm | Có | Khóa không trùng | Cần ánh xạ `key -> value` |

Với bài đếm nhãn, `dict` phù hợp hơn `list` vì ta có thể truy cập trực tiếp số đếm bằng tên nhãn:

```python
counts["bengal_tiger"]
```

## 9. List comprehension

List comprehension tạo một danh sách mới từ một dãy có sẵn.

Vòng lặp thông thường:

```python
squares = []

for number in range(1, 6):
    squares.append(number ** 2)
```

Viết bằng comprehension:

```python
squares = [number ** 2 for number in range(1, 6)]
```

Có thể thêm điều kiện:

```python
even_squares = [number ** 2 for number in range(1, 6) if number % 2 == 0]
```

Chỉ nên dùng comprehension khi biểu thức vẫn ngắn và dễ đọc. Nếu có nhiều điều kiện hoặc nhiều bước xử lý, vòng lặp thông thường sẽ rõ hơn.

## 10. Bài thực hành có hướng dẫn

Mở tệp `animal_labels.py` trong thư mục Buổi 4.

Danh sách mẫu:

```python
file_names = [
    "cat_001.jpg",
    "dog_001.jpg",
    "cat_002.jpg",
    "bengal_tiger_001.jpg",
    "dog_002.jpg",
    "bengal_tiger_002.jpg",
]
```

Quy ước tên file:

```text
<tên_loài>_<số_thứ_tự>.jpg
```

Tên loài có thể chứa dấu gạch dưới, ví dụ `bengal_tiger`.

### Mức 1 – Tách nhãn từ tên file

Hoàn thiện hàm:

```python
def extract_label(file_name):
    pass
```

Ví dụ mong đợi:

```python
assert extract_label("cat_001.jpg") == "cat"
assert extract_label("bengal_tiger_001.jpg") == "bengal_tiger"
```

Gợi ý:

1. Kiểm tra tên file kết thúc bằng `.jpg`.
2. Bỏ phần mở rộng `.jpg`.
3. Dùng `split("_")` để tách các phần.
4. Phần cuối là số thứ tự; ghép các phần còn lại bằng `"_".join(...)`.
5. Nếu tên file không đúng định dạng, phát sinh `ValueError`.

### Mức 2 – Lấy danh sách nhãn

Hoàn thiện hàm sau bằng vòng lặp, sau đó thử viết lại bằng list comprehension:

```python
def extract_labels(file_names):
    pass
```

Hàm phải trả về một `list` mới và không thay đổi `file_names`.

### Mức 3 – Tìm các nhãn duy nhất

Hoàn thiện:

```python
def find_unique_labels(file_names):
    pass
```

Hàm trả về một `set` chứa các nhãn không trùng lặp.

### Mức 4 – Đếm tần suất nhãn

Hoàn thiện:

```python
def count_labels(file_names):
    pass
```

Kết quả mong đợi với danh sách mẫu:

```python
{
    "cat": 2,
    "dog": 2,
    "bengal_tiger": 2,
}
```

Không dùng `list.count()` để đếm lại toàn bộ danh sách cho từng nhãn. Hãy duyệt danh sách một lần và cập nhật `dict`.

### Mức 5 – Kiểm thử

Tạo ít nhất 6 test case, bao gồm:

1. Nhãn một từ: `cat_001.jpg`.
2. Nhãn nhiều từ: `bengal_tiger_001.jpg`.
3. Danh sách có nhãn trùng nhau.
4. Danh sách chỉ có một file.
5. Danh sách rỗng.
6. Tên file sai định dạng phải gây ra `ValueError`.

## 11. Cách tự kiểm chứng

Chạy tệp:

```powershell
py -X utf8 "Bat dau Module 1 - Buoi 4\animal_labels.py"
```

Sau đó kiểm tra:

- Chương trình kết thúc mà không có `AssertionError`.
- `bengal_tiger_001.jpg` được tách thành `bengal_tiger`, không phải `bengal`.
- Danh sách rỗng trả về `{}` khi đếm nhãn.
- Tên file sai định dạng gây ra `ValueError`.
- Danh sách ban đầu không bị thay đổi.
- Bạn có thể giải thích vì sao `dict` phù hợp với bài đếm.

## 12. Tiêu chí hoàn thành

Bạn hoàn thành Buổi 4 khi:

- [ ] Phân biệt được `list`, `tuple`, `set` và `dict`.
- [ ] Truy cập đúng phần tử bằng chỉ số và slicing.
- [ ] Dùng `set` để lấy các nhãn duy nhất.
- [ ] Viết được list comprehension đơn giản.
- [ ] Tách đúng nhãn một từ và nhãn có dấu gạch dưới.
- [ ] Đếm đúng tần suất nhãn bằng `dict`.
- [ ] Giải thích được vì sao dùng `dict` thay vì `list` trong bài đếm.
- [ ] Chương trình từ chối tên file sai định dạng bằng `ValueError`.
- [ ] Có ít nhất 6 test case, gồm trường hợp bình thường, biên và không hợp lệ.
- [ ] Tự giải thích được phần mã mình viết.

## 13. Câu hỏi tự kiểm tra

1. `list` khác `tuple` ở điểm quan trọng nào?
2. Kết quả của `[10, 20, 30, 40][1:3]` là gì?
3. Vì sao `set` thích hợp để tìm các nhãn duy nhất?
4. Trong `dict`, `key` và `value` của bài đếm nhãn là gì?
5. `counts.get(label, 0)` trả về gì khi `label` chưa tồn tại?
6. List comprehension khác vòng lặp `for` thông thường như thế nào?
7. Vì sao không thể chỉ lấy phần trước dấu `_` đầu tiên của `bengal_tiger_001.jpg`?
8. Vì sao việc duyệt một lần và cập nhật `dict` tốt hơn gọi `list.count()` cho từng nhãn?

## 14. Bài tập về nhà

Mở rộng chương trình để xử lý danh sách tên ảnh dạng:

```text
bengal_tiger_001.jpg
african_elephant_002.jpg
red_fox_003.jpg
```

Yêu cầu:

- Kiểm tra phần mở rộng phải là `.jpg`.
- Kiểm tra số thứ tự gồm đúng 3 chữ số.
- Chuyển nhãn thành dạng dễ đọc, ví dụ `bengal_tiger` thành `Bengal Tiger`.
- Trả về `dict` đếm số file của từng loài.
- Tìm loài có nhiều file nhất mà không dùng `max()`.
- Có ít nhất 8 test case.
- Viết 3–5 dòng nhật ký: lỗi đã gặp, cách sửa và điều còn chưa chắc.

Không chuyển sang Buổi 5 chỉ vì đã đọc xong. Chỉ chuyển khi các tiêu chí ở Mục 12 đã được kiểm chứng.
