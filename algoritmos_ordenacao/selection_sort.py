def select_smaller(alist, i):
    smaller = alist[i]
    index_smaller = i
    for c in range(i, len(alist)):
        if smaller > alist[c]:
            smaller = alist[c]
            index_smaller = c
    return index_smaller


def selection_sort(alist):
    for i in range(len(alist)):
        index_smaller = select_smaller(alist, i)
        alist[i], alist[index_smaller] = alist[index_smaller], alist[i]

