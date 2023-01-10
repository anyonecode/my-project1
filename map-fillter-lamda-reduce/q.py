'''write a lambda program to add 15 to a given number passed as a argument and also multipy x and y print the result'''
y = 6
add = (lambda x:15+x)
print("sum : ",add(5))
print()
# mul = lambda x,y:x*y
# print("multiple of two number : ",mul(5,6))
'''sort list of tuple using lambda'''
input = [('sreehari',66),('hari',88),('jojo',55),('vava',77)]
input.sort(key=lambda x:x[1])
print(input)

input = [('sreehari',66),('hari',88),('jojo',55),('vava',77)]
x = lambda x:x[0]
input.sort(key=x)
print(input)