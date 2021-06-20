names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = [s.split() for s in names]
for i in range(len(names)):
    print('Привет,', names[i][-1].title())





