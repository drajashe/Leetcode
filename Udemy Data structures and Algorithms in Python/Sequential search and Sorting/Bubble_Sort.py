'''Implementation of a Bubble Sort
The bubble sort makes multiple passes through a list.
It compares adjacent items and exchanges those that are out of order.
 Each pass through the list places the next largest value in its proper place.
 In essence, each item “bubbles” up to the location where it belongs.
 Resources for Review
Check out the resources below for a review of Bubble sort!

Wikipedia
Visual Algo
Animation
Sorting Algorithms Animcation with Pseudocode

'''

def bubble_sort(arr):
    
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[j]< arr[i]):
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
                #arr[j]=min
    return arr



print(bubble_sort([4,5,6,7,1,2,3]))