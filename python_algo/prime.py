from math import sqrt
from functools import reduce


def prime_factor(numb):
    n = numb
    lst = []

    while n % 2 == 0:
        n = n / 2
        lst.append(2)

    boolean = True
    k = int(sqrt(n))
    f = 3
    while boolean:
        if n % f == 0:
            lst.append(f)
            n = n / f
            k = int(sqrt(n))
            f = 3

        f += 2
        if f > k:
            boolean = False

    if lst != []:
        res = reduce(lambda x, y: x * y, lst)
        if res != numb:
            lst.append(int(n))
    else:
        lst.append(int(n))

    return(lst)


def display_prime(numb):
    lst = prime_factor(numb)
    if len(lst) > 1:
        lst_str = [str(i) for i in lst]
        factors = ', '.join(lst_str)
        str_l = '{} has the following prime factors {}'.format(numb, factors)
    else:
        str_l = '{} is prime'.format(numb)
    return str_l


if __name__ == "__main__":
    '''
    'print(prime_factor(8))
    'print(prime_factor(9))
    'print(prime_factor(163))
    'print(prime_factor(164))
    '''
    print(display_prime(11))
    print(display_prime(13147))
    print(display_prime(17297))
    print(display_prime(2893))
    print(display_prime(19453))
