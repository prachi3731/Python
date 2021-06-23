# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 13:17:42 2021

@author: Anand Yargole
"""

# 1: Create a list of 10 elements of four different data types.
l = [10,20,2+4j,30,"good job",6.5,34 ]

#2: Create a list of size 5 and execute the slicing structure.
l = [30, 24, "mine", "yours", 3.14]
print(l[0:5:2])


# 3: Write a program to get the sum and multiply all the items on a given list.
# from functools import reduce
from functools import reduce
l = [1,2,3,4,5]
result = reduce (lambda x,y: x*y, l)
print(sum(l))
print(result)


# 4: Find the largest and smallest number from a given list.
num = [40,399,4,454,1,67]
print(max (num))
print(min(num))


# 5: Create a new list which contains the specified numbers after removing even numbers from a predefined list.

l = [26,67,35,60,15,42]
print("List: ",l)
nl = [x for x in l if x%2==0]
l= [x for x in l if x%2!=0]
print("Modified list: ",l)
print("New list: ",nl)


# 6: Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and 30
l = range(1,31)
New_list = list(map(lambda a:a*a,l[:5])) + list(map(lambda a:a*a,l[-5:]))
print(New_list)


# 7: Write a program to replace the last element in a list with another list.
list = [1,3,5,7,9,10]
new_list = [2,4,6,8]
list[-1] = new_list
print(str(list))


# 8: Create a new dictionary by concatenating two dictionaries.
def Merge(dict1, dict2):
    return( dict2. update(dict1))
dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
print (Merge(dict1, dict2))
print (dict2)

# 10: Write a program which accepts a sequence of comma-separated numbers from console and generates list and tuple containing numbers.
values = input("Please enter a sequence of comma separated numbers: ")
l = values.split(",")
t = tuple(l)
print("List: ",l)
print("Tuple: ",t)
