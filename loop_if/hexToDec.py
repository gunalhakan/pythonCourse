def hex_to_decimal(hex_num):
    decimal_num = 0
    hex_digits = '0123456789ABCDEF'
    hex_num = hex_num.upper()
    for digit in hex_num:
        print()
        print(hex_digits.index(digit))
        decimal_num = 16 * decimal_num + hex_digits.index(digit)
    return decimal_num

hex_input = input("Lütfen 16'lık sayı sistemindeki bir sayı girin (örn: 1A): ")
if len(hex_input) != 2:
    print("Lütfen iki basamaklı bir 16'lık sayı girin.")
else:
    try:
        decimal_output = hex_to_decimal(hex_input)
        print("10'luk sayı sistemindeki karşılığı:", decimal_output)
    except ValueError:
        print("Geçersiz giriş. Lütfen 16'lık bir sayı girin.")
