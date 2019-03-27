'''In the first part of the Big-O example section we will go through various iterations of the various Big-O functions. Make sure to complete the reading assignment!

Let's begin with some simple examples and explore what their Big-O is.
O(1) Constant¶'''


def func_constant(values):
    '''
    Prints first item in a list of values.
    '''
    print
    values[0]


print(func_constant([1, 2, 3]))

'''Note how this function is constant because regardless of the list size, the function will only ever take a constant step size, in this case 1, printing the first value from a list. so we can see here that an input list of 100 values will print just 1 item, a list of 10,000 values will print just 1 item, and a list of n values will print just 1 item!'''
#O(n) Linear¶

def func_lin(lst):
    '''
    Takes in list and prints out all values
    '''
    for val in lst:
        print
        val


print(func_lin([1, 2, 3]))