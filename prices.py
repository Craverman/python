original_list = [59.2, 97.3, 12.4, 56, 72, 32.45, 58, 21, 22.3, 15.45, 17.74, 75]
original_list.sort()
down_list = original_list[::-1]
top5_list = original_list[-5:len(original_list):1]

def money(prices):
    i = 0
    while i < len(prices):
        if type(prices[i]) == float:
            prices[i] = str(prices[i])
            a, b = prices[i].split('.')
            if len(b) < 2:
                b = ('0' + b)
                prices[i] = (str(a) + ' руб ' + str(b) + ' коп ')
            else:
                prices[i] = (str(a) + ' руб ' + str(b) + ' коп ')
                i = i + 1
        elif type(prices[i]) == int:
            prices[i] = (str(prices[i]) + ' руб')
        else:
            i = i + 1
    return prices

print(money(original_list))
print(money(down_list))
print(money(top5_list))










