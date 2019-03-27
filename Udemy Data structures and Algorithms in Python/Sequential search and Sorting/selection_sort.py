'''Implementation of Selection Sort
The selection sort improves on the bubble sort by making
 only one exchange for every pass through the list. In order to do this,
 a selection sort looks for the largest value as it makes a pass and, after
 completing the pass, places it in the proper location. As with a bubble sort,
 after the first pass, the largest item is in the correct place. After the second pass,
  the next largest is in place. This process continues and requires n−1 passes to sort n items,
since the final item must be in place after the (n−1) st pass.'''
def selection_sort(arr):

    start=0
    min_pos=0
    while start < len(arr):
        min_pos=start
        i=min_pos+1
        while(i<len(arr)):
            if(arr[i] < arr[min_pos]):
                min_pos=i
            i = i + 1

        temp=arr[min_pos]
        arr[min_pos] = arr[start]
        arr[start]=temp
        start=start+1


    return arr

print(selection_sort([2,8,4,5,1]))

