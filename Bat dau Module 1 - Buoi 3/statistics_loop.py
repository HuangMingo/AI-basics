def calculate_total(values):
  if not values:
    raise ValueError
  total = 0
  for value in values:
    total += value;
  return total
def calculate_mean(values):
  if not values:
    raise ValueError
  sum = calculate_total(values)
  n = len(values)
  return sum / n
def find_minimum(values):
  if not values:
    raise ValueError
  min = values[0]
  for i in values:
    if i < min: 
      min = i
  return min
def find_maximum(values):
  if not values:
    raise ValueError
  max = values[0]
  for i in values:
    if i > max:
      max = i
  return max

def assert_raises_value_error(function, values):
  try:
    function(values)
  except ValueError:
    return
  raise AssertionError("Expected ValueError")

n = int(input("Nhap so n: "))
values = []

try:
  if n == 0:
    raise ValueError()
  for i in range(n):
    x = int(input())
    values.append(x)
  print(f"Tong cua mang: {calculate_total(values)}")
  print(f"mean: {calculate_mean(values)}")
  print(f"min: {find_minimum(values)}")
  print(f"max: {find_maximum(values)}")
  assert calculate_total([1, 2, -3]) == 0
  assert calculate_total([1]) == 1
  assert find_minimum([4, 2, 2]) == 2
  assert find_maximum([4, 2, 3]) == 4
  assert calculate_mean([1, 2, 3]) == 2
  assert_raises_value_error(calculate_mean, [])

except ValueError:
  print("Dữ liệu không hợp lệ")
