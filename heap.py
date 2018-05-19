import operator
# https://codereview.stackexchange.com/questions/176731/binary-heap-object

class BinaryHeap:

    def __init__(self, _comp = operator.gt):
        self.heap = []
        self.comp = _comp
        # comparison operator used to order items in the heap
        # comp(a,b) should return true if a should be stored
        # above b in the heap
        # comp(self.heap[0], self.heap[n]) will be true for
        # any n (when the heap is valid)

        # comp defaults to > which results in a maxheap

    def __str__(self):
        outStr = ""
        n = 0
        # put each layer of the stack on a different line
        while pow(2, n) - 1 < len(self.heap):
            outStr += str( self.heap[pow(2,n)-1 :
                      min(pow(2,n+1)-1, len(self.heap))] ) + "\n"
            n += 1
        return outStr

    def size(self):
        return len(self.heap)

    # returns true if item at i1 should be above that at i2
    def compareAtIndices(self, i1,i2):
        return self.comp(self.heap[i1], self.heap[i2])

    # given a node's index, return the index of that node's first/second child
    # (which is on the left/right when displayed graphically)
    def leftChildIdx(self,i):
        return 2*i + 1
    def rightChildIdx(self,i):
        return 2*i + 2

    # given a node's index, return the index of that node's parent
    def parentIdx(self,i):
        return (i-1) // 2 # integer division to round down

    # add an item to the stack, sorting to restore validity
    def push(self, item):
        self.heap.append(item)
        self.upsort(len(self.heap)-1)

    # remove and return top element, sorting to restore validity
    def pop(self):
        if len(self.heap) == 0:
            return
        top = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.downsort(0)
        else:
            self.heap.pop()
        return top

    # return the top element
    def peek(self):
        return self.heap[0]

    # move an item up, swaping it with its parent(s), to restore heap validity
    def upsort(self, i):
        if i <= 0:
            return
        pIdx = self.parentIdx(i)
        if not self.compareAtIndices(pIdx, i):
            self.swap(pIdx, i)
            self.upsort(pIdx)

    # move an item down, swaping it with its children, to restore heap validity
    def downsort(self, i):
        if i >= len(self.heap):
            # no node at this index in the heap
            return

        lcIdx, rcIdx = self.leftChildIdx(i), self.rightChildIdx(i)
        if lcIdx >= len(self.heap):
            # no left child for node at this index
            swapLeft = False
        else:
            swapLeft = self.compareAtIndices(lcIdx, i)

        if rcIdx >= len(self.heap):
            # no right child for node at this index
            swapRight = False
        else:
            swapRight = self.compareAtIndices(rcIdx, i)

        # if both children could be swapped with parent,
        # compare them to decide which to swap
        if swapLeft and swapRight:
            # if self.compareAtIndices(lcIdx, rcIdx):
            #     swapRight = False
            # else:
            #     swapLeft = False
            swapLeft = self.compareAtIndices(lcIdx, rcIdx)
            swapRight = not swapLeft

        # otherwise heap already valid
        if swapLeft or swapRight:
            self.swap(lcIdx if swapLeft else rcIdx, i)
            self.downsort(lcIdx if swapLeft else rcIdx)

    # swap elements at given indices
    def swap(self,i1,i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]