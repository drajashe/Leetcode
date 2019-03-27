#recursive selection sorting
#find min of list and swap with first element
# now continue the recursive action step 2 on remaining list

def selection_sort(A):
    #length of array
    n= len(A)

    for start_pos in range(len(A)):
        min_pos=start_pos


        temp = 0

        for i in range(min_pos + 1,n):
            if(A[i] < A[min_pos]):
                min_pos=i


        temp=A[start_pos]
        A[start_pos]=A[min_pos]
        A[min_pos]=temp
    return A

print(selection_sort([23,1,2,44,6]))