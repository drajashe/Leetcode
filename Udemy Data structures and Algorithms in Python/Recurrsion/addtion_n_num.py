''''Finding the sum of n numbers recursively'''

def recursion_n_num(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return n+recursion_n_num(n-1)
print(recursion_n_num(4))