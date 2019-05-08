# encoding=utf-8
# I would recommend always using parentheses
# to indicate the start and end of tuple
# even though parentheses are optional.
# Explicit is always better than implicit.
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is:', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of the cages in the new zoo is:', len(new_zoo))

print('All animals in the new zoo are:', new_zoo)
print('Animals brought from the old zoo are:', new_zoo[2])

print('The last animal brought from the old zoo is:', new_zoo[2][2])
print('Number of the animals in the new zoo is:', len(new_zoo) -1 + len(new_zoo[2]))

empty_zoo = ()
