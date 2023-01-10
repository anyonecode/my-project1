n=int(input('enter a number'))
for count in range(n+1):
    num=2*count
for i in range(num+1,0,-1):
    if i%2!=0:
        for j in range(num-i):
            print(" ",end=" ")
        for j in range(i):
            print('*  ', end=" ")
        print()