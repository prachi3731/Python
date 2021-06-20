# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 1) write a program if number is divisible by 3 print "consultadd",5 print "python trainning"

num = int(input("Enter any number: "))

if(num%3==0):
    print("Consultadd")
elif(num%5==0):
   print("Python Training")
elif(num%3==0 and num%5==0):
   print("Consultadd -Python Training")
else:
    print(" Error")


#2) Write a program to function allowing users to input 2 numbers for  add, subtract, divide, multiply.
    
    def add(a, b):
        return a+b
    def sub(a, b):
        return a-b
    def Div(a, b):
        return a/b
    def mutiply(a,b):
        retrun (a*b)
    def Avg(a,b,c,d):
        return(a+b+c+d/4)
        print("Select operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")
        print("5. Average")
        
        choice = int(input("enter a choice:"))
        if choice in(1,2,3,4,5):
                num1= int(input("Enter first number:"))
                num2= int(input(" Enter second number:"))
                if choice== 1:
                     print(add(num1, num2))
                     if add(num1, num2) < 0:           
                      print("NEGATIVE")
                 else:
                break
                     elif choice == 2:
               print(sub(num1, num2))
               if sub(num1, num2) < 0:
                   print("NEGATIVE")
                   else:
                    break
            elif choice == 3:
                print(div(num1, num2))
                if div(num1, num2) < 0:
                    print("NEGATIVE")
                else:
                    break
            elif choice == 4:
                 print(mult(num1, num2))
                 if mult(num1, num2) < 0:
                    print("NEGATIVE")
                else:
                    break
             elif choice == 5:
                 num3 = float(input("Enter third number: "))
                 num4 = float(input("Enter fourth number: "))
               print(avg(num1, num2, num3, num4))
               if avg(num1, num2, num3, num4) < 0:
                    print("NEGATIVE")
               else:
                  break
            break
        else:
          print("Invalid Input")


# 3: Write a program to implement given flowchart.
a = 10
b = 20
c = 30

 avg = (a+b+c)/3
 print("avg =",avg)

if avg > a and avg > b and avg > c:
    print("avg is higher than a, b, c")
elif avg > a and avg > b:
    print("avg is higher than a, b")
elif avg > a and avg > c:
    print("avg is higher than a, c")
elif avg > b and avg > c:
    print("avg is higher than b, c")
 elif avg > a:
    print("avg is just higher than a")
elif avg > b:
    print("avg is just higher than b")
elif avg > c:
   print("avg is just higher than c")
else:
    print("avg is the same as a, b, c")




    # 4: Write a program to break and continue in case the user enters a negative number.
while True:
     choice = float(input("Please enter any number: "))
     if choice < 0:
         print("It's Over")
         break
     else:
         print("Good Going")
         break

 # 5: Write a program which will find all numbers between 2000 and 3200 that are divisble by 7 but not 5
list = []
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
         list.append(i)
         print(list)


# 6: What is the output of the following code?

x = 123
for i in x:
     print(i)



#TypeError: 'int' object is not iterable


i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
         break
    else:
        print("error")
# Results in a count from 0 to 2, move the indent before 'else' command.

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# Results in a count 0 1 2 3 4 .
        
# 7: Write a program that prints all the numbers from 0 to 6 except 3 and 6.
a = -1
while a < 6:
     a = a + 1
     if a == 3:
         continue
     if a == 6:
         continue
     print(a)
     
 
 # 9: Write a program that asks users to "guess the lucky number" which runs forever unless the correct number is guessed.
num = int(input("Guess the lucky number: "))
guess=90
while True:
    if num != guess:
         num = int(input("Guess the lucky number: "))
    else:
        print("congrats right guess")
        break

 #10: Write a program that asks 5 times to guess the lucky number using a while loop and a counter.
guess = 50
counter = 1
while counter <= 5:
    num = int(input("Type in the " + str(counter) + " number: "))
    if num != guess:
         print("Try again!")
    else:
        print("Good guess!")
        counter = counter + 1

    print("Game over!")






