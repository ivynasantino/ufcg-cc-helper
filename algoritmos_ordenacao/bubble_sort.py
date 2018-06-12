def bubble_step(alist):
    changed = False
    for i in range(len(alist)-1):
        if alist[i] > alist[i+1]:
            alist[i], alist[i+1] = alist[i+1], alist[i]
            changed = True
    return changed

def bubble_sort(alist):
    changed = True
    while changed:
        changed = bubble_step(alist)

