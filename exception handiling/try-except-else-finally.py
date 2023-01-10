# try:
#     #statements in try block
# except:
#     #executed when error in try block
# else:
#     #executed if try block is error-free
# finally:
#     #executed irrespective of exception occured or not
try:
    print('try block')
    x=int(input('Enter a number: '))
    y=int(input('Enter another number: '))
    z=x/y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Division = ", z)
finally:
    print("finally block")
    x=0
    y=0
print ("Out of try, except, else and finally blocks." )
