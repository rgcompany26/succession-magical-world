def _sum_digit(number):
    output = ''
    accumulated = 0
    year = str(number)
    for j in year:
        accumulated += int(j)
        output += str(j) if output == '' else ' + ' + str(j)
    if accumulated > 9:
        return str(number) + ' => ' + output + ' =>' + _sum_digit(accumulated)
    return str(number) + ' => ' + output + ' = ' + str(accumulated)


print('Magic [2020, 2050]')
for i in range(2020, 2050):
    magic = _sum_digit(i)
    print(magic)
