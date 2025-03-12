"""
A decorator in Python by definition is a function that is used to enhance the features of other functions, here is an example of a decorator that prints the arguments and the result of a function before and after calling it.
we can define an inner function called wrapper and can access the original arguments, keyword arguments and the result of the function that is being decorated.
The wrapper function can be used to print the arguments and the result of the function that is being decorated.
"""


def decorate(func):
    def wrapper(*args, **kwargs):
        print('Before calling the function')
        result = func(*args, **kwargs)
        print(result, args, kwargs)
        print('After calling the function')
        return result
    return wrapper


@decorate
def two_sum(arr, target):

    d = {}
    for number in range(len(arr)):
        if target - arr[number] in d:
            return [number, d[target-arr[number]]]
        d[arr[number]] = number

    return -1


nums, target = [2,7,11,15], 9
print(two_sum(nums, target))