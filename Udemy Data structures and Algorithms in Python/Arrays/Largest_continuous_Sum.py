'''Largest Continuous Sum
Problem
Given an array of integers (positive and negative) find the largest continuous sum.

Solution
If the array is all positive, then the result is simply the sum of all numbers. The negative numbers in the array will cause us to need to begin checking sequences.

The algorithm is, we start summing up the numbers and store in a current sum variable. After adding each element, we check whether the current sum is larger than maximum sum encountered so far. If it is, we update the maximum sum. As long as the current sum is positive, we keep adding the numbers. When the current sum becomes negative, we start with a new current sum. Because a negative current sum will only decrease the sum of a future sequence. Note that we don’t reset the current sum to 0 because the array can contain all negative integers. Then the result would be the largest negative number.
Fill out your solution below:'''


def large_cont_sum(arr):
    # Check to see if array is length 0
    if len(arr) == 0:
        return 0

    # Start the max and current sum at the first element
    max_sum = current_sum = arr[0]

    # For every element in array
    for num in arr[1:]:
        # Set current sum as the higher of the two
        current_sum = max(current_sum + num, num)

        # Set max as the higher between the currentSum and the current max
        max_sum = max(current_sum, max_sum)
    return max_sum
print(large_cont_sum([-1,-2,-20]))


    # def large_continous_sum(list1):
#     max_total=0
#     # start=0
#     # end=0
#     dict1={}
#     i=0
#
#     sum = list1[i]
#     start = i
#     for j in range(i+1,len(list1)):
#         sum += list1[j]
#         if(sum > max_total):
#             #print((i,j),(list1[i],list1[j]),max_total,sum)
#             max_total=sum
#             dict1[max_total] = (i, j)
#     sum=0
#     end = j
#         # print(dict1)
#
#
#     return (max_total,dict1[max_total])
#
#
# print(large_continous_sum([-1,-2,-3,4]))