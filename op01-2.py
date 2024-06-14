from datetime import datetime

def calculate_age_in_months(age):
    return age * 12

def calculate_age_in_days(age):
    return age * 365

def calculate_age_in_hours(age):
    return age * 365 * 24

name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))

months = calculate_age_in_months(age)
days = calculate_age_in_days(age)
hours = calculate_age_in_hours(age)

print(f"Привет, {name}! Тебе {age} лет.")
print(f"Ты прожил(а) примерно {months} месяцев, {days} дней и {hours} часов.")
