from random import choice
import re

# functions

def axiomGenerate():

    # initialize variables
    chars = list("+-[]{}<>fxfxfyfyFzFzF|*/")
    axiom_chars = list("fFxyz+-")
    axiom = ''
    rule = ''

    count = input('Enter a number of chars: ')

    # axiom generator
    if count.isdigit() and int(count) <= 50:
        for i in range(int(count)):
            random_char = choice(axiom_chars)
            if random_char not in '+-' or i != 1:
                axiom += random_char

        # save file with axiom
        path = input(r'Enter a path to save: ')
        with open(path, 'w') as file:
            file.write(axiom)
    else:
        print('Number of chars more than 50')

def specialRuleGenerator():

    # initialize variables
    chars = list("+-[]{}<>fxfxfyfyFzFzF|*/")
    axiom_chars = list("fFxyz+-")
    axiom = ''
    rule = ''
    chars2 = list("+-[]{}<>ffffFFFF|*/")
    special_axiom = input('Enter axiom: ')
    count = input('Enter a number of chars: ')

    # create new chars list
    special_axiom_chars = re.findall(r"[\d\w]", special_axiom)
    chars2 = chars2 + special_axiom_chars
    axiom_rule_helper = ''

    # special rule generator
    if count.isdigit():
        for i in range(int(count)):
            random_char = choice(chars2)
            if random_char not in '+-[]{}|*/' or i != 1:
                rule += random_char

        for i in special_axiom_chars:
            axiom_rule_helper += str(i + "\n")

        # save file with special fractal
        path = input(r'Enter a special fractal path to save: ')
        with open(path, 'w') as file:
            file.write(rule)

        # save file with axiom helper
        path = input(r'Enter a axiom helper path to save: ')
        with open(path, 'w') as file:
            file.write(axiom_rule_helper)

def ruleGenerator():
    # initialize variables
    chars = list("+-[]{}<>fxfxfyfyFzFzF|*/")
    axiom_chars = list("fFxyz+-")
    axiom = ''
    rule = ''
    count = input('Enter a number of chars: ')

    # rule generator
    if count.isdigit():
        for i in range(int(count)):
            random_char = choice(chars)
            if random_char not in '+-[]{}|*/' or i != 1:
                rule += random_char

        # save file with fractal
        path = input(r'Enter a path to save: ')
        with open(path, 'w') as file:
            file.write(rule)

# main cycle
def main():
    while True:
        choose = input('[A]xiom [R]ule: ')

        if choose.upper() == 'A':
                axiomGenerate()

        elif choose.upper() == 'R':
            axiom_rule = input('Rule for special axiom? [Y] or [N]: ')

            if axiom_rule.upper() == 'Y':
                specialRuleGenerator()

            elif axiom_rule.upper() == 'N':
                ruleGenerator()

if __name__ == '__main__':
    main()