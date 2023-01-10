# #zip method
# l = ('sreehari','sreerag',"sreeraj")
# l1 = [1,3,4]
# p = zip(l,l1)
# print(dict(p))
# #zip with enumerate method
# name = ('sreehari','sreerag',"sreeraj")
# year = [1,3,4]
# for i ,(name,year) in enumerate(zip(name,year)):
#     print(i,name,year)
# #map method
# name = ['sreehari','sreerag',"sreeraj"]
# p = list(map(list,name))
# print(p)

a= {'sreehari': 1, 'sreerag': 3, 'sreeraj': 4}
c = []
b = [ ]
for i,j in a.items():
    b.append(j)
    c.append(i)
print(c)
print(b)


