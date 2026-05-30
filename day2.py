#conditional statements

#find the odd and even from number
num=int(input("enter the number:"))
if num%2==0:
    print("even number is",num)
else:
    print("odd number:",num)

number=int(input("enter the number:"))
num="even" if number%2==0 else "odd"
print(num)

#find positive and negative from the number
num=int(input("enter the number:"))
if num>0:
    print("its a positive number",num)
elif num<0:
    print("its a negative number",num)
else:
    print("zero also a positive number",num)

number=int(input("enter the number:"))
num="positive" if number>0 else "negative"
print(num)

#which numbers are divisible by 5
num=int(input("enter the number:"))
if num%5==0:
    print("it is divisible by 5-",num)
else:
    print("it is not divisible by 5-",num)

#find the largest of two numbers
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if num1>num2:
    print(f"the {num1} is largest of the two numbers")
elif num1<num2:
    print(f"the {num2} is largest of two numbers")
else:
    print(f"both {num1} and {num2} are equal numbers")

#find largest of three numbers
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if num1>num2 and num1>num3:
    print(f"the {num1} is largest of the three numbers")
elif num2>num1 and num2>num3:
    print(f"the {num2} is largest of the three numbers")
elif num3>num1 and num3>num1:
    print(f"the {num3} is largest of the three numbers")
else:
    print(f"the three number are {num1},{num2} and {num3} are equal numbers")

#leap year
year=int(input("enter the year:"))
if year%400==0:
    print("it is a leap year",year)
elif year%4==0 and year%100==0:
    print("it is a leap year",year)
else:
    print("it is not a leap year")

#grade based on marks
marks=int(input("enter the marks:"))
if marks<=100 and marks>=90:
    print("its a grade A")
elif marks<90 and marks>=70:
    print("its a grade B")
elif marks<70 and marks>=50:
    print("it a grade C")
elif marks<50 and marks>=30:
    print("its a grade D")
elif marks<30 and marks>=0:
    print("its a grade E, it means your failed")
else:
    print("INVALID MARKS PLEACE TRY AGAIN ")

#the number should be three digits
"""num=int(input("enter the number:"))
if num>99 and num<10000:
    print("it is a three digit number",num)
else:
    print("it is not a three digit number",num)"""

#profit and loss
"""cost=int(input("enter the cost:"))
price=int(input("enter the price:"))
if price>cost:
    profit=price-cost
    print("its a profit")
elif cost>price:
    print("its a loss")
else:
    print("its not a profit or loss")"""

#operations

"""a=int(input("enter the number:"))
b=int(input("enter the number:"))
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)"""

#even or odd using arithmetic operator
"""num=int(input("enter the number:"))
if num%2==0:
    print("it is even")
else:
    print("it is odd")"""


