'''
Bubble sort
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html

Bubble sort, sometimes referred to as sinking sort, is a simple sorting
algorithm that repeatedly steps through the list to be sorted,
compares each pair of adjacent items and swaps them if they are in the
wrong order. The pass through the list is repeated until no swaps are
needed, which indicates that the list is sorted. The algorithm, which is
a comparison sort, is named for the way smaller or larger elements "bubble"
to the top of the list. Although the algorithm is simple, it is too slow and
impractical for most problems even when compared to insertion sort.
Bubble sort can be practical if the input is in mostly sorted order with
some out-of-order elements nearly in position.

'''


def bubble_sort(lst):
    swap = True
    while swap:
        swap = False
        for i in range(1, len(lst)):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                print(lst)
                swap = True
        print('end loop')
    return lst


if __name__ == "__main__":
    lst = [1, 2, 5, 3, 9, 4, 15, 23, 8, 12]
    a = bubble_sort(lst)
    print(a)
