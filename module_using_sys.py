# encoding=utf-8
import sys
from my_module import say_hi, __version__

print('The command arguments are:')
for i in sys.argv:
    print(i)

print('\nThe PYTHONPATH is:', sys.path, '\n')

say_hi()
print('Version:', __version__)
