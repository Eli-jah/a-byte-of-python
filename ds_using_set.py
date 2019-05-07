bri = set(['Brazil', 'Russia', 'India'])
# According to the recommendation for PEP 8
# bri = {'Brazil', 'Russia', 'India'}
print('Bri:', bri)

is_india_in_bri = 'India' in bri
print('Is India in Bri?', is_india_in_bri)

is_russia_in_bri = 'Russia' in bri
print('Is Russia in Bri?', is_russia_in_bri)

# Making copy of a set
bric = bri.copy()
# Adding item to a set
bric.add('China')

# is superset of
print('Bric:', bric)
bric_is_superset_of_bri = bric.issuperset(bri)
print('Is Bric superset of Bri?', bric_is_superset_of_bri)

# removing item from a set
bri.remove('Russia')

# intersection operation
intersection = bri & bric  # OR bri.intersection(bric)
print('Intersection of Bri and Bric:', intersection)
