mytuple = ("s","r","e","e","h","a","r","i")
str = ""
for i in mytuple:
    str = str+i
print(str)
list = [1,2,3,4,5]
tuple = tuple(list)
print(tuple)
tuple = ("sreehari","google","apple")
a = list(tuple)
p = []
for i in a:
    t = ''
    for j in i:
        if j in t:
            continue
        else:
            t=t+j
    p.append(t)
x = " ".join(p)
print(x)