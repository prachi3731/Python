# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 08:12:41 2021

@author: Anand Yargole
"""
 Q1: Write a program that calculates and prints the value according to the given formula.
 C = 50
 H = 30
 D = float(input("Enter a value: "))

 Q = ((2*C*D)/H)**0.5

 print(Q)


 Q2: Define a class named Shape and its subclass Square. The Square class has an init function which takes length as argument. Both classes have area function which can print the area of the shape where Shape's area is 0 by default.
 class Shape():
     def __init__(self):
         pass
     def area(self):
         return 0

 class Square(Shape):
     def __init__(self, length = 0):
         Shape.__init__(self)
         self.length = length
     def area(self):
         return self.length * self.length

 sq = Square(5)
 print(sq.area())

 print(Square().area())


 Q3: Create a class to find three elements that sum to zero from a set of n real numbers.
 l = [-25,-10,-7,-3,2,4,8,10]
 n = len(l)
 result = 0

 Researched answer::
 class triple_sum():
     def zero_sum(self,num):
         num,result,i = sorted(num),[],0
         while i < n-2:
             j,k = i+1,n-1
             while j < k:
                 if num[i] + num[j] + num[k] < 0:
                     j += 1
                 elif num[i] + num[j] + num[k] > 0:
                     k -= 1
                 else:
                     result.append([num[i],num[j],num[k]])
                     j,k = j+1,k-1
                     while j < k and num[j] == num[j-1]:
                         j += 1
                     while j < k and num[k] == num[k+1]:
                         k -= 1
             i += 1
             while i < n-2 and num[i] == num[i-1]:
                 i += 1
         return result

 print(triple_sum().zero_sum(l))



 Q4: Create a Time class and initialize it with hours and minutes. Create methods for addTime, displayTime, and diplayMinute.
 class Time():
     def __init__(self, hours, minutes):
         self.hours = hours
         self.minutes = minutes

     def addTime(t1, t2):
         t3 = Time(0,0)
         t3.hours = t1.hours + t2.hours
         t3.minutes = t1.minutes + t2.minutes
         while t3.minutes >= 60:
             t3.hours += 1
             t3.minutes -= 60
         return t3

     def displayTime(self):
         print("The time is ", self.hours, "hours and ", self.minutes, "minutes.")

     def displayMinute(self):
         print((self.hours * 60) + self.minutes, " minutes")

 a = Time(2,40)
 b = Time(3,30)
 c = Time.addTime(a,b)

 c.displayTime()
 c.displayMinute()


 Q5: Write a Person class with an instance variable "age" and a constructor that takes an integer as a parameter. The constructor must assign the integer value to the age variable after confiming the agrument is not negative. If a negative argument is passed then the constructor should set age to - and print "Age is not valid, setting age to 0." Also create yearPasses() and amIOld() methods.
 class Person():
     def __init__(self,age):
         if age < 0:
             print("Age is not valid, setting age to 0")
             self.age = 0
         else:
             self.age = age

     def yearPasses(self):
         self.age += int(input("How many years have passed? "))
         print(self.age)

     def amIOld(self):
         if self.age < 13:
             print("You are young")
         elif self.age < 20:
             print("You are a teenager")
         else:
             print("You are old")

 t = int(input("Enter your age: "))

 age = t
 p = Person(age)
 p.amIOld()
 p.yearPasses()
 p.amIOld()
