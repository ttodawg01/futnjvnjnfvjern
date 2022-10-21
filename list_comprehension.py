# param for param in iterable

# my_list = {char for char in 'hello'}
# my_list2 = [number for number in range(0,100)]
# my_list3 = [num**2 for num in range(0,100)]
# my_list4 = {num**2 for num in range(0,100) if num % 2 ==0}

# print(my_list4)


# print([char for char in 'hello'])
# simple_dict = {
#     'a':1,
#     'b':2
# }

# my_dict = {num:num*2 for num in [1,2,3]}

# print(my_dict)

from multiprocessing.reduction import duplicate


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = [x for x in some_list if some_list.count(x) >= 2]
# print(duplicates)

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)