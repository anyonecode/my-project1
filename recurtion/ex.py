# def num(x):
#     return x
# n = 0
# def sum(y):
#     if y>0:
#         result = num(y-1)
#         sum = y+result
#
#         print(sum)
#     else:
#         sum = y
#     return sum
#
# sum(5)
def new(y):
    print(y)
def tri_recursion(k):
  if(k > 0):
    result = new(y) + tri_recursion(k - 1)
    print(result)
    new(3)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
