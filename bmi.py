name = input("Tên của bạn: ")
print(f"Xin chào {name}!")
weight = float(input("Cân nặng của bạn:")) # Nhập cân nặng
height = float(input("Chiều cao của bạn:")) # Nhập chiều cao
#Tính toán bmi
def calculate_bmi(weight, height):
  # if height <= 0:
  #   return "Chiều cao không hợp lệ"
  # if weight <= 0: 
  #   return "Cân nặng không hợp lệ"
  # return round(weight/(height ** 2), 2)
  if weight <= 0:
    raise ValueError("Cân nặng phải lớn hơn 0")
  if height <= 0:
    raise ValueError("Chiều cao phải lớn hơn 0")
  return round(weight/ (height ** 2), 2)
#Phân loại bmi
def classify_bmi(bmi):
  if bmi < 18.5:
    return "Gầy"
  if bmi <= 22.9:
    return "Lí tưởng"
  if bmi <= 24.9:
    return "Thừa cân"
  if bmi <= 29.9:
    return "Béo phì độ I"
  if bmi >= 30:
    return "Béo phì độ II"
  #Thực thi chương trình

def runtest(weight, height):
  try: 
    bmi = calculate_bmi(weight, height);
    print(f"Chỉ số BMI của bạn: {bmi}")
    print(f"Trạng thái của bạn: {classify_bmi(bmi)}")
  except ValueError as e:
    print(f"Dữ liệu không hợp lệ: {e}")
if __name__ == "__main__":
  runtest(weight, height)