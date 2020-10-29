empty_tuple = ()

one_marx = 'Groucho',
# >>> one_marx
# ('Groucho',)

one_marx = ('Groucho',)
# >>> one_marx
# ('Groucho',)

marx_tuple = 'Groucho', 'Chico', 'Harpo'
# >>> marx_tuple
# ('Groucho', 'Chico', 'Harpo')
# >>> type(marx_tuple)
# <class 'tuple'>

"""The tuple() conversion function makes tuples from other things"""
marx_list = ['Groucho', 'Chico', 'Harpo']
# >>> tuple(marx_list)
# ('Groucho', 'Chico', 'Harpo')

"""Combine Tuples by Using +"""
# >>> ('Groucho',) + ('Chico', 'Harpo')
# ('Groucho', 'Chico', 'Harpo')

"""Duplicate Items with *"""
# >>> ('yada',) * 3
# ('yada', 'yada', 'yada')

"""Iterate"""
# >>> words = ('fresh','out', 'of', 'ideas')
# >>> for word in words:
#     print(word)

"""Modify a Tuple"""
# >>> t1 = ('Fee', 'Fie', 'Foe')
# >>> t2 = ('Flop,')
# >>> t1 += t2
# >>> t1
# ('Fee', 'Fie', 'Foe', 'Flop')




