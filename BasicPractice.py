# iq = 100
# user_age = iq / 5

# augmented assignment operator

# some_value = 5
# some_value *= 5

# print(some_value)

# print(type("hi hey their 34"))
# username = 'supercoder'
# password = 'supersecret'
# long_string = '''
# WOW
# O O
# ---
# '''

# print(long_string)

#string concatanation
# print(type(int(str(100))))

#escape sequence
# weather = 'it\'s sunny'
# print(weather)

# weather = "\t It's \"kind of\" sunny \n hope you had a good day"
# print(weather)


# FORMATTED STRINGS
# name = 'Johnny'
# age = 55

# print("hi {new_name}, you are  {age} years old".format(new_name = 'sally', age=9000))


# #STRING INDEXES  IMMUTABILITY
# selfish = '01234567'
# # [start:stop:stepover]
# print(selfish[::-1])

# #strings are immutable you have to completely re assign the value

# selfish = selfish + str(8)
# print(selfish)


# BUILT-IN FUNCTIONS + METHODS

# str()
# quote = 'to be or not to be'
# quote2 = quote.replace('be', 'me')

# print(quote)
# print(quote2)


#BOOLEANS
# True or False
# name = 'Tony'
# is_cool = False

# is_cool = True
# print(bool('True'))


# #EXERCITE: TYPE CONVERSION
# birth_year = input("What year were you born? ")
# age = 2022 - int(birth_year)
# print(f"your age is {age}")


#DEVELOPER FUNDAMENTALS
#commenting you code with a pound sign or hashtag sign


#EXERCITE PASSWORD CHECKER
# username = input("What is your username? ")
# password = input("What is your password? ")

# length = len(password)

# hidden = '*' * length

# print(f"{username}, your password {hidden} is {length} letters long.")


#LISTS

# amazon_cart = ['notebooks', 'sunglasses']
# print(amazon_cart[1])


#LIST SLICING
# amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

# amazon_cart[0] = 'laptop'
# new_cart = amazon_cart[:]
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)


#MATRIX
# multi dimensional lists
# matrix = [
#     [1,2,3],
#     [2,4,6],
#     [7,8,9]
# ]
# print(matrix[0][1])


#LIST METHODS
# basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
# # add

# # new_list = basket.extend([100])
# # print(new_list)
# basket.sort()
# basket.reverse()
# # print(basket[::-1])
# # print(basket)


# new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'jojo'])
# print(new_sentence)



#LIST UNPACKING
# a,b,c, *other, d= [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)


#NONE
# weapons = None
# print(weapons)


#DICTIONARY
# user = {
#     'basket':[1,2,3],
#     'greet':'hello',
#     'age':20
# }

# print(user.update({'age':55}))
# print(user)


#TUPLES immutable****** usually faster then lists
# my_tuple = (1,2,3,4,5,5)

# print(len(my_tuple))



#SET unorder collections of unique 
# my_set = {1,2,3,4,5,5}
# new_copy = my_set.copy()
# my_set.clear()
# print(new_copy)
# print(my_set)

# from turtle import update


# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}

# # print(my_set.difference(your_set))

# # my_set.discard(5)
# # print(my_set)

# my_set.difference_update(your_set)
# print(my_set)



