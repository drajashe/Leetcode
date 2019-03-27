'''Recursive Version of Binary Search
def rec_bin_search(arr,ele):

    # Base Case!
    if len(arr) == 0:
        return False

    # Recursive Case
    else:

        mid = len(arr)/2

        # If match found
        if arr[mid]==ele:
            return True

        else:

            # Call again on second half
            if ele<arr[mid]:
                return rec_bin_search(arr[:mid],ele)

            # Or call on first half
            else:
                return rec_bin_search(arr[mid+1:],ele)'''


def bin_search(arr,ele):
    mid_pt=len(arr)//2
    if(len(arr)%2!=0):
        mid_pt=mid_pt+1
    if(arr[mid_pt]==ele):
        return True
    elif(ele>arr[mid_pt]):
        i=mid_pt+1
        while i < len(arr):
            if(arr[i]==ele):
                return True
            i = i + 1

    else:
        i = 0
        while i < len(arr):
            if (arr[i] == ele):
                return True
            i = i + 1

    return False

print(bin_search([1,2,3],8))


"""def binary_search(arr,ele):
    
    # First and last index values
    first = 0
    last = len(arr) - 1
    
    found = False
    
    
    while first <= last and not found:
        
        mid = (first+last)/2 # or // for Python 3
        
        # Match found
        if arr[mid] == ele:
            found = True
        
        # Set new midpoints up or down depending on comparison
        else:
            # Set down
            if ele < arr[mid]:
                last = mid -1
            # Set up 
            else:
                first = mid + 1
                
    return found"""