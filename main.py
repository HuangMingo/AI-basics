name = input("Tên của bạn: ")
print(f"Xin chào {name}!")
weight = float(input("Cân nặng của bạn:"))
height = float(input("Chiều cao của bạn:"))
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
try: 
  bmi = calculate_bmi(weight, height);
  print(f"Chỉ số BMI của bạn: {bmi}")
except ValueError as e:
  print(f"Dữ liệu không hợp lệ: {e}")
