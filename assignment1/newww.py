# a = "apple"
# index=0
# while index<len(a):
#     letter=a[index]
#     print (index,letter)
#     index+=1
#
# # a = "sreehari"
# # b = "vishnu"
# # for i in range(len(a)):
# #     print(i,a[i])
# # for j in range(len(b)):
# #     print(j, b[j])
#remove special symbols / puntuation from  a string
#ans : jon is developer music director
str = "*/jon is 2developer & music director"
x=[]
for char in str:
    if char.isalpha():
        x.append(char)
print(''.join(x))