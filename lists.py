""" A list is made from zero or more elements, separated by commas and
surrounded by square brackets. """

""" This shows that values do not need to be unique. """
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

randomness = ["Punxsatawney", {"groundhog": "Phil"}, "Feb. 2"]
leap_years = [2000, 2004, 2008]

""" Empty list. """
empty_list = list()

""" Converts a tuple to a list """
a_tuple = ('ready', 'fire', 'aim')
a_list = list(a_tuple)
print(a_list)

""" Create from a String with split() """
talk_like_a_pirate_day = '9/19/2019'
talk_like_a_pirate_day = talk_like_a_pirate_day.split('/')
print(talk_like_a_pirate_day)
# ['9', '19', '2019']


""" Get Items with a Slice """
marxes = ['Groucho', 'Chico', 'Harpo']

new_marxes = marxes[0:2]
print(new_marxes)
# ['Groucho', 'Chico']

""" Starts at the beginning and goes right by 2 """
new_marxes_2 = marxes[::2]
print(new_marxes_2)
# ['Groucho', 'Harpo']

""" Here, we start at the end and go left by 2 """
new_marxes_3 = marxes[::-2]
print(new_marxes_3)
# ['Harpo', 'Groucho']

""" Reverse a list """
reverse_marxes = marxes[::-1]
print(reverse_marxes)
# ['Harpo', 'Chico', 'Groucho']

""" The reverse() function changes the list but doesn’t return its value. """
marxes.reverse()
print(marxes)

""" Add an Item to the End """
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)
# ['Groucho', 'Chico', 'Harpo', 'Zeppo']

""" Add an Item by Offset with insert() """
marxes.insert(2, 'Gummo')
print(marxes)
# ['Groucho', 'Chico', 'Gummo', 'Harpo', 'Zeppo']

"""Duplicate All Items with *"""
print(["blah"] * 3)
# ['blah', 'blah', 'blah']

""" Combine Lists by Using extend() """
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)
# ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']

""" Change an Item by [offset] """
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)
# ['Groucho', 'Chico', 'Wanda']