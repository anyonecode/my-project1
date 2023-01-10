#find the repeating numbers in 2 list
a= [1,2,3,4]
b=[2,3,4,5]
com = [x for x in a if  x in b ]
print(com)
# count number of spaces in string
str = "my name is sreehari"
u = [i for i in str if i.isspace()]
count = len(u)
print("number of space:",count)
# find the all word that are 4 letters
text = "The teacher is in the classroom"
k= text.split()
print(k)
j = [w for w in k if len(w)<4]
print(j)

#use a nested list comprimention all the numers from 1-1000 that are divisible by a single digite beside one
new_lis = [x for x in range(1,1001) if any(x % y ==0 for y in range(2,10))]
print(new_lis)