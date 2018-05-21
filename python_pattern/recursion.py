
def fact(numb):
    if isinstance(numb, int) and numb >= 0:
        if numb < 2:
            return 1
        else:
            return numb * fact(numb - 1)
    else:
        raise ValueError


def move(n, source, target, auxiliary):
    '''
    Tower of Hanoi
    https://en.wikipedia.org/wiki/Tower_of_Hanoi
    '''
    if n > 0:
        # move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, auxiliary, target)

        # move the nth disk from source to target
        target[0].append(source[0].pop())

        X = [source, target, auxiliary]
        for i in X:
            if i[1] == "source":
                A = i
            elif i[1] == "auxiliary":
                B = i
            else:
                C = i

        # Display our progress
        print('Tower of Hanoi\n{}\n{}\n{}\n'.format(A[0], B[0], C[0]))

        # move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, auxiliary, target, source)

# initiate call from source A to target C with auxiliary B


if __name__ == "__main__":

    source = ([6, 5, 4, 3, 2, 1], "source")
    print('{} {}'.format(*source))
    target = ([], "target")
    auxiliary = ([], "auxiliary")

    move(len(source[0]), source, target, auxiliary)
