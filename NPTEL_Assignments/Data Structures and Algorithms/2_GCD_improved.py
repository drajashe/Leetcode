def gcd(m,n):
    factors=[]
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            factors.append(i)
    return max(factors) #or return factors[-1

print(gcd(18,24))

# we dont need list

def gcd_2(m,n):
    factors=[]
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            mrcf=i
    return mrcf

print(gcd_2(18,24))

# another way - move backward
def gcd_3(m,n):
    factors=[]
    for i in range(min(m,n)+1,1,-1):
        if m%i==0 and n%i==0:
            return i

print(gcd_2(18,24))