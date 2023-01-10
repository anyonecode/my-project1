'''The loop iterates through nums and keeps adding all the numbers to summ. Again to make it pythonic, we have a function, i.e. Reduce.'''
#reduce(function, iterable, [, initializer])
from functools import reduce
nums = [1, 2, 3, 4, 5]
summ = reduce(lambda x, y: x + y, nums)
summ
# Output: 15