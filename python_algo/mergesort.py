

def mergesort(lst):

    def merge(a, b):
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0] < b[0]:
                c.append(a[0])
                a.remove(a[0])
            else:
                c.append(b[0])
                b.remove(b[0])
        if len(a) == 0:
            c += b
        else:
            c += a
        return c

    if len(lst) < 2:
        return lst
    else:
        middle = len(lst) // 2
        left = mergesort(lst[: middle])
        right = mergesort(lst[middle:])
    return(merge(left, right))


if __name__ == "__main__":

    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    alist = mergesort(alist)
    print(alist)

