'''
Heap algo from MIT Pseudo code
'''


def max_heapify(arr, i):
    # To maintain the max heap property
    left = i + 2
    right = i + 3
    if i <= len(arr):
        if left <= len(arr):
            if arr[left] > arr[i]:
                # print('{} {}'.format(arr[left], arr[i]))
                largest = left
            else:
                largest = i
        if right <= len(arr):
            if arr[right] > arr[largest]:
                largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            max_heapify(arr, largest)


if __name__ == "__main__":
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print(arr)
    max_heapify(arr, 1)
    print(arr)
