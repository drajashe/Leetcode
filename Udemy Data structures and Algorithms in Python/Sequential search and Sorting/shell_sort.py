'''Implementation of Shell Sort
The shell sort improves on the insertion sort by
breaking the original list into a number of smaller sublists,
each of which is sorted using an insertion sort. The unique way
that these sublists are chosen is the key to the shell sort.
Instead of breaking the list into sublists of contiguous items,
the shell sort uses an increment i, sometimes called the gap,
to create a sublist by choosing all items that are i items apart.
Resources for Review
Check out the resources below for a review of Shell sort!

Wikipedia
Visual Algo
Sorting Algorithms Animcation with Pseudocode

'''

def shell_sort(arr):
    sublistcount=len(arr)//2
    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion_sort(arr,start,sublistcount)

        print('After increments of size',sublistcount)
        sublistcount=sublistcount//2
    return arr



def gap_insertion_sort(arr,start,gap):
    # For every index in array
    for i in range(start+gap, len(arr),gap):

        # Set current values and position
        currentvalue = arr[i]
        position = i

        # Sorted Sublist
        while position >gap and arr[position-gap] > currentvalue:
            arr[position] = arr[position - gap]
            position = position - gap

        arr[position] = currentvalue

print(shell_sort([1,2,3,22,5,77,88,6,99,9]))

