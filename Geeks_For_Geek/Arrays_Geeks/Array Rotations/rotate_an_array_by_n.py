'''Given an array arr[] of N integers. Do the following operation n-1 times. For every Kth operation:

Right rotate the array clockwise by 1.
Delete the (n-k+1)th last element.
Now, find the element which is left at last.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follows. Each test case contains two lines. The first line of each test case contains an integer N. Then in the next line are N space separated values of the array arr[].

Output:
For each test case in a new line print the required result.

Constraints:
1 <= T <= 110
1 <= N <= 106
1 <= A[i] <= 107

Example:
Input
2
4
1 2 3 4
6
1 2 3 4 5 6

Output:
2
3

Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
1) Store d elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the d elements
   arr[] = [3, 4, 5, 6, 7, 1, 2]

'''

class rotate_by_n():
    def rotate_fn(arr1,n):
        temp=[]
        i=0
        while(i<n):
            temp.append(arr1[i])
            i=i+1
        new_arr=()
        new_arr=set(arr1)-set(temp)
        new_arr=list(new_arr)
        i=0
        while (i < n):
            new_arr.append(temp[i])
            i = i + 1
        return (new_arr)


'''rotating one by one '''
class rotate_by_n_oneByone():
    def rotate_fn_1(arr1,n):

        arr2=[]
        arr2=arr1[n:]
        arr2.extend(arr1[:n])
        return arr2


print(rotate_by_n_oneByone.rotate_fn_1([1,2,3,4,5,6,7],2))