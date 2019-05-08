# encoding=utf-8
# function
def greet():
    print('Hello, Kitty!')


greet()


# function with parameters
# Note the terminology used
#  - the names given in the function definition are called parameters
#    whereas the values you supply in the function call are called arguments.
def compare(a, b):
    if a == b:
        print('{0} is equal to {1}'.format(a, b))
    elif a < b:
        print('{0} is lower than {1}'.format(a, b))
    else:
        print('{0} is higher than {1}'.format(a, b))


compare(2, 4)

number = 10


# local variable
def localize(x):
    print('X is', x)
    x = 2
    print('Localized X is', x)


localize(number)
print('But X is still', number)


# the global statement
def globalize():
    global number
    print('Number is', number)
    number = 2
    print('Now Number is globalized as', number)


print('number =', number)
globalize()
print('number =', number)


# default argument value
def repeat(content, times=1):
    print(content * times)


repeat('Hello, Kitty!')
print('*' * 10)
repeat('Hello, Kitty! \n', 3)
