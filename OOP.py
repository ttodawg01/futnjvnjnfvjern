# class PlayerCharacter:
#     membership = True #Class object attribute

#     def __init__(self, name, age):
#         self.name = name #attributes
#         self.age = age

#     def shout(self):
#         print(f'My name is {self.name}')

#     @classmethod
#     def adding_things(cls, num1, num2):
#         return num1 + num2

#     @staticmethod
#     def adding_things(cls, num1, num2):
#         return cls('teddy', num1 + num2)

# player1 = PlayerCharacter('Tom', 10)

# player3 = PlayerCharacter.adding_things(2, 3)

# print(player3.age)






#Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         if (age > 18 ):
            
#             self.name = name
#             self.age = age

#     def old(self):
#         return f"The Oldest cat is {self.age} years old"


# cat1 = Cat('Teddy', 5)
# cat2 = Cat('Ruby', 10)
# cat3 = Cat('Edgar', 25)

# print(cat3.old())
# 1 Instantiate the Cat object with 3 cats



# 2 Create a function that finds the oldest cat



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2




# class PlayerCharacter:

#     def __init__(self, name, age):
#         self._name = name #attributes
#         self._age = age

#     def run(self):
#         print('run')

#     def speak(self):
#         print(f"My name is {self._name} and I am {self._age} years old.")

# player1 = PlayerCharacter('tony', 100)
# player1.name = '!!!'
# player1.speak = 'BOO'

# print(player1.speak)






# class User():
#     def sign_in(self):
#         print("logged in")

#     def attack(self):
#         print("do nothing")

# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         User.attack(self)
#         print(f"attacking with power of {self.power}")

# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f"attacking with arrows: arrows left - {self.num_arrows}")

# wizard1 = Wizard('Merlin', 60)
# archer1 = Archer('robin', 30)

# print(wizard1.attack())






# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Tony(Cat):
#     def sing(self, sounds):
#         return f"{sounds}"

# my_cats = [Simon, Sally, Tony]

# # print(Simon.walk(my_cats))

# cat1 = Tony('Tony', 7)
# print(cat1.walk())
# print(cat1.sing())

#1 Add nother Cat

#2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = []

#3 Instantiate the Pet class with all your cats use variable my_pets

#4 Output all of the cats walking using the my_pets instance










# class User():

#     def sign_in(self):
#         print("logged in")

# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f"attacking with power of {self.power}")

# class Archer(User):
#     def __init__(self, name, arrows):
#         self.name = name
#         self.arrows = arrows

#     def check_arrows(self):
#         print(f"{self.arrows} remaining")

#     def run(self):
#         print('ran really fast')

# class HybridBorg(Wizard, Archer):
#     def __init__(self, name, power, arrows):
#         Archer.__init__(self, name, arrows)
#         Wizard.__init__(self, name, arrows)


# hb1 = HybridBorg('borgie', 50, 100)
# print(hb1.sign_in())


# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.my_dict = {
#             'name':'yoyo',
#             'has_pets': False
#         }

#     def __str__(self):
#         return f"{self.color}"

#     def __len__(self):
#         return 5

#     def __call__(self):
#         return 'yesss?'

#     def __getitem__(self, i):
#         return self.my_dict[i]


# action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))

# print(action_figure.__len__())
# print(action_figure())

# print(action_figure['name'])





# class SuperList(list):
#     def __len__(self):
#         return 1000



# superlist1 = SuperList()
# print(len(superlist1))
# superlist1.append(5)
# print(superlist1[0])
# print(issubclass(SuperList, list))






# class A:
#     num = 10

# class B(A):
#     pass

# class C(A):
#     num = 1

# class D(B, C):
#     pass

# print(D.num)