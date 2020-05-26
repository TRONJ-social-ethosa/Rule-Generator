from random import choice

chars = list("+-[]{}<>fxfxfyfyFzFzF|*/")
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
                if choice(axiom_chars) in list('+-') and i == 1:
                    pass
                else:
                    axiom += choice(axiom_chars)

            # save file with axiom
            path = input(r'Enter a path to save: ')
            with open(path, 'w') as file:
                file.write(axiom)
                file.close()
        else:
            print('Number of chars more than 50')
            pass

    elif choose.upper() == 'R':
        count = input('Enter a number of chars: ')

        # rule generator
        if count.isdigit():

            for i in range(int(count)):
                if choice(chars) in list('+-[]{}|*/') and i == 1:
                    pass
                else:
                    expression += choice(chars)

            # save file with fractal
            path = input(r'Enter a path to save: ')
            with open(path, 'w') as file:
                file.write(expression)
                file.close()