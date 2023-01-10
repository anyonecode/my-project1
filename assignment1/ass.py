rows = int(input('enter a number'))

for i in range(1,rows+1):
    for j in range(rows-i,0,-1):
        print(j, end=' ')
    print('')