# TASK 2
    # Purpose of Function: takes a single command-line argument and reads every line in a text file consisting of two float values.
    # For each line, convert the float values and print their sum.
import sys


def read_all_file():
    command_line_input = sys.argv[1]
    with open(command_line_input, "r") as test_file:
        tempr_list = []
        for line in test_file:
            split_contents = line.strip().split()
            try:
                x = float(split_contents[0])
                y = float(split_contents[1])
                total_sum = x + y
                tempr_list.append(total_sum)
                print(total_sum)

            except ValueError:
                print("Error - an inputted value could not be processed.")

        return tempr_list

if __name__ == "__main__":
    test = read_all_file()
    print("Completed processing.")