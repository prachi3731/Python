# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 07:49:29 2021

@author: Anand Yargole
""" 
#Q1: Write a program in Python to find out the character in a string which is uppercase using list comprehension.
# s = "This is a sample String"
#
# upper = [i for i in s if i.isupper()]
# print(upper)


# Q2: Write a program to construct a dictionary from the two lists containing the names of students and corresponding subjects.
# students = ['Smit','Jaya','Rayyan']
# subjects = ['CSE','Networking','Operating System']

# # For loops:
# dic = {}
# for x in students:
#     for y in subjects:
#         dic[x] = y
#         subjects.remove(y)
#         break
#
# print(dic)

# # Dictionary comprehension:
# dic = {students[i]: subjects[i] for i in range(len(students))}
#
# print(dic)

# # Zip funtion:
# dic = dict(zip(students,subjects))
#
# print(dic)

####
# initializing lists
#students = ["Rash", "Kil", "Varsha"]
#subjects = ["cs", "networking", "os"]
  
# Printing original keys-value lists
#print ("Original key list is : " + str(students))
#print ("Original value list is : " + str(subjects))
  
# using dictionary comprehension
# to convert lists to dictionary
#res = {students[i]: subjects[i] for i in range(len(students))}
#  
# Printing resultant dictionary 
#print ("Resultant dictionary is : " +  str(res))

# Q3: Learn more about Yield, next, and Generators


# Q4: Write a program in python using generators to reverse the string.
#    
#def reverse(s):
#  str = ""
#  for i in s:
#    str = i + str
#  return str
#  
#s = "Constultadd"
#  
#print ("The original string  is : ",end="")
#print (s)
#  
#print ("The reversed string(using loops) is : ",end="")
#print (reverse(s))


# Q5: Write an example on decorators.
#def shout(text): 
#    return text.upper() 
#  
#print(shout('Hello')) 
#  
#yell = shout 
#  
#print(yell('Hello')) 
######
#def shout(text): 
#    return text.upper() 
#  
#def whisper(text): 
#    return text.lower() 
#  
#def greet(func): 
#    # storing the function in a variable 
#    greeting = func("""Hi, I am created by a function passed as an argument.""") 
#    print (greeting) 
#  
#greet(shout) 
#greet(whisper) 