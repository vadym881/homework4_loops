'hw_4.1'
# list1 = [0, 1, 0, 12, 3]
# list1 = [0]
# list1 = [1, 0, 13, 0, 0, 0, 5]
list1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

non_zero_elements = [num for num in list1 if num != 0]
zero_elements = [num for num in list1 if num == 0]
list1 = non_zero_elements + zero_elements

print(list1)