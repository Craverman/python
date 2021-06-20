array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(array):
    if array[i].isdigit() or array[i][1:].isdigit():
        array.insert(i, '"')
        i += 1
        array.insert(i + 1, '"')
        i += 1
    else:
        i += 1

for el in range(len(array)):
    if '+' in array[el]:
        array[el] = array[el].zfill(3)
    elif '5' in array[el]:
        array[el] = array[el].zfill(2)
print(' '.join(array))
