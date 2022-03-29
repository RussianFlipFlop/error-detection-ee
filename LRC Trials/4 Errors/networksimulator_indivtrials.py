import random

# Creating lists for storing our bytes.
bytes = []

# Manually setting the number of trials.
trials = 500

# Inputted data from file.
with open("binary_data.txt") as f:
    input_data = f.read()
    f.close()

# Converting ASCII characters to binary numbers.
bytes = list(input_data.split(" "))

# Creating loop to run through each trial file.
for trial in range(0, trials):

    # Creating a new list which is an exact copy of the original list.
    new_bytes_list = bytes.copy()

    # Manually selecting the number of errors to be introduced.
    number_of_errors_final = 4

    # Creating a loop which introduces a single random error every time it is looped.
    for error_round in range(number_of_errors_final):

        # Randomly determining the index of the byte in which the error will occur.
        error_byte_ind = random.randint(0, len(bytes) - 1)

        # Randomly determining the index of the bit that will be corrupted.
        error_bit_ind = random.randint(0, 7)

        error_byte = bytes[error_byte_ind]

        # Ensuring a "corruption", or change in values, depending on the bits's current value.
        if error_byte[error_bit_ind] == "0":
            error_byte = error_byte[:error_bit_ind] + "1" + error_byte[(error_bit_ind + 1):]
            new_bytes_list[error_byte_ind] = error_byte

        elif error_byte[error_bit_ind] == "1":
            error_byte = error_byte[:error_bit_ind] + "0" + error_byte[(error_bit_ind + 1):]
            new_bytes_list[error_byte_ind] = error_byte


    # Displaying a summary of all the data.
    print("\n-------------------------------------")
    print("Transmitted binary data = " + ' '.join(bytes))
    print("Received binary data =    " + ' '.join(new_bytes_list))

    trial_file_name = "transmitted_data_" + str(trial) + ".txt"

    # Writing new list of bytes (now with errors) back to individual trial files.
    with open(trial_file_name, 'w') as td:
        td.write(' '.join(new_bytes_list))
        td.close()
