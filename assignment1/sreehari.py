word = "*"
for i in range(0,7):
    for j in range(0,7):
        if (((i==0 or i==3 or i==6 )and j>1 and j<5)or(j==1 and (i==1 or i==2 or i==6))or(j==5 and (i==0 or i==4 or i==5))):
            print(word,end=" ")
        else:
            print(' ', end=" ")
    print(" ")