# #1.	Multiply all the numbers in a list using function
def mul(x):
    num = 1
    for i in x:
        num = num*i
    return (num)
j = [2, 3, 5]
print(mul(j))
# #2Write a Python program to reverse a string.
#
# def revers():
#     print("reverse number",str[::-1])
# str = "1234abcd"
# revers()
#3	Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument
# def factrorial(n):
#     fact = 1
#     for i in range(n,1,-1):
#         fact = fact*i
#     print(f"it is a factorial {num} is  {fact}")
# num = int(input("enter a number"))
# factrorial(num)
# #4. Write a Python function that takes a number as a parameter and check  the number is prime or not.
# num = int(input("enter a number"))
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")
# #5. Create an inner function to calculate the addition in the following way
def inner(x,y):
    sum = x+y
    print(sum)
    def outer(z):
        return (z+a)
    p = outer(sum)
    print(p)
d = int(input("enter a number"))
e = int(input("enter a number"))
a = int(input("enter a number"))
inner(d,e)
#6. Generate a Python list of all the even numbers between 4 to 30
# def even_1(x):
#     y = []
#
#     for i in range(3, 30):
#         if i % x == 0:
#             y.append(i)
#     print(y)
# even_1(2)
#
#
##
