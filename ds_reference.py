print('Sample Assignment')

shopping_list = ['apple', 'mango', 'carrot', 'banana']
# my_list is just another name pointing to the same object!!!
my_list = shopping_list

# I purchased the 1st item, so I removed it from the shopping_list
del shopping_list[0]

print('Shopping list:', shopping_list)
print('My List:', my_list)
# Notice that both shopping_list and my_list are printed
# as the same list without the 1st item 'apple' confirming
# that they are pointing to the same list object

print('Then, copy by making a full slice')
# Make a copy by doing a full slice
my_list = shopping_list[:]
# Then try to remove the 1st item
del my_list[0]

print('Shopping list:', shopping_list)
print('My List:', my_list)
# Notice that they are 2 different list now.
