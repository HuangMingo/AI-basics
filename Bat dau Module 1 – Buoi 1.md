# Bắt đầu Module 1 – Buổi 1

## Python và tư duy giải bài toán AI

**Thời lượng đề xuất:** 120 phút  
**Sản phẩm cuối buổi:** Chương trình tính BMI có kiểm tra đầu vào và ít nhất 5 test case.

## 1. Kiểm tra đầu buổi

Trước khi học, hãy tự trả lời:

1. Bạn đã cài Python 3.12 trở lên chưa?
2. Bạn đang dùng VS Code, PyCharm hay công cụ khác?
3. Bạn có thể mở terminal và chạy `python --version` không?
4. Bạn đã từng chạy một tệp `.py` chưa? Rồi

Nếu chưa hoàn thành các bước trên, hãy thiết lập môi trường trước khi làm bài thực hành.

## 2. Mục tiêu đầu ra

Sau buổi học, bạn cần:

- Mô tả được vị trí của Python trong một bài toán AI.
- Chạy được tệp `.py` và phân biệt lỗi cú pháp với lỗi khi chương trình đang chạy.
- Sử dụng được biến, số, chuỗi, `input()`, `print()` và f-string.
- Viết được chương trình tính BMI có kiểm tra đầu vào cơ bản.
- Tự kiểm chứng chương trình bằng ít nhất 5 test case.

## 3. Python trong một hệ thống AI

Một hệ thống AI tối thiểu thường có bốn phần:

1. **Nhận dữ liệu:** ảnh, văn bản, số liệu hoặc dữ liệu cảm biến.
2. **Tiền xử lý:** làm sạch, chuẩn hóa và chuyển dữ liệu thành dạng số.
3. **Mô hình:** học quy luật từ dữ liệu hoặc sử dụng mô hình đã huấn luyện.
4. **Đánh giá và sử dụng:** đo chất lượng, phát hiện lỗi và đưa kết quả vào ứng dụng.

Python thường được dùng vì cú pháp dễ đọc và có hệ sinh thái như NumPy, pandas, scikit-learn và PyTorch. Trong Module 1, mục tiêu chưa phải là huấn luyện mô hình lớn mà là xây nền tảng để đọc dữ liệu, tính toán đúng và kiểm thử được.

## 4. Tư duy Input → Process → Output

Trước khi viết code, hãy trả lời ba câu hỏi:

- **Input:** Dữ liệu đầu vào là gì? Đơn vị nào?
- **Process:** Công thức hoặc quy tắc xử lý là gì?
- **Output:** Kết quả cần có dạng nào? Điều kiện nào xác định kết quả đúng?

Ví dụ bài toán BMI:

- Input: cân nặng theo kg và chiều cao theo m.
- Process: `BMI = cân nặng / chiều cao²`.
- Output: chỉ số BMI được làm tròn đến 2 chữ số thập phân.

BMI chỉ là một chỉ báo sàng lọc, không phải kết luận hoặc chẩn đoán y khoa.

## 5. Chương trình Python đầu tiên

```python
name = input("Tên của bạn: ")
print(f"Xin chào, {name}!")
```

`input()` luôn trả về một chuỗi. Khi cần tính toán, phải chuyển dữ liệu sang `int` hoặc `float`.

```python
weight = float(input("Cân nặng (kg): "))
height = float(input("Chiều cao (m): "))

bmi = weight / (height ** 2)

print(f"BMI = {bmi:.2f}")
```

Trong đoạn mã trên:

- `float(...)` chuyển chuỗi người dùng nhập thành số thực.
- `height ** 2` là bình phương chiều cao.
- `{bmi:.2f}` hiển thị kết quả với 2 chữ số thập phân.

## 6. Kiểm tra dữ liệu đầu vào

Chương trình chạy với dữ liệu hợp lệ vẫn chưa đủ. Chiều cao bằng 0 gây lỗi chia cho 0; cân nặng hoặc chiều cao âm không hợp lệ.

Tách công thức thành một hàm giúp chương trình dễ đọc và dễ kiểm thử:

```python
def calculate_bmi(weight, height):
    if weight <= 0:
        raise ValueError("Cân nặng phải lớn hơn 0")
    if height <= 0:
        raise ValueError("Chiều cao phải lớn hơn 0")

    return weight / (height ** 2)
```

Xử lý dữ liệu nhập không hợp lệ:

```python
try:
    weight = float(input("Cân nặng (kg): "))
    height = float(input("Chiều cao (m): "))
    result = calculate_bmi(weight, height)
    print(f"BMI = {result:.2f}")
except ValueError as error:
    print(f"Dữ liệu không hợp lệ: {error}")
```

Không nên dùng `except:` trống vì nó che giấu nguyên nhân thật của lỗi.

## 7. Tự kiểm chứng bằng test case

Mỗi test case cần có:

- Input.
- Output mong đợi.
- Kết quả thực tế.
- Kết luận đạt hoặc không đạt.

Hai trường hợp hợp lệ:

```python
assert round(calculate_bmi(57, 1.67), 2) == 20.44
assert round(calculate_bmi(70, 1.75), 2) == 22.86
```

Kiểm tra trường hợp không hợp lệ:

```python
def expect_value_error(weight, height):
    try:
        calculate_bmi(weight, height)
    except ValueError:
        return True
    return False


assert expect_value_error(-57, 1.67)
assert expect_value_error(57, 0)
assert expect_value_error(57, -1.67)
```

Các test trên kiểm tra 5 trường hợp: 2 trường hợp bình thường và 3 trường hợp không hợp lệ.

## 8. Bài thực hành 45 phút

### Mức 1

Viết chương trình nhập cân nặng, chiều cao và in BMI với 2 chữ số thập phân.

### Mức 2

Từ chối số không, số âm và dữ liệu không chuyển được thành số. Thông báo phải giúp người dùng hiểu mình nhập sai ở đâu.

### Mức 3

Viết hàm `classify_bmi(bmi)` theo bộ ngưỡng do giảng viên cung cấp. Kết quả chỉ dùng cho bài tập lập trình, không được mô tả như một chẩn đoán sức khỏe.

### Mức 4

Tạo ít nhất 5 test case, trong đó có ít nhất 2 trường hợp không hợp lệ.

## 9. Tiêu chí hoàn thành

Bạn hoàn thành Buổi 1 khi:

- [ ] Chạy được chương trình từ tệp `bmi.py`.
- [ ] Giải thích được Input, Process và Output của bài toán.
- [ ] Giải thích được `input()`, `float()`, `**`, `raise` và `try/except`.
- [ ] Chương trình từ chối cân nặng hoặc chiều cao không hợp lệ.
- [ ] Có ít nhất 5 test case và tất cả đều chạy đúng.
- [ ] Tự giải thích được phần mã mình viết, không chỉ sao chép.

## 10. Câu hỏi tự kiểm tra

1. `input()` trả về kiểu dữ liệu gì? String
2. `=` và `==` khác nhau như thế nào? = để gán giá trị còn == để so sánh liệu có bằng nhau không
3. Vì sao `height ** 2` khác `height * 2`? một cái là lũy thừa bậc 2 một cái là phép nhân
4. Vì sao nên đưa công thức BMI vào một hàm riêng? Để tái sử dụng
5. Nếu một đoạn code do AI tạo ra chạy được, điều đó đã đủ chứng minh code đúng chưa? Vì sao? Chưa. Vì có thể sai

## 11. Bài tập về nhà

Tạo tệp `bmi.py` đáp ứng các yêu cầu:

- Có hàm `calculate_bmi(weight, height)`.
- Từ chối số không, số âm và dữ liệu không chuyển được thành số.
- In kết quả với 2 chữ số thập phân.
- Có ít nhất 5 test case; ghi output mong đợi trong comment.
- Cuối tệp có 3–5 dòng nhật ký: lỗi đã gặp, cách sửa và điều còn chưa chắc.

## 12. Nhật ký học tập

Sau khi hoàn thành, điền ngắn gọn:

- Điều tôi đã hiểu: 
- Lỗi tôi đã gặp:
- Nguyên nhân của lỗi:
- Cách tôi sửa lỗi:
- Điều tôi còn chưa chắc:
