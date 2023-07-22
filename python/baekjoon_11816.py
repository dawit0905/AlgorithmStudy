# import sys
#
#
# s = sys.stdin.readline().strip()
# if s[0:2] == '0x':
#     print(int(s[2:], 16))
# elif s[0] == '0':
#     print(int(s[1:], 8))
# else:
#     print(int(s))


def convert_to_decimal(x):
    decimal_value = 0
    if x[0:2] == '0x':  # Hexadecimal format
        num = x[2:]  # Remove the '0x' prefix
        hex_digits = "0123456789abcdef"

        for i in range(len(num)):
            digit = num[i]
            decimal_value += hex_digits.index(digit) * (16 ** (len(num) - i - 1))

    elif x[0] == '0':  # Octal format
        num = x[1:]  # Remove the '0' prefix
        for i in range(len(num)):
            digit = int(num[i])
            decimal_value += digit * (8 ** (len(num) - i - 1))

    else:  # Decimal format
        for i in range(len(x)):
            digit = int(x[i])
            decimal_value += digit * (10 ** (len(x) - i - 1))

    return decimal_value

# Read input from the user
x = input().strip()

# Convert and print the result
result = convert_to_decimal(x)
print(result)
