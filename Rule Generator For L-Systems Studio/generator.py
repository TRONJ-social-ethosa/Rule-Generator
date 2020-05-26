from random import choice

chars = list("+-[]{}<>fF|*/")
axiom_chars = list("fFxyz+-")
axiom = ''
expression = ''

while True:
    choose = input('[A]xiom or [R]ule: ')

    if choose.upper() == 'A':
        count = input('Enter a number of chars: ')

        # axiom generator
        if count.isdigit() and int(count) <= 50:

            for i in range(int(count)):
                if choice(axiom_chars) in '+-' and i == 1:
                    pass
                else:
                    axiom += choice(axiom_chars)

            # save file with axiom
            choose2 = input('Save in file? [Y] or [N] ').upper()
            if choose2 == 'Y':

                path = input(r'Enter a path to save: ')
                with open(path, 'w') as file:
                    file.write(axiom)

            elif choose2 == 'N':
                pass
        else:
            print('Number of chars more than 50')
            pass

    elif choose.upper() == 'R':
        count = input('Enter a number of chars: ')

        # rule generator
        if count.isdigit():

            for i in range(int(count)):
                expression += choice(chars)

            # save file with fractal
            choose2 = input('Save in file? [Y] or [N] ').upper()
            if choose2 == 'Y':

                path = input(r'Enter a path to save: ')
                with open(path, 'w') as file:
                    file.write(expression)

            elif choose2 == 'N':
                pass