#to saparate upper and lower case os a string
str1 = "HeLlo woRld"
p = ('')
q=('')
z =('')
for i in str1:
    if i.isupper():
        p = p+i
    elif i.isspace():
        z=z+i
    else:
        q = q+i
print(p+q)
#difference between tupple and list
""" list is orderd, it can be mutable, present in squre brecket,repetion possible """
list =[2,3,4,5,6,6]
"""tupple is orderd it can be mutable,it many variable in a set,repetion possinle ,it can contain all type  """
tuple = ("sreehari",[1,3,4,5],"hari")
print(type(tuple))
print(type(list))

#string reverse
str = "HeLlo woRld"
print(str[::-1])

#concatinate 2 dictionaries
d1 = {"name":"sreehari","age":12,"place":"malappuram"}
d2 = {"school":"ghss ghg","pin":676102}
d1.update(d2)
print(d1)
#inverted full pyramid
n = int(input("enter a number"))
for i in range(n):
    for j in range(i+1):
        print(' ' ,end=' ')
    for j in range(n-i):
        print("*  " , end=" ")
    print()
str1 = "HeLlo woRld"
for i in str1:
    str = i+str
print(str)