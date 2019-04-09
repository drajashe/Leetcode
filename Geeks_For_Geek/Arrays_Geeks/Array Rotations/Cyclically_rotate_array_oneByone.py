'''Program to cyclically rotate an array by one
Given an array, cyclically rotate the array clockwise by one.

Examples:

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}
Following are steps.
1) Store last element in a variable say x.
2) Shift all elements one position ahead.
3) Replace first element of array with x.'''

def cyc(arr):
    temp=arr[0]
    i=1
    while(i < len(arr)):
        arr[i-1]=arr[i]
        i=i+1
    arr[-1]=temp
    return arr
print(cyc([1,2,3,4,5,6]))



