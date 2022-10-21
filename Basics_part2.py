#CONDITIONAL LOGIC

# is_old = True
# is_licensed = True

# if is_old and is_licensed:
#     print("you are old enough to drive! and you have a license")
# else:
#     print("you are not of age")

# print('okok')



#TERNARY OPERATOR ONE LINERRRR!!!

# condition_if_true if condition else condition_if_else

# is_friend = False
# can_message = 'message allowed' if is_friend else 'not allowed to message'
# print(can_message)



#SHORT CIRCUITING

# is_friend = True
# is_user = True

# if is_friend or is_user:
#     print("Bestfriends forever")



#LOGICAL OPERATORS

# print(1 != 0)

# print(not(1 == 1))

# Exercise time

# is_magician = False
# is_expert = True

# #check if magician and expert: 'you are a mester magician'

# #check if magician but not expert: 'at least your getting their'

# #check if your not a magician: 'you need magic powers'

# if is_magician and is_expert:
#     print('you are a master magician')
    
# elif is_magician and not is_expert:
#     print('at least your getting their')
# else:
#     print("you need magic powers")



# is vs ==

# is checks if the location in memory is the same
# print(10 is 10)
# print([] is [])
# print('' is '')



#FOR LOOPS

# for item in (1,2,3,4,5):
#     for x in ['a', 'b', 'c']:
#         print(item, x)




#ITERABLES
# list, dictionary, tuple , set , string
# go one by one to check each item in the collection

# users = {'name':'Goldem', 'age':5006, 'can_swim':False}

# for key,value in users.items():
#     print(key,value)

# for item in users.values():
#     print(item)

# for item in users.keys():
#     print(item)



#EXERCICE TRICKY COUNTER


# my_list = [1,2,3,4,5,6,7,8,9,10]
# counter = 0 
# for i in my_list:
#     counter = counter + i
#     print(counter)



#RANGE()

# print(range(0, 100))

# for _ in range(2):
#     print(list(range(0,10)))



#ENUMERATE()
# for i,character in enumerate(list(range(0,100))):
#     if character == 50:
#         print(f'The index of 50 is {i}')



#WHILE LOOPS
# i = 0
# while i < 50:
#     print(i)
#     i += 1
# else:
#     print('done with all the work')

# my_list = [1,2,3]
# for item in [1,2,3]:
#     print(item)
#     continue

# i = 0
# while True:
#     response = input('say something ')
#     i += 1
#     break




#OUR FIRST GUI


#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', 
# and the 1 is going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# #iterate over picture
#     #if its a 0 print ''
#     #if 1 print '*'
# for row in picture:
#     for pixel in row:
#         if pixel == 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')





# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicate = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicate:
#             duplicate.append(value)

# print(duplicate)




#FUNCTIONS
#PARAMETERS


# def say_hello(name='Darth vador', emoji='devil'):
#     print(f'hello {name} {emoji}')

# say_hello('Tony', 'Smiley')
# say_hello('Teddy', 'Smiley')
# say_hello('Ruby', 'Smiley')
# say_hello(emoji='angry', name ='caca')
# say_hello()



#RETURN

# def sum(num1, num2):
#     return num1 + num2

# total = 15
# print(sum(10, total))

# def sum(num1, num2):
#     def another_func(n1, n2):
#         return n1 + n2
#     return another_func(num1, num2)

# total = sum(10, 20)
# print(total)

# equal = another_func('2', '3')





#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, 
# you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, 
# so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

# def checkDriverAge(age=0):
#     # age = input("What is your age?: ")

#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!")
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")

# checkDriverAge(20)



#DOCTSTRINGS

# def test(a):
#     '''
#     Info: This function test and prints param a
#     '''
#     print(a)

# test('!!')
# # test(a)
# print(help(test))



#CLEAN CODE

# def is_even(num):
#     return num % 2 == 0

# print(is_even(51))



#ARGS AND KAWRGSS


# def super_func(*args, **kwargs):
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total

# print(super_func(1,2,3,4,5, num1=5, num2 = 10))



# def highest_even(li):
#     for i in li:
#         if i % 2 == 0:
#             return i

# print(highest_even([10,2,3,4,8,11,14]))


# def highest_even(li):
#     even = []
#     for item in li:
#         if item % 2 == 0:
#             even.append(item)
#     return max(even)

# print(highest_even([10,2,3,4,8,11,14]))




#WALRUS OPERATOR 

# a = 'hellooooooooooo'

# if ((n := len(a)) > 10):
#     print(f'Too long {n} elements')

# while ((n := len(a)) > 1):
#     print(n)
#     a = a[:-1]

# print(a)



#SCOPE what variables do i have access too

# def some_func():
#     total = 100

# print(total)



# a = 10 
# def confusion():
#     a = 5
#     return a

# print(confusion())
# print(a)


# total = 0

# def count():
#     global total 
#     total += 1
#     return total

# count()
# count()
# print(count())

