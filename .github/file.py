# TASK 2
    # Purpose of Function: takes a single command-line argument and reads every line in a text file consisting of two float values.
    # For each line, convert the float values and print their sum.

def read_all_file():
    with open("test_file", "r") as test_file:
        for line in test_file:
            split_contents = line.strip().split()
            try:
                print(split_contents)
                x = float(split_contents[0])
                y = float(split_contents[1])
                total_sum = x + y
                print(total_sum)
                return total_sum

            except ValueError:
                print("Error - an inputted value could not be processed.")

read_all_file()