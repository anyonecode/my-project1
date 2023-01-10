word = str("ABCD")
n = len(word)
for i in range(n+1):
    ch = chr(65+i)
    for j in range(n+1):
        if (i==0 or i==n or j==0 or j==n):
            print(ch,end=" ")
        else:
            print(' ', end=" ")
    print(" ")