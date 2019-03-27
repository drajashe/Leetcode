def insertion_sort(arr):
    start_pos = 1
    while start_pos < len(arr):
        nextpos = start_pos
        while(nextpos>0 and arr[nextpos]<arr[nextpos-1]):
            temp=arr[nextpos]
            arr[nextpos]=arr[nextpos-1]
            arr[nextpos-1]=temp
            nextpos-=1
        start_pos+=1

    return arr


print(insertion_sort([3,4,5,6,1,2,3,9,8]))


