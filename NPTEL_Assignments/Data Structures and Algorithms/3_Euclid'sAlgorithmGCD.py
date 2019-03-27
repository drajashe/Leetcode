#consider gcd of (m,n) such that m>n, compute if ndivides m return n
#else gcd = gcd(n,m-n and return that value

#
# def euclid_gcdgcd(m, n):
#     factors = []
#     for i in range(min(m, n) + 1, 1, -1):
#         if m % i == 0 and n % i == 0:
#             return i


#recursive function


def euclid_gcd(m,n):
    if(m<n):
        (m,n)=(n,m)
    if(m%n==0):
        return(n)
    else:
        return euclid_gcd(max(n,m-n),min(n,m-n))

print(euclid_gcd(18,24))


#improved euclids
def euclid_gcd2(m,n):
    if(m<n):
        (m,n)=(n,m)
    while(m%n != 0):
        (m,n)=(n,m%n)
    return n
print(euclid_gcd2(18,24))
