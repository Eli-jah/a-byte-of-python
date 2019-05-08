# encoding=utf-8
age = 20
name = 'Swaroop'
book = "A Byte of Python"

row_delimiters = '''Unix|Linux: \\n
MacOS: \\r
Windows: \\r\\n
'''

# Here the anti-slash works as the string ligature
row_delimiters_2 = "Unix|Linux: \\n\n\
MacOS: \\r\n\
Windows: \\r\\n\n"

print('The first case:', end='\n\n')

print(row_delimiters)

print('The following would be the same ...', end='\n\n')

print(row_delimiters_2)

print('Another case:', end='\n\n')

print('{0} was {1} years old when he wrote this book {2}'.format(name, age, book), end='\n\n')

print('The following would be the same as the above', end='\n\n')

print('{} was {} years old when he wrote this book {}'.format(name, age, book), end='\n\n')

print('N this would be the same ...', end='\n\n')

print(name + ' was ' + str(age) + 'years old when he wrote this book ' + book)
