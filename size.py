import os
size_list = []
size_dictionary = {0:0, 100:0, 1000:0, 100000:0}
dir_path = 'C:/Users/crave/PycharmProjects'
for (dirpath, dirnames, filenames) in os.walk(dir_path):
    for f in filenames:
        f_path = os.path.join(dirpath, f)
        f_size = os.path.getsize(f_path)
        size_list.append(f_size)

for el in size_list:
    if el > 0 and el <= 100:
        size_dictionary[0] += 1
    elif el > 100 and el <= 1000:
        size_dictionary[100] += 1
    elif el > 1000 and el <= 100000:
        size_dictionary[1000] += 1

print(size_dictionary)