x = str("python")
y = 6
for i in range(y):
    for j in range(y-i):
        print(' ',end = "")
    for k in range(i+1):
        print(x[k], end =" ")
    print()