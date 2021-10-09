import random

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
    new_byte = bin(int.from_bytes(b.encode('ascii'), 'big')).replace("0b", "")
    bytes.append(new_byte)

# Reverting binary numbers back to ASCII characters for demonstrative purposes.
for byte in bytes:
    byte_int = int(byte, 2)
    output_data = str(byte_int.to_bytes(1, 'big').decode('ascii'))
    output_list.append(output_data)

# Randomly determining the number of bytes that will be "interfered" with.
number_byte_errors = random.randint(0, len(output_list) / 2)

# Copying the list of original bytes to serve as a basis for the bytes to be modified later.
new_bytes_list = bytes.copy()

# Creating a loop that alters a random byte each time it is run.
for iter in range(1, number_byte_errors):

    # Randomly selecting the number of bits that will be changed in this specific byte.
    number_bit_errors = random.randint(1, 2)
    print("-------------------------------------")
    print("\nNumber of random bit errors to occur = " + str(number_bit_errors))

    # Randomly selecting the index of the byte that will be changed.
    rand_index = random.randint(0, len(new_bytes_list) - 1)
    list_occupant = new_bytes_list[rand_index].replace("0b", "")

    print("\nSelected byte: " + list_occupant)

    # Creating a loop that changes a random bit each time it is run.
    for bit_iter in range(1, number_bit_errors + 1):

        # Randomly selecting the index of the bit that will be changed.
        rand_bit_index = random.randint(0, 5)
        print("\nRandom bit index = " + str(rand_bit_index) + ", with a value of " + list_occupant[rand_bit_index])

        # Changing the value of the bit depending on its current value.
        if list_occupant[rand_bit_index] == "0":
            list_occupant = list_occupant[:rand_bit_index] + "1" + list_occupant[(rand_bit_index + 1):]
            print("\nCurrent altered byte value = " + str(list_occupant))
            new_bytes_list[rand_index] = list_occupant

        elif list_occupant[rand_bit_index] == "1":
            list_occupant = list_occupant[:rand_bit_index] + "0" + list_occupant[(rand_bit_index + 1):]
            print("\nCurrent altered byte value = " + str(list_occupant))
            new_bytes_list[rand_index] = list_occupant

# Displaying a summary of all the data.
print("\n-------------------------------------")
print("Transmitted binary data = " + ' '.join(bytes))
print("Received binary data =    " + ' '.join(new_bytes_list))

for byte in new_bytes_list:
    byte_int = int(byte, 2)
    output_data = str(byte_int.to_bytes(1, 'big').decode('ascii'))
    output_ascii.append(output_data)

print("\nTransmitted ASCII data = " + ''.join(output_list))
print("Received ASCII data = " + ''.join(output_ascii))
print("\n")

with open("transmitted_data.txt", 'w') as td:
    td.write(' '.join(new_bytes_list))
    td.close()
