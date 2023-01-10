try:
    f = open(r"C:\Users\ManiKandan\PycharmProjects\file handeling\demofile.txt",'r')
except FileNotFoundError:
    print('file is not found')
else:
    print('file is found')