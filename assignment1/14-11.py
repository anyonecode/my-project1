str = "sreehari hari"
a = str.split(" ")
print(a)
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
