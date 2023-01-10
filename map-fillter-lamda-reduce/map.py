'''the map function takes in a function and an iterable(list, tuple, etc.) as an input; applies passed function to each item of an iterable and returns a map object(an iterator).'''
#map(function, iterable)
def square(n):
    return n ** 2
squares = map(square, range(1, 10, 2))
squares
# returns map object
list(squares)
# Output: [1, 9, 25, 49, 81]
#using lambda
squares = list(map(lambda n: n ** 2, range(1, 10, 2)))