'''Search an element in a sorted and rotated arrayzΩ
 An element in a sorted array can be found in O(log n) time via binary search.
 But suppose we rotate an ascending order sorted array at some pivot unknown
 to you beforehand. So for instance,
 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to
 find an element in the rotated array in O(log n) time.
 Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
         key = 3
Output : Found at index 8
All solutions provided here assume that all elements in array are distinct.

The idea is to find the pivot point, divide the array in two sub-arrays and
call binary search.
The main idea for finding pivot is – for a sorted (in increasing order)
and pivoted array, pivot element is the only element for which next element
to it is smaller than it.
Using above criteria and binary search methodology we can get pivot element
in O(logn) time'''
def search_S(arr,n,key):
    pivot=find_pivot(arr,n)

    if arr[pivot] == key:
        return pivot
    elif(pivot==-1):
        start=0
        end=n
        ans=binary_search(arr,start,end,key)
    elif(key<arr[pivot]):
        start=0
        end=pivot
        ans=binary_search(arr,start,end,key)
    else:
        start = pivot+1
        end = n
        ans= binary_search(arr,start,end, key)


    return ans


def find_pivot(arr,n):
    for i in range(len(arr)):
        if(arr[i+1]==arr[i]+1):
            pass
        else:
            return i+1

    return -1

def binary_search(arr,start,end,key):

    for i in range(start,end):
        mid_point = (start + end) // 2
        if(key==arr[mid_point]):
            return mid_point
        elif(key<arr[mid_point]):
            return binary_search(arr,start,mid_point,key)
        elif(key>arr[mid_point]):
            return binary_search(arr,mid_point,end, key)

    return mid_point

s= [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = len(s)
key = 3
print(search_S(s,n,key))


'''Improved solution-1) Find middle point mid = (l + h)/2
2) If key is present at middle point, return mid.
3) Else If arr[l..mid] is sorted
    a) If key to be searched lies in range from arr[l]
       to arr[mid], recur for arr[l..mid].
    b) Else recur for arr[mid+1..h]
4) Else (arr[mid+1..h] must be sorted)
    a) If key to be searched lies in range from arr[mid+1]
       to arr[h], recur for arr[mid+1..h].
    b) Else recur for arr[l..mid] 
    '''


def search_in_sort(arr,start,end,key):
    l=arr[0]
    h=arr[-1]
    mid= (arr[0]+arr[-1])//2
    if(key==arr[mid]):
        return mid

    if (arr[l] <= arr[mid]):



        if(key >= arr[l] and key <= arr[mid]):
            return search_in_sort(arr, l, mid - 1, key)


    return search_in_sort(arr, mid + 1, h, key)
    if key >= arr[mid] and key <= arr[h]:
        return search(a, mid + 1, h, key)
    return search(arr, l, mid -1, key)

# Driver program
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 6
i = search_in_sort(arr, 0, len(arr)-1, key)
if i != -1:
    print ("Index: %d"%i)
else:
    print ("Key not found")