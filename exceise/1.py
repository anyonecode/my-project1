'''Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
i
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500'''

D = int(input('enter the deposit'))
W = int(input('enter the withdrawal'))
total = D-W
print(total)
while True:
    if total !=0:
        d = int(input('enter the deposit'))
        total = total+d
        print(total)
        if total!=0:
            w = int(input('enter the withdrawal'))
            total = total-w
            print(total)
    else:
        print('zero balance')
        break

