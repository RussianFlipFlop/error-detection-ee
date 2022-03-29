# Importing NumPy
import numpy as np

# Creating lists for storing our bytes.
bytes = []

trials = 500

# Inputted data from text file.
with open("input_message.txt") as f:
    input_data = f.read()
    f.close()

# Converting ASCII characters to binary numbers.
for b in input_data:
    new_byte = bin(int.from_bytes(b.encode('ascii'), 'big')).replace("0b", "0")

    # Making sure each byte is displayed as 8 bits long.
    if len(new_byte) < 8:
        ztba = 8 - len(new_byte)
        new_byte = "0" * ztba + new_byte
    bytes.append(new_byte)

# Ensuring that the number of bytes can be divided up into blocks of 4.
if len(bytes) % 4 != 0:
    byte_fillers = 4 - (len(bytes) % 4)
    for extra_byte in range(0, byte_fillers):
        bytes.append("00000000")

# Determining the number of blocks and bytes.
block_divisions = int(len(bytes) / 4)
print("BLOCK DIVISIONS: " + str(block_divisions))
number_of_bytes = len(bytes)
print("NUMBER OF BYTES: " + str(number_of_bytes))

# Creating a new list which is an exact copy of the original list.
new_data = []

# Combining every 4 bytes into a single block, for CRC calculation.
for space in range(0, block_divisions):
    new_data.append(bytes[space * 4] + bytes[(space * 4) + 1] + bytes[(space * 4) + 2] + bytes[(space * 4) + 3])

divisor = "101101"

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



for block_run in range(0, block_divisions):
    current_block = new_data[block_run]

    quotient = bin_poly_division(current_block, divisor)[0]
    remainder = bin_poly_division(current_block, divisor)[1]

    if len(remainder) != 5:
        for x in range(0, 5 - len(remainder)):
            remainder.insert(0, 0)

    #print(remainder)
    remainder_str = "".join([str(int) for int in remainder])

    new_data[block_run] = new_data[block_run] + remainder_str

print(new_data)


# Writing new data, now in binary and with parity bytes, to a new file.
with open("binary_data.txt", 'w') as td:
    td.write(' '.join(new_data))
    td.close()
