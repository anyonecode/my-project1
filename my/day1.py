num = int(input('enter a number'))

if num < 0:
    print('entered number is negative')
elif num == 0:
    print('entered number is zero')
else:
    print('entered number is positive')
#next work
#while loop
i=1
while i<=20 :
    print(i)
    i=i+1
#star
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()
    i += 1
#loop
n = int(input('enter number of raws'))
while i<=n:

    print('*',end='')
    i=i+1
