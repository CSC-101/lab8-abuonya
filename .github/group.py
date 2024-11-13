# TASK 1
# DESIGN RECIPE
    # Purpose of Function: takes list[int] as a parameter and groups the elements of the input list into groups of three values. Returns a nested list.
    # Input: [1,2,3,4,5,6,7,8,9] --> list[int]  #Output Given Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] --> list[list[int]]

def groups_of_3(given_list: list[int]) -> list[list[int]]:
    tempr_list = []  # initialize an empty list to store groups of 3 in.

    for x in range(0,len(given_list), 3):
        tempr_list.append(given_list[x:x+3])
        print(tempr_list)

    return tempr_list

