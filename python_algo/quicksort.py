'''
quicksort Guillaume THOMAS
from MIT Pseudo code
'''
from random import randint

def quicksort(lst):

    def quicksort_h(lst, p, r):
        if p < r:
            q = partition_h(lst, p, r)
            quicksort_h(lst, p, q - 1)
            quicksort_h(lst, q + 1, r)

    def partition_h(lst, p, r):

        piv = lst[r]
        i = p - 1
        for j in range(p, r):
            if lst[j] <= piv:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[r] = lst[r], lst[i + 1]
        return i + 1

    quicksort_h(lst, 0, len(lst) -1)

if __name__ == "__main__":
    lst = [randint(0, 20) for _ in range(10)]
    print(lst)
    quick(lst)
    print(lst)
