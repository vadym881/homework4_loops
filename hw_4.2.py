'hw_4.2'
list1 = [0, 1, 7, 2, 4, 8]
# list1 = [1, 3, 5]
# list1 = [6]
# list1 = []

if not list1:
    result = 0
else:
    sum_even_index = sum(list1[el] for el in range(0, len(list1), 2))
    result = sum_even_index * list1[-1]

print(f'{list1} -> {result}')