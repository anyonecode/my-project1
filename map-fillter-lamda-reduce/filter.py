'''The loop iterates through nums and stores every odd number. The conditional statement here filters out the even numbers and returns only the odd numbers. This kind of functionality is known as filtering.'''
#filter(function, iterable)
def find_odd(x):
    if x % 2 != 0:
        return x
nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(find_odd, nums))
print(odds)
# Output: [1, 23, 89]
#using lambda
nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)