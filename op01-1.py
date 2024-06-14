def calculator(num1, num2):
  addition = num1 + num2
  subtraction = num1 - num2
  multiplication = num1 * num2
  division = num1 / num2
  integer_division = num1 // num2
  remainder = num1 % num2
  exponentiation = num1 ** num2

  return addition, subtraction, multiplication, division, integer_division, remainder, exponentiation

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

result = calculator(num1, num2)
print(f"Сложение: {result[0]}")
print(f"Вычитание: {result[1]}")
print(f"Умножение: {result[2]}")
print(f"Деление: {result[3]}")
print(f"Целая часть от деления: {result[4]}")
print(f"Остаток от деления: {result[5]}")
print(f"Возведение в степень: {result[6]}")
