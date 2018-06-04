'''
Insertion sort algo
O(n2)
In Place (no need for extra storage)
'''


def insertion_sort(lst):
    i = 1
    # looping with position 
    while i < len(lst):
        j = i
        while all([j > 0, lst[j - 1] > lst[j]]):
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
        i += 1
    return lst


if __name__ == "__main__":
    lst = [8, 4, 9, 7, 12, 3, 7, 1, 6, 14, 22, 81, 1]
    print(lst)
    print(insertion_sort(lst))

