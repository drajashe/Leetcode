
'''Insertion Sort builds the final sorted array (or list) one item at a time.
 It is much less efficient on large lists than more advanced algorithms
 such as quicksort, heapsort, or merge sort.'''


def insertion_sort(arr):
    # For every index in array
    for i in range(1, len(arr)):

        # Set current values and position
        currentvalue = arr[i]
        position = i

        # Sorted Sublist
        while position > 0 and arr[position - 1] > currentvalue:
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = currentvalue


def insertion_sort(A,n):
    for pos in range(1,n):
        next_el= pos
        while(next_el>0 and A[next_el]<A[next_el-1]):
            temp=0
            temp=A[next_el]
            A[next_el]=A[next_el-1]
            A[next_el - 1]=temp
            next_el=next_el-1
    return A

print(insertion_sort([1,44,5,77,6,88],6))

