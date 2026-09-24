def classify_score(score):
    if score < 0 or score > 10:
        return "Không hợp lệ"
    if score >= 0 and score < 5.0: 
        return 'Chưa đạt'
    elif not(score >= 7.0):
        return "Trung bình"
    elif score < 8.5:
        return "Khá"
    elif score <= 10:
        return "Giỏi"

try: 
    name = input("Nhap ten: ")
    diem = float(input("Nhap diem: "))

    if diem < 0 or diem > 10:
        raise ValueError("Không hợp lệ")
    print(f"Diem cua {name}: {diem}")
    print(f"Xếp loại: {classify_score(diem)}")
except ValueError:
    print("Dữ liệu không hợp lệ")

if __name__ == "__main__":
    assert classify_score(9) == "Giỏi"
    assert classify_score(8.5) == "Giỏi"
    assert classify_score(5.0) == "Trung bình"
    assert classify_score(-2.0) == "Không hợp lệ"
    assert classify_score(11.0) == "Không hợp lệ"

