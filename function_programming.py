# my_list = [1,2,3]
# your_list = [10, 20, 30]
# their_list = [5, 4, 3]
# def multiply_by2(item):
#     return item*2

# print(list(map(multiply_by2, my_list)))   #using map()
# print(my_list)


# def check_if_odd(item):
#     return item % 2 != 0

# # def 

# print(list(zip(my_list, your_list, their_list)))  # zip created a tuple
# # print(my_list)


# from functools import reduce

# my_list = [1,2,3]

# def multiply_by2(item):
#     return item*2

# def only_odd(item):
#     return item % 2 != 0

# def accumalator(acc, item):
#     print(acc, item)
#     return acc + item

# print(reduce(accumalator, my_list, 10))
# print(my_list)








# from functools import reduce
# from operator import truediv

#1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']

# def cap(ok):
#     for i in ok:
#         return i.capitalize()

# print(list(map(cap, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]

# x = my_strings, my_numbers

# print(list(zip(my_strings, sorted(my_numbers))))
# print(x)

# def Reverse(x):
#     new_tup = x[::-1]
#     return new_tup
# print(Reverse(tuple(x)))



#3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]

# def greater_50(item):
#     # for i in item:
#     if item >= 50:
#         return True
#     else:
#         return None
# print(list(filter(greater_50, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). 
# What is the total?
# scores = [73, 20, 65, 19, 76, 100, 88]
# my_numbers = [5,4,3,2,1]
# # combining a list of integers
# # we need a function with data SCORES and NUMBERS


# def total(x, y):
#     return sum(scores + my_numbers)

# # print(reduce(total, scores, my_numbers))

# def accumulator(acc, item):
#     return acc + item

# # print(reduce(accumulator, (my_numbers + scores)))








# lambda expressions

# from functools import reduce
# from operator import truediv

# my_list = [1,2,3,4,5,6,7,8]
# def multiply_by2(item):
#     return item * 2

# print(list(map(lambda item: item*2, my_list)))
# print(list(filter(lambda item: item % 2 == 0, my_list)))
# print(reduce(lambda acc, item: acc + item, my_list))

# # lambda param: action(param)



# my_list = [5,4,3]

# new_list = list(map(lambda x:x **2, my_list)) GOT THIS ONE RIGHT MANE
# print(new_list)

# # list sorting
# a = [(0,2), (4,3), (9,9), (10, -1)]

# a.sort(key=lambda x:x[1])
# print(a)

# new_a = list(filter( lambda y: y [1:2:2], a))
# print(new_a)