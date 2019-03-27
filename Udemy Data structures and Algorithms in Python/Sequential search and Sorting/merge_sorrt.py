'''Implementation of Merge Sort
Merge sort is a recursive algorithm that continually splits a list in half.
If the list is empty or has one item, it is sorted by definition (the base case).
If the list has more than one item, we split the list and recursively invoke a merge sort
 on both halves. Once the two halves are sorted, the fundamental operation, called a merge,
  is performed. Merging is the process of taking two smaller sorted lists and combining them
   together into a single, sorted, new list.

'''
def merge_sort(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        left_array=arr[:mid]
        right_array=arr[mid:]
        merge_sort(left_array)
        merge_sort(right_array)
        i=j=k=0
        while i < len(left_array) and j < len(right_array):
            if(left_array[i]<right_array[j]):
                arr[k]=left_array[i]
                i+=1
            else:
                arr[k]=right_array[j]
                j+=1
            #print("merging", arr)
            k+=1

        while(i < len(left_array)):
            arr[k]=left_array[i]
            i+=1
            k+=1
            #print("merging", arr)
        while(j<len(right_array)):
            arr[k] = right_array[j]
            j+=1
            k+=1
    print("merging",arr)
    return arr
print(merge_sort([11,2,5,4,7,6,8,1,23]))
