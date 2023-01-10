# num = int(input("enter a number"))
new_lis = [x for x in range(1,1001) if all(x % y!=0 for y in range(2,x))]
print(new_lis)
# n = int(input("enter a number"))
# fact = 1
# li = [x for x in range(n,1,-1) if (fact*x)]
# print(li)
# list_1=[1,2,3]
# list_2=[2,4,5,6]
# com = [x for x in list_1 if  x in list_2 ]
# print(com)
# l = ('sreehari','hari','jojo')
# list_2=[1,2,3]
# com=[(x for x in l for y in list_2]
# print(com)