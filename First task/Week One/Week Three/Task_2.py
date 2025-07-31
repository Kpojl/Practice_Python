def hex2int(hex_char):
    hex_char = hex_char.upper()
    if hex_char in '0123456789ABCDEF':
        return int(hex_char, 16)
    else:
        print("Ошибка: недопустимый символ в шестнадцатеричном числе")
        return None

def int2hex(num):
    if 0 <= num <= 15:
        return format(num, 'X')
    else:
        print("Ошибка: число должно быть от 0 до 15")
        return None

print(hex2int('B'))   
print(hex2int('c'))   
print(int2hex(9))    
print(int2hex(7))    