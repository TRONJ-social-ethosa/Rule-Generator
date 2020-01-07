import random

chars = ['+','-',']','[','}','{','>','<','f','F','|','*','/']
expression = ''

count = input('Enter a number of chars: ')

# generate expression
if count.isdigit():

    for i in range(int(count)):
        char = random.choice(chars)
        char += expression

print(expression)
# save file with fractal
choose = input('Save in file? [Y] or [N] ')
if choose.upper() == 'Y':

    path = input(r'Enter a path to save: ')
    with open(path, 'a') as file:
        file.write(expression)

elif choose.upper() == 'N':
    pass
