'hw_4.3'
import random

my_list = [random.randint(0, 10) for i in range(random.randint(3, 10))]
new_list = [my_list[0], my_list[2], my_list[-2]]
print(f'{my_list} -> {new_list}')
