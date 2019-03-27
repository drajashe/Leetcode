def GCD(num1,num2):
    factors_num1=[]
    factors_num2 = []
    for i in range(1,num1+1):
        if(num1 % i) ==0:
            factors_num1.append(i)

    for i in range(1, num2+1):
        if (num2 % i) == 0:
            factors_num2.append(i)
    list1=[]
    for each in factors_num2:
        if each in factors_num1:
            list1.append(each)
    return max(list1)

print(GCD(18,24))