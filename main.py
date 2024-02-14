import math
from math import *

#Tip Calculator
bill = float(input("Bill Cost: "))
service = input("Was your service good? bad, okay, good, or great? ")
if service == "bad":
    total = bill
elif service == "okay":
    total = 1.15*bill
elif service == "good":
    total = 1.2*bill
elif service == "great":
    total = 1.25*bill
print(f"Your total is ${total}")


# # of words in a string
sentence = input("Sentence :")
list = sentence.split()
wordcount = len(list)
print(f"Word Count: {wordcount}")


#even or odd
number = float(input("Number: "))
if (number % 2 == 1):
    print("odd")
elif (number%2 == 0):
    print("even")


#factoring
number = float(input("Number: "))
factors = []
for i in range(1,int(number)):
    if number%i == 0:
        if not i in factors:
            factors.append(int(i))
        if not number/i in factors:
            factors.append(int(number/i))
factors.sort()
for i in factors:
    print(factors)


#greatest common factor
num1 = float(input(""))
num2 = float(input(""))
gcf = 1
if num1 < num2:
    smaller = num1
else:
    smaller = num2
for i in range(1, int(smaller+1)):
    if num1%i == 0 and num2%i == 0:
        gcf = i
print(gcf)