# TASK 1
# DESIGN RECIPE
    # Purpose of Function: takes list[int] as a parameter and groups the elements of the input list into groups of three values. Returns a nested list.
    # Input: [1,2,3,4,5,6,7,8,9] --> list[int]  #Output Given Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] --> list[list[int]]

def groups_of_3(input: list[int]) -> list[list[int]]:
    tempr_list = []  # intialize an empty list to store groups of 3 in.