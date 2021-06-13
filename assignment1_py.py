# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#1) Create three variables in a single line and assign values to them in such a manner that each one of
#them belongs to a different data type.
#Define date types
a_int=10
a_float=60.5
a_complex=1+2j
a_string='prachi'

#define types of data type

type(a_int)
type(a_float)
type(a_complex)
type(a_string)

#2. Create a variable of type complex and swap it with another variable of type integer.

b=int(a_complex) 


#3. Swap two numbers using a third variable and do the same task without using any third variable.
a=50
b=20

temp=a
a=b
b=temp

print(' After swapping value of :{} '.format(a))
print('after sawpping valur of :{} '.format(b))


#without using varible swapping

a = 10
b= 40
 
print ("Before swapping: ")
print("Value of a : ", a, " and b : ", b)
 
# code to swap a and b
a,b = b,a
 
print ("After swapping: ")
print("Value of a : ", a, " and b : ", b)

#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
Version.
    
# taking input from user in python 3.x
    
value = input("Please enter a string:\n")
 
print(f'You entered {value}')


#taking input from user in python  2.x
value = raw_input("Please enter a string:\n")
 
print(f'You entered {value}')

#5. Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the
#final output.

a = int(input("enter first number: "))
b = int(input("enter second number: "))
z= a + b
print("sum:", z)
x=z+30
print (f"final output:", x)

#6. Write a program to check the data type of the entered values.

var = input("Please enter value for a: ", a )
print(f'The input value of data type is {var}')
type(var)

#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#UPPERCASE.

UccVariable=7
lccvariable=7
snake_case=4
UCVARIABLE=10

#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?
a_int = 11
type(a_int)
a_int_to_float = float(a_int)
a_int_to_float
type(a_int_to_float)


a_int_to_complex = complex(a_int)
a_int_to_complex
type(a_int_to_complex)


a_int_to_str = str(a_int)
a_int_to_str
type(a_int_to_str)
