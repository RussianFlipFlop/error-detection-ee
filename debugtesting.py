import numpy as np

def bin_poly_division(dividend, divisor):
    divisor_list = []
    dividend_list = []

    for x in range(0, len(divisor)):
        divisor_list.append(int(divisor[x]))
    for x in range(0, len(dividend)):
        dividend_list.append(int(dividend[x]))

    a = np.poly1d(divisor_list)
    b = np.poly1d(dividend_list)

    quotient = list(np.polydiv(b,a)[0])
    remainder = list(np.polydiv(b,a)[1])

    for x in range(0, len(quotient)):
        current_bit = quotient[x]
        if current_bit % 2 == 0:
            quotient[x] = 0
        elif current_bit % 2 == 1:
            quotient[x] = 1

    for x in range(0, len(remainder)):
        current_bit = remainder[x]
        if current_bit % 2 == 0:
            remainder[x] = 0
        elif current_bit % 2 == 1:
            remainder[x] = 1

    return quotient, remainder

print(bin_poly_division("1011011011100100000", "110101")[0])
print(bin_poly_division("1011011011100100000", "110101")[1])
