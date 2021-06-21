def thesaurus(*names):
    name_list = {}
    for el in names:
        key = el[0].capitalize()
        if key not in name_list:
            name_list[key] = []
        name_list[key].append(el)
    return name_list
print(thesaurus('Mariya', 'Vlad', 'Petr', 'Michael', 'Joseph', 'Victor'))