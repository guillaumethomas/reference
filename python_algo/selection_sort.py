'''
selection sort
Find the smallest card. Swap it with the first card.
Find the second-smallest card. Swap it with the second card.
Find the third-smallest card. Swap it with the third card.
Repeat finding the next-smallest card, and swapping it into the correct
position until the array is sorted.
This algorithm is called selection sort because it repeatedly selects
the next-smallest element and swaps it into place.
'''


def selection_sort(lst):

    for i in range(len(lst)):
        j = i
        min_lst = lst[j]
        min_ind = j
        for k in range(j, len(lst)):
            if lst[k] < min_lst:
                min_lst = lst[k]
                min_ind = k
        lst[j], lst[min_ind] = lst[min_ind], lst[j]
    return lst


if __name__ == "__main__":
    lst = [1, 2, 5, 3, 9, 4, 15, 23, 8, 12]
    a = selection_sort(lst)
    print(a)
