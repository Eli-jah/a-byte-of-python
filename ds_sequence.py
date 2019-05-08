# encoding=utf-8
shopping_list = ['apple', 'mango', 'carrot', 'banana']
name = 'Swaroop'

# Indexing or 'Subscription' operation
print('Item 0 is:', shopping_list[0])
print('Item 1 is:', shopping_list[1])
print('Item 2 is:', shopping_list[2])
print('Item 3 is:', shopping_list[3])
print('Item -1 is:', shopping_list[-1])
print('Item -2 is:', shopping_list[-2])
print('Item -3 is:', shopping_list[-3])
print('Character 0 is:', name[0], end='\n\n')

# Slicing on a list
print('Item 1:3 is:', shopping_list[1:3])
print('Item from 2 to the end is:', shopping_list[2:])
print('Item from 1 to -1 is:', shopping_list[1:-1])
print('Item from the start to the end is:', shopping_list[:], end='\n\n')

# Slicing on a string
print('Characters 1:3 are:', name[1:3])
print('Characters from 2 to the end are:', name[2:])
print('Characters from 1 to -1 are:', name[1:-1])
print('Characters from the start to the end are:', name[:])
