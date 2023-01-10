'''1.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.'''
# import math
#
# row_num = int(input("number of rows: "))
# col_num = int(input("number of columns: "))
# result = [[0 for col in range(col_num)] for row in range(row_num)]
#
# for row in range(row_num):
#     for col in range(col_num):
#         result[row][col]= row*col
#
# print(result)

'''2.Write a program that calculates and prints the value according to the given formula:Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:C is 50. H is 30.D is the variable whose values should be input to your program in a comma-separated sequence.
Example:Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''
# import math
#
# c = 50
# h = 30
# d = [int(input('n1')),int(input('n2')),int(input('n3'))]
# new = [ ]
# for i in d:
#
#     Q = int(math.sqrt(( 2 * c * i)//h))
#     new.append(Q)
#
# print(new)
'''3. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''
# a = ('without','hello','bag','world')
# b =sorted(a)
# print(b)

'''4.  Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.'''
# k = list(input('enter 4 digit numbers using 0 and 1 : ').split(','))
# for i in k:
#     ran =int(i,2)
#     if not ran%5:
#         print(i)

'''5. Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line'''
l = [ ]
for i in range(999,3001):
    s = str(i)
    if (int(s[0])%2==0 and int(s[1])%2==0  and int(s[2])%2==0  and int(s[3])%2==0 ):
        l.append(s)
print(','.join(l))
