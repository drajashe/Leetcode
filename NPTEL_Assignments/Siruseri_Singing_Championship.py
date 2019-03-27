'''5
3 23
4 20
11 16
5 19
1 25'''
import os
test_input= open("test_input.txt","r")
all_cases= test_input.readlines()
total_singers=all_cases[0]
test_cases=all_cases[2:]

start=list(all_cases[1].rstrip("\n").split(" "))

#lst1=list(range(int(start[0]),int(start[1])+1,1))

#print(lst1)