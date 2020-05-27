from random import choice
import re

chars = list("+-[]{}<>fxfxfyfyFzFzF|*/")
axiom_chars = list("fFxyz+-")
axiom = ''
expression = ''

while True:
    choose = input('[A]xiom [R]ule: ')

    if choose.upper() == 'A':
        count = input('Enter a number of chars: ')

        # axiom generator
        if count.isdigit() and int(count) <= 50:

            for i in range(int(count)):
                if choice(axiom_chars) in list('+-') and i == 1:
                    pass
                else:
                    axiom += choice(axiom_chars)
            print(axiom)
            # save file with axiom
            path = input(r'Enter a path to save: ')
            with open(path, 'w') as file:
                file.write(axiom)
                file.close()
        else:
            print('Number of chars more than 50')
            pass

    elif choose.upper() == 'R':
        axiom_rule = input('Rule for special axiom? [Y] or [N]: ')
        if axiom_rule.upper() == 'Y':
            chars2 = list("+-[]{}<>ffffFFFF|*/")
            special_axiom = input('Enter axiom: ')
            count = input('Enter a number of chars: ')
            special_axiom_chars = re.findall(r"[\d\w]", special_axiom)
            chars2 = chars2 + special_axiom_chars
            axiom_rule_helper = ''
            # rule generator
            if count.isdigit():

                for i in range(int(count)):
                    if choice(chars2) in list('+-[]{}|*/') and i == 1:
                        pass
                    else:
                        expression += choice(chars2)
                print(expression)
                for i in special_axiom_chars:
                    axiom_rule_helper += str(i + "\n")

                # save file with special fractal
                path = input(r'Enter a path to save: ')
                with open(path, 'w') as file:
                    file.write(axiom_rule_helper)
                    file.close()
        elif axiom_rule.upper() == 'N':
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