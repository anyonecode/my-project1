#try:
    #statements in try block
# except:
#     #executed when error in try block
# else:
#     #executed if try block is error-free
try:
    f = open(r"C:\Users\ManiKandan\PycharmProjects\file handeling\demofile1.txt",'r')
except FileNotFoundError:
    print('file is found')
else:
    print('file is found')