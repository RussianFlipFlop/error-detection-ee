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

# Writing new data, now in binary and with parity bytes, to a new file.
with open("binary_data.txt", 'w') as td:
    td.write(' '.join(new_data))
    td.close()
