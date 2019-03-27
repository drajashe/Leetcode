#recursive selection sorting
#find min of list and swap with first element
# now continue the recursive action step 2 on remaining list

def selection_sort(A,start_key,n):
    if(start_key >= n-1):
        return A
    min_pos=start_key
    for i in range(min_pos+1,n):
        if(A[i]<A[min_pos]):
            min_pos=i
    temp = A[start_key]
    A[start_key] = A[min_pos]
    A[min_pos] = temp

    return selection_sort(A,start_key+1,min_pos)



print(selection_sort([23,1,2,44,6],0,5))