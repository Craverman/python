numbers = int(input('Введите число '))
while numbers < 21:
    if numbers == 1:
        print(numbers, 'процент')
    elif 1 < numbers <= 4:
        print(numbers, 'процента')
    elif 4 < numbers <= 20:
        print(numbers, 'процентов')
    break
print()

for el in range(1, 21):
    if el == 1:
        print(el, 'процент')
    elif 1 < el <= 4:
        print(el, 'процента')
    elif 4 < el <= 20:
        print(el, 'процентов')



