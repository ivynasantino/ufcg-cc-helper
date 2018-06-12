def ordered_insert(alist, i):
    for i in range(i, 0, -1):
        if alist[i] < alist[i-1]:
            alist[i], alist[i-1] = alist[i-1], alist[i]
        else:
            break

def insertion_sort(alist):
    for i in range(len(alist)):
        ordered_insert(alist, i)

