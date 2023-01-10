# '''1)	Python Check If File Exists'''
# import os.path
# file = r'C:\Users\ManiKandan\PycharmProjects\file handeling\demo.txt'
# flag = os.path.isfile(file)
# if flag:
#     print(f'the file{file} exist')
# else:
#     print(f'the file{file} not exist')
#
# '''2)	Python Check File Size'''
# import os
#
# file_size = os.path.getsize(r'C:\Users\ManiKandan\PycharmProjects\file handeling\demo.txt')
# print("File Size is :", file_size, "bytes")
#
# '''3)	Python Count Number of Lines in a File'''
# f = open('sree.txt','r')
# a = f.readlines()
# print('number of lines : ',len(a))

# '''4)	Python Search for a String in Text Files'''
# f = open('sree.txt','r')
# word = str(input('enter a string'))
# contant = f.read()
# # lines = f.readlines()
# # for line in lines:
# if word in contant:
#     print('the string is found')
# else:
#     print('string is not found')
#
# '''5)	Read Specific Lines From a File in Python'''
#
# x = open('sree.txt','r')
# line_number = [0,1]
# for count,line in enumerate(x):
#     if count in line_number:
#         print(line.strip())

# '''6)	Delete Lines From a File in Python'''
#
# lines = [ ]
# y  = open('sree.txt','r')
# lines = y.readlines()
#
# y  = open('sree.txt','w')
# for number,line in enumerate(lines):
#     if number not in [0]:
#         y.write(line)
#
# '''7)	Writing List to a File in Python'''
#
# name = ['sreehari','hari','sree']
# y = open('sreehari.txt','w')
# for add in name:
#     y.write('%s '% add)
# y = open('sreehari.txt', 'r')
# print(y.read())

# '''8)	Python List Files in a Directory'''
# import os
#
# path = "C:\\Users\\ManiKandan\\PycharmProjects\\file handeling"
# dir_list = os.listdir(path)
# print(f"Files and directories in {path} : ")
#
# print(dir_list)
# print('')
# '''9)	Python Count Number of Files in a Directory'''
# import os
#
# path = "C:\\Users\\ManiKandan\\PycharmProjects\\file handeling\\assignment"
# dir_list = os.listdir(path)
# print(f"Files and directories in {path} : ")
#
# print(dir_list)
# print(len(dir_list))

# '''10)	Python list Files in Directory with Extension txt'''
#
# import os
#
# path = r'C:\Users\ManiKandan\PycharmProjects\file handeling\assignment'
#
# res = []
#
# for new_file in os.listdir(path):
#     if new_file.endswith('.txt'):
#         res.append(new_file)
# print(res)
#
# '''11)	Python Remove/Delete Non-Empty Folder'''
#
# import shutil
# shutil.rmtree(r'C:\Users\ManiKandan\PycharmProjects\file handeling\assignment\dictS')

'''12)	Python Get File Creation and Modification DateTime'''

import datetime
import os

path = r'C:\Users\ManiKandan\PycharmProjects\file handeling\assignment\empty'
mtime = os.path.getmtime(path)
dtm = datetime.datetime.fromtimestamp(mtime)
print('modified time : ',dtm)
ctime = os.path.getctime(path)
dtc = datetime.datetime.fromtimestamp(ctime)
print('created on : ',dtc)
