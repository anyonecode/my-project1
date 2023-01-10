# from mo import mul
# j = [2, 3, 5]
# print(dir(mul(j)))
# import json
# # ,math ,os ,random,sys
# # print(dir(json))
# # print(dir(math))
# # print(dir(os))
# # print(dir(random))
# # print(dir(sys))
# x = '{"name":"sreehari","age":21,"place":"malappuram"}'
# y = json.loads(x)
# print(y)
import random
print(random.randint(1,100))
print(random.randrange(1,100))
print(random.randrange(0,10,2))
print(random.choice([1,10,19,18]))
x = [1,3,5,8]
random.shuffle(x)
print(x)
import os
d = os.getcwd()
print(d)
os.mkdir('C:\Users\ManiKandan\PycharmProjects\assignment1')