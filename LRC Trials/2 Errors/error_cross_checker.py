# Manually setting number of trials.
trials = 500

# Setting variables for total summation of incorrect and correct error detects across all trials.
incorrect_detects = 0
correct_detects = 0

# Creating loop to run through each trial file, and to compare the calculated parity with the transmitted parity.
for trial in range(0, trials):
    current_file = "transmitted_data_" + str(trial) + ".txt"

    errors_detected = 0
    errorless_bytes = 0

    # Opening specific trial file.
    with open(current_file) as td:
        transmitted_data = td.read()
        td.close()

    # Inserting all bytes from file into a list.
    error_parity_data = list(transmitted_data.split(" "))
    #print(error_parity_data)

    # Determining the number of "blocks" (equivalent to 4 bytes of original data transmitted + 1 parity byte).
    number_of_blocks = int((len(error_parity_data) - (len(error_parity_data) / 5)) / 4)
    #print("NUMBER OF BLOCKS: " + str(number_of_blocks))

    # Creating a loop to run through each individual block and calculate a parity.
    for block_run in range(0, number_of_blocks):

        provided_parity_byte_index = (4 * (block_run + 1)) + block_run
        provided_parity_byte = list(error_parity_data[provided_parity_byte_index])

        calculated_parity_byte = [0, 0, 0, 0, 0, 0, 0, 0]

        # Creating a loop to run through each byte and calculate a parity byte.
        for x in range((block_run * 5), (block_run * 5 + 4)):
            #print("BYTE INDEX: " + str(x))
            for y in range(0, 8):
                current_byte = error_parity_data[x]
                calculated_parity_byte[y] += int(current_byte[y])
                #print(calculated_parity_byte)

        for digit in range(0, 8):
            if calculated_parity_byte[digit] % 2 == 0:
                calculated_parity_byte[digit] = "0"
            else:
                calculated_parity_byte[digit] = "1"

        # Converting the calculated parity block from an integer list to a string list - in order to compare to the transmitted parity byte later.
        for bit in range(0, len(calculated_parity_byte)):
            calculated_parity_byte[bit] = str(calculated_parity_byte[bit])

        # Summing up the number of errors detected.
        if provided_parity_byte != calculated_parity_byte:
            errors_detected += 1
        elif provided_parity_byte == calculated_parity_byte:
            errorless_bytes += 1

    #print("Number of Errors: " + str(errors_detected))
    #print("Number of Checked Bytes: " + str(errorless_bytes))

    # Adding to total count of incorrect/correct error detects (i.e. if the number of errors is set to 10, and only 9 are detected, this counts as an incorrect error detect).
    if errors_detected == 2:
        correct_detects += 1
    else:
        incorrect_detects += 1

# Outputting compiled data to a single file.
with open("testing_file.txt", 'w') as td:
    td.write("Number of incorrect detects: " + str(incorrect_detects))
    td.write("\nNumber of correct detects: " + str(correct_detects))
    td.close()
