# TASK 2
    # Purpose of Function: takes a single command-line argument and reads every line in a text file consisting of two float values.
    # For each line, convert the float values and print their sum.

def read_all_file():
    with open("test_file", "r") as test_file:
        tempr_list = []
        for line in test_file:
            split_contents = tempr_list.append(line.strip().split())
        print(split_contents)

        try:
            x = float(split_contents[0])
            y = float(split_contents[1])
            sum = x+y
            print(sum)
            return sum

        except ValueError:
            print("Error - an inputted value could not be processed.")



read_all_file()