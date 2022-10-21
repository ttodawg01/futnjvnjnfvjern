class Gather_info():
    # def __init__(self):
       

    def first_input(self):
        name = input('What is your name? ')
        print(f'Hey {name} Were going to learn code foreal this time! ')

    def living(self):
        question = input('what do you want to do to make bread? ')
        print(f'{question}')


player = Gather_info.living('hey')

print(player)
