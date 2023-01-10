'''print largest word'''
f = open('sree.txt','r')
x = f.read()
y = x.split()
z = max(y,key=len)
print(z)
