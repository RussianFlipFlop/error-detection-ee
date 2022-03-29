# Importing NumPy
import numpy as np

divisor = "101101"
crc_length = len(divisor) - 1

trials = 500

# Setting variables for total summation of incorrect and correct error detects across all trials.
incorrect_detects = 0
correct_detects = 0

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


for trial in range(0, trials):
    current_file = "transmitted_data_" + str(trial) + ".txt"

    print("Trial: " + str(trial))
    # Inputted data from text file.
    with open(current_file) as f:
        input_data = f.read()
        f.close()

    blocks = list(input_data.split(" "))

    # Determining the number of blocks and bytes.
    block_divisions = int(len(blocks))
    #print("BLOCK DIVISIONS: " + str(block_divisions))

    # Creating a new list which is an exact copy of the original list.
    new_data = blocks.copy()

    errors_detected = 0
    errorless_bytes = 0

    for block_run in range(0, block_divisions):
        current_block = new_data[block_run]
        current_dividend = current_block[0:(len(current_block) - crc_length)]
        #print(current_dividend)

        quotient = bin_poly_division(current_dividend, divisor)[0]
        remainder = bin_poly_division(current_dividend, divisor)[1]

        if len(remainder) != 5:
            for x in range(0, 5 - len(remainder)):
                remainder.insert(0, 0)

        transmitted_remainder_str = "".join(str(current_block[(len(current_block) - crc_length):len(current_block)]))
        remainder_str = "".join([str(int) for int in remainder])
        #print("Transmitted: "+ transmitted_remainder_str)
        #print("Calculated: " + remainder_str)

        if transmitted_remainder_str == remainder_str:
            errorless_bytes += 1
        else:
            errors_detected += 1

    if errors_detected == 2:
        correct_detects += 1
    else:
        incorrect_detects += 1

    #print(errorless_bytes)
    #print(errors_detected)
    #print(incorrect_detects)
    #print(correct_detects)


with open("result_file.txt", 'w') as td:
    td.write("Number of incorrect detects: " + str(incorrect_detects))
    td.write("\nNumber of correct detects: " + str(correct_detects))
    td.close()
