'''The cause of an exception is often external to the program itself.
For example, an incorrect input, a malfunctioning IO device etc.
Because the program abruptly terminates on encountering an exception,
it may cause damage to system resources, such as files.
 Hence, the exceptions should be properly handled so that an abrupt termination of the program is prevented.'''

# try :
#     #statements in try block
# except :
#     #executed when error in try block



# try:
#     a=5
#     b= '0'
#     print(a/b)
# except:
#     print('Some error occurred.')
# print("Out of try except blocks.")

#multiple except


try:
    a=5
    b=0
    print (a/b)
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    print ('Division by zero not allowed')
print ('Out of try except blocks')




