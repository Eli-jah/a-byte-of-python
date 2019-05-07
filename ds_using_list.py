# This is my shopping list
shopping_list = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shopping_list), 'items to purchase.')

print('And these items are:', end=' ')
for item in shopping_list:
    print(item, end=' ')

print('\nI also have to buy some rice.')
shopping_list.append('rice')

print('Then, my shopping list is now:', shopping_list)

print('And I wanna sort my shopping list now,')
shopping_list.sort()
print('So, the sorted shopping list is shown this way:', shopping_list)

print('The 1st item that I wanna buy is:', shopping_list[0])

bought_item = shopping_list[0]

print('Then I bought some', bought_item)

del shopping_list[0]

print('So, now my shopping list is:', shopping_list)
