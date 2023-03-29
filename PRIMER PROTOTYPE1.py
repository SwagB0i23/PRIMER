# WELCOME TO PRIMER! THIS PROGRAM IS SIMILAR TO HMNDB BUT INSTEAD OF COUNTING divisibilty, it counts the prime-ability of a number list.
print('               WELCOME TO PRIME CHECKER')
print('\n\n               INPUT A NUMBER AND IT WILL LIST (AND COUNT) ALL PRIME NUMBERS THAT COME BEFORE IT')


def count_primes(num):

    """BACKBONE OF PRIMER"""

    prime_list = [2]

    primer = 3

    while primer <= int(num):
        for primes in prime_list:
            if primer%primes == 0:
                primer += 2
                break
        else:
            prime_list.append(primer)

    return prime_list

def inputnum():
    return input('\n\nPlease enter number to check: ')

def display():
    print(f'\n\nPRIME NUMBER LIST:\n\n{to_display}')
    print(f'\n\nTOTAL PRIME NUMBER COUNT: {len(to_display)}\n\n')

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    ',10:'    *'}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4],'F':[4,9,5,9,9],'G':[4,9,4,3,4],'J':[10,10,10,3,4]}
    for pattern in alphabet[letter.upper()]:
        print(f'{patterns[pattern]}')

def prevclose():
    prevclose_input = input('\n\n                        PLEASE PRESS ANY KEY TO EXIT:')
    return prevclose_input

num = inputnum()

to_display = count_primes(num)

display()

prevclose()

c = print_big('c')
j = print_big('j')
