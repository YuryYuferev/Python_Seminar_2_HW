# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

# Сложение
def add_fractions(fraction1, fraction2):
    result = fraction1 + fraction2
    return result
# Умножение
def multiply_fractions(fraction1, fraction2):
    result = fraction1 * fraction2
    return result


fraction1_str = input("Введите первую дробь в формате 'a/b': ")
fraction2_str = input("Введите вторую дробь в формате 'a/b': ")

numerator1, denominator1 = map(int, fraction1_str.split('/'))
numerator2, denominator2 = map(int, fraction2_str.split('/'))

fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)

sum_result = add_fractions(fraction1, fraction2)
product_result = multiply_fractions(fraction1, fraction2)

print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)

# Чтобы проверить правильность работы программы, можно использовать методы класса `Fraction`:


fraction1 = Fraction(3, 4)  # Для проверки вводим те же значения "a/b", как при вводе вначале задачи.
fraction2 = Fraction(1, 2)  # Для проверки вводим те же значения "a/b", как при вводе вначале задачи.

sum_result = fraction1 + fraction2
product_result = fraction1 * fraction2

print("Проверка: Сумма дробей:", sum_result)
print("Проверка: Произведение дробей:", product_result)
