from random import choice

chars = list("+-[]{}<>fF|*/")
expression = ''

count = input('Enter a number of chars: ')

# generate expression
if count.isdigit():

    for i in range(int(count)):
        expression += choice(chars)

print(expression)
# save file with fractal
choose = input('Save in file? [Y] or [N] ').upper()
if choose == 'Y':

    path = input(r'Enter a path to save: ')
    with open(path, 'a') as file:
        file.write(expression)

elif choose == 'N':
    pass
