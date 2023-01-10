'''write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000-3200'''
a = [ ]
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        a.append(i)
print(a)
'''write a given intergral number n, write a program to generate a dictionary that contain(i,i*i)'''
n = int(input('enter a number'))
r = { }

for i in range(1,n+1):
    r[i]=i*i
print(r)
'''write a program which accepts  SEQUENCE OF comma-sperated number from console and generate a list suppose the follwing input list to tuple'''
a = input("valus")

b = a.split()
