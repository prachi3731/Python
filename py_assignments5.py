# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 07:29:51 2021

@author: Anand Yargole
"""

Q1: Write a program in Python to allow the error of syntax to be handled using exception handling

try:
     a = 8
     b = 12
     c=a b
     except SyntaxError:
     print("SyntaxError exception was raised")
 else:
     print("No Errors")


 Q2: Write a program in Python to allow the user to open a file by using the argv module. If entered name is incorrect throw an exception and ask them to Enter Name again.
 while True:
     try:
         f = open(input("Please enter a file name: "))
     except FileNotFoundError:
         print("Unexpected error")
     except:
         raise
     else:
         print("File Opened!")
         break


 Q3: Write a program to handle an error if the user entered a number more than 4 digits.
 f = len(input("Please enter a four digit number: "))
 if f != 4:
     print("The length is too short/long!!! Please provide only four digits")
     raise Exception


 Q4: Create a login page backend to ask users to enter the username and password. Ask fo a re-type password with a counter of 3.
 def login():
     counter = 0
     usn = input("Please enter username: ")
     pw = input("Please enter password: ")
     while True:
         rpw = input("Please re-enter password: ")
         if pw != rpw:
             counter += 1
             if counter == 3:
                 print("Too many attempts!")
                 break
             else:
                 print("Try again! ")
         elif pw == rpw:
             print("Correct!")
             break

 login()



 Q6: Read doc.txt file using Python File handling concept and return only the even length string from the file.
 f = open('doc.txt')

 for line in f:
     line = line.strip()
     if len(line)%2 == 0:
         print(line)
