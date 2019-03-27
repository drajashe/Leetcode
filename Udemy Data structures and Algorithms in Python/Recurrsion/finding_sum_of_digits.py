'''Finding sum of add of all dig of a number'''
def add_dig(num):
    if(num<10):
        return num
    else:
        rem=num%10
        num=num//10
        return rem+add_dig(num)

print(add_dig(420))