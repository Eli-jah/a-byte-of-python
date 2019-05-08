# encoding=utf-8
import pickle

shopping_list = ['apple', 'mango', 'carrot', 'banana']
print('Original shopping list:', shopping_list)

# Get a file handler in 'w'riting binary mode
f = open('shopping_list', 'wb')
# Dump the object into a file
pickle.dump(shopping_list, f)
f.close()

del shopping_list

# Get a file handler in 'r'eading 'b'inary mode
f = open('shopping_list', 'rb')
# Load the object from the file
stored_list = pickle.load(f)
f.close()

print('Stored shopping list:', stored_list)
