'''1.	Write a code to reverse a number'''
# a = str(25)
# print(a[::-1])
# a=2456
# r = 0
# while a !=0:
#     d = a%10
#     r = r*10+d
#     a = a//10
# print(r)
'''2.	Write code of Greatest Common Divisor '''
# x = int(input('first number'))
# y = int(input('second number'))
# result = x%y
# def div(x,y):
#     if result:
#         return result
#     if result==0:
#         return y
# print(f'the greatest common divisor of {x} and {y} is :')
# print(div(x,y))

'''palindrome'''
# a= str(input("enter a letter"))
# b = (a[::-1])
# if b==a:
#     print('it is a palindrome ')
# else:
#     print('it is not a palindrome ')

'''anagram'''
# def check(s1, s2):
#     if (sorted(s1) == sorted(s2)):
#
#         print("The strings are anagrams.")
#
#     else:
#
#         print("The strings aren't anagrams.")
#
#
# s1 = input(" enter a string : ")
#
# s2 = input(" enter other string : ")
# check(s1, s2)
# '''5.	Write code to Calculate frequency of characters in a string'''
# test_str = str(input('enter a string'))
# all_freq = {}
# for i in test_str:
#     if i in all_freq:
#         all_freq[i] += 1
#     else:
#         all_freq[i] = 1
# print(all_freq)
'''6.	Write code to check if two strings match where one string contains wildcard characters'''
# def match(word_1, a, word_2, b):
#     if len(word_2) == b:
#         return len(word_1) == a
#     if len(word_1) == a:
#         for i in range(b, len(word_2)):
#             if word_2[i] != "*":
#                 return False
#         return True
#     if word_2[b] == "?" or word_2[b] == word_1[a]:
#         return match(word_1, a + 1, word_2, b + 1)
#     if word_2[b] == "*":
#         return match(word_1, a + 1, word_2, b) or match(word_1, a, word_2, b + 1)
# def matching(word_1,word_2):
#     return match(word_1, 0, word_2, 0)
# print(matching('XYXZZXY', 'X***Y'))

'''7.	Write to code to check whether a given year is leap year or not.'''
# year = int(input('enter the year'))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("it is a leap year")
# else:
#     print("it is not a leap year")
#
# '''8.	Find non-repeating characters in a string'''
# string = ('sreehari')
# for i in string:
#     count = 0
#     for j in string:
#         if i==j:
#             count+=1
#     if count==1:
#         print(i,end=' ')

'''9.	Write a code to find circular rotation of an array by K positions.'''
# d = int(input('eneter the range'))
# array = (1,2,3,4,5)
# a = [ ]
# for j in array[d:]:
#     a.append(j)
# for i in array[:d]:
#     a.append(i)
# print(a)
'''10.Write the code to for Armstrong number'''
# n = input(('enter a number'))
# a = len(n)
# s = 0
# for i in n:
#     b = int(i)**a
#     s = s+b
# print(s)
# if s == int(n):
#     print("it is amstrong")
# else:
#     print("it is not amstrong")

# '''11.Write a program to check whether a character is a vowel or consonant'''
# a = ['a','e','i','o','u']
# letter = str(input('enter a letter'))
# if letter in a:
#     print('it is a vowel')
# else:
#     print('it is a consonant')