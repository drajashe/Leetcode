
'''Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

'''

def array_pair(arr1,k):
    ans=[]
    arr1=sorted(arr1)
    if len(arr1)<2:
        return
    for i in arr1:
        complement = k-i
        if (complement in arr1 ) :
            ans.append((i,complement))
            arr1.remove(i)
            arr1.remove(complement)
    print('\n'.join(map(str,list(ans))))
array_pair([1,3,2,2],4)


def pair_sum(arr, k):
    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k - num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)

        else:
            # Add a tuple with the corresponding pair
            output.add((min(num, target), max(num, target)))

    # FOR TESTING
    print('\n'.join(map(str, list(output))))
    return len(output)
    # Nice one-liner for printing output

pair_sum([1,3,2,2],4)