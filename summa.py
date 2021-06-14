def sum_digits(value): #создаём функцию для подсчёта суммы цифр
    result = 0
    while value != 0:
        result += value % 10
        value //= 10

    return result

cubes = []
cubes_2 = []
for el in range(1001): #создаём кубы нечетных чисел
    if el % 2 != 0:
        cubes.append(el**3)

sum = 0 #контейнер для хранения суммы цифр
for el in cubes:
    if sum_digits(el) % 7 == 0: #отсеиваем только те, что кратны 7
        sum += el
print('Сумма цифр, кратных 7 =', sum)

sum = 0
for el in cubes:
    if sum_digits(el + 17) % 7 == 0: #прибавляем 17 и снова отсеиваем
        sum += el
print('Сумма цифр + 17, кратных 7 =', sum)


