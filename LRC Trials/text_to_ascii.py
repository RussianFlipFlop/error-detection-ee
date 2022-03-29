# Creating lists for storing our bytes.
bytes = []
output_list = []
output_ascii = []

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
new_data = bytes.copy()

# Creating a loop to run through each BLOCK and calculate the parity of the 4 contained bytes.
for block_run in range(0, block_divisions):
    print("BLOCK RUN " + str(block_run))
    print("------------------------------")
    parity_block = [0, 0, 0, 0, 0, 0, 0, 0]

    # Creating a loop to run through each byte and calculate a parity byte.
    for x in range((block_run * 4), (block_run * 4) + 4):
        print("X IS EQUAL TO " + str(x))
        for y in range(0, 8):
            current_byte = bytes[x]
            parity_block[y] += int(current_byte[y])
            print(parity_block)

    for digit in range(0, 8):
        if parity_block[digit] % 2 == 0:
            parity_block[digit] = "0"
        else:
            parity_block[digit] = "1"

    # Determining the index at which the parity byte has to be inserted - and inserting it there.
    insertion_index = (4 * (block_run + 1)) + block_run
    new_data.insert(insertion_index, ''.join(parity_block))

# Writing new data, now in binary and with parity bytes, to a new file.
with open("binary_data.txt", 'w') as td:
    td.write(' '.join(new_data))
    td.close()
