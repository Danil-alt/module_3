def get_multiplied_digits(n):
    n = int(n)
    str_n = str(n)
    first = int(str_n[0])
    while str_n.endswith('0'):
        str_n = str_n[:len(str_n) - 1]
    if len(str_n) > 1:
        return first * get_multiplied_digits(int(str_n[1:]))
    else:
        return first


num = input('Введите число: ')
print(f'Произведение цифр числа {num}:', get_multiplied_digits(num))
