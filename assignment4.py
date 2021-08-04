 Q1: Write a program to reverse a string.
# i = "1234abcd"
# print(i[::-1])


# Q2: Write a function that accepts a string and prints the number of uppercase and lowercase letters.
str=input("Enter a string: ")
upper=0
lower=0
for i in range(len(str)):
      #to lower case letter
      if(str[i]>='a' and str[i]<='z'):
          lower+=1
      #to upper case letter
      elif(str[i]>='A' and str[i]<='Z'):
          upper+=1
print('Lower case letters= ',lower)
print('Upper case letters=' ,upper)


# Q3: Create a function that takes a list and returns a new list with unique elements of the first list.
l = [3,3,3,3,52,73,12,6,55,5]
nl = list(set(l))
print(nl)


# Q4: Write a program that accepts hyphen-separated sequence of words as input and prints them in hyphen seperated after sorting alphabetically.
# words = input("Enter a sequence of hyphen-separated words: ")
l = words.split("-")
l.sort()
print('-'.join(l))


# Q5: Write a program that accepts a sequence of words as input and prints the words after making all the characters in the sentence capitalized.
i = input("Enter a sequence of words: ")

 print(i.upper())


# Q6: Define a funtion that can recieve two integral numbers in string form and compute their sum and print it on the console.
 a = input("Enter first integral number: ")
 b = input("Enter second integral number: ")

def addition(a,b):
    res = int(a)+int(b)
    return res

 print("Sum is: ",addition(a,b))


 Q7: Define a funtion that can accept two strings as input and print maximum length string. If same length, print both line by line.
 a = input("Enter first string: ")
 b = input("Enter second string: ")

 def length(a,b):
     if len(a)==len(b):
         print(a)
         print(b)
     elif len(a) > len(b):
         print(a)
     else:
         print(b)

 length(a,b)


 Q8: Define a function which can generate and print a tuple where the values are square of numbers 1-20.
 f = tuple(map(lambda a:a*a,range(1,21)))
 print(f)


 Q9: Write a funtion "showNumbers" that takes parameter "limit". It should print all numbers between 0 and limit with label to identify the even and odd numbers.
 def showNumbers(limit):
     for i in range(0,limit+1):
         if i%2==0:
             print(i ,"EVEN")
         else:
             print(i ,"ODD")

 showNumbers(10)


 Q10: Write a program which uses filter() to make a list whose elements are even numbers between 1-20.
 f = list(filter(lambda a:a%2==0,range(1,21)))
 print(f)


 Q11: Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in set.
 l = [1,2,3,4,5,6,7,8,9,10]

 f = list(filter(lambda a:a%2==0,l))
 m = list(map(lambda a:a*a,f))

 print(f)
 print(m)


 Q12: Write a function to compute 5/0 and use try/except to catch the exceptions.
 def f():
     return 5/0

 try:
     f()
 except ZeroDivisionError:
     print("You cant divide a number by 0!")


 Q13: Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce()
 from functools import reduce

 l = [1,2,3,4,5,6,7]

 f = reduce(lambda a,b: 10*a+b,l,0)
 print(f)


 Q14: Write a program in Python to find the values not divisible by 3 but are a multiple of 7.
 f = list(filter(lambda a:a%3!=0 and a%7==0,range(0,101)))
 print(f)


 Q15: Write a program to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.
 l = [2,5,4,10]

 def square(x):
     return x**2

 m = list(map(square, l))
 print(m)


 Q16: What is the output of the following code:
 (i)
 def foo():
     try:
         return 1
     finally:
         return 2
 k = foo()
 print(k)

 This will return with an output of 2 because of the "finally" statement defined in the function.


 (ii)
 def a():
     try:
         f(x,4)
     finally:
         print('after f')
         print('after f?')
 a()

 This will return with a two statements saying "after f" and "after f?" because of the finally statement, but will also get a Traceback error due to not defining f in the try statement.
