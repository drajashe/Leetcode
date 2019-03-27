
def insertion_sort_recursive(A,n,next_el):
    if(next_el>=n-1):
        return
    pos = next_el
    temp = 0
    while (pos > 0 and A[pos] < A[pos - 1]):
        temp = A[pos]
        A[pos] = A[pos - 1]
        A[pos - 1] = temp
        pos = pos - 1
    insertion_sort_recursive(A,n,next_el+1)
    return

print(insertion_sort_recursive([1,44,5,77,6,88],6,0))