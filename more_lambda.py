# encoding=utf-8


# Passing tuples around
def get_error_details():
    # OR: return (200, 'Success')
    return 200, 'Success'


# OR: (error_code, error_message) = get_error_details() will work the same.
error_code, error_message = get_error_details()

# The assert statement
# When assertion is right, no AssertionError thrown.
assert error_code == 200

print('Error Code:', error_code)
print('Error Message:', error_message)

# Single statement blocks
flag = True
if flag: print('YES')

# Lambda forms
points = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]
points.sort(key=lambda i: i['y'])
print('Sorted points:', points)

# List comprehension
list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [i * 3 for i in list_1 if 1 < i < 6]
print('List 2:', list_2)


# Receiving tuple and dictionary as arguments in functions
def power_sum(power, *args):
    """Return the sum of each argument raised to the specified power."""
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(power_sum(3, 1, 3, 5))


def get_dict(**kwargs):
    """Return the dict of the keywords args"""
    return kwargs


print(get_dict(a=1, b=2, c=3))
