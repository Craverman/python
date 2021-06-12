seconds = int(input('Пожалуйста, укажите желаемое время в секундах: '))
years = seconds // 31536000  # Делим значение на количество секунд в одном году
seconds -= (years * 31536000)  # Вычитаем из секунд количество лет в секундах, остаток переходит в месяцы и т.д.
month = seconds // 2628000
seconds -= (month * 2628000)
days = seconds // 86400
seconds -= (days * 86400)
hours = seconds // 3600
seconds -= (hours * 3600)
minutes = seconds // 60
seconds -= (minutes * 60)
if years == 0 and month == 0 and days == 0 and hours == 0 and minutes == 0:
    print(seconds, 'сек')
elif years == 0 and month == 0 and days == 0 and hours == 0:
    print(minutes, ' мин ', seconds, ' sec ')
elif years == 0 and month == 0 and days == 0:
    print(hours, ' час ', minutes, ' мин ', seconds, ' sec ')
elif years == 0 and month == 0:
    print(days, ' дн ', hours, ' час ', minutes, ' мин ', seconds, ' sec ')
elif years == 0:
    print(month, ' мес ', days, ' дн ', hours, ' час ', minutes, ' мин ', seconds, ' sec ')
elif years > 0:
    print(years, ' лет ', month, ' мес ', days, ' дн ', hours, ' час ', minutes, ' мин ', seconds, ' sec ')

